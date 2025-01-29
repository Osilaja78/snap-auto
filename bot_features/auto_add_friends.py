"""
AUTO-ADD FRIENDS AND SENDS THEM ALL A MESSAGE
"""

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os

options = UiAutomator2Options().load_capabilities({
    "platformName": "Android",
    "platformVersion": "10",
    "deviceName": "4845395858364798",
    "appActivity": "com.snapchat.android.LandingPageActivity",
    "appPackage": "com.snapchat.android",
    "autoGrantPermissions": True,
    "noReset" : True,
    "fullReset": False,
    "disableIdLocatorAutocompletion": True,
})

message = input("What message you want to send with the friend request: ")

def click_element(driver,element_id,type=AppiumBy.ID):
    element = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((type, element_id))
    )
    element.click()

    
def type_element(driver,element_id,text):
    element = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((AppiumBy.ID, element_id))
    )
    element.click()
    element.send_keys(text)

    

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)


while True:
    # Open the "Add Friends" section
    click_element(driver, "com.snapchat.android:id/neon_add_friend_button_container")
    
    # Start dynamic handling of "Add" buttons
    index = 1
    while True:
        try:
            # Dynamically construct the XPath for the current button
            add_button_xpath = f'(//android.widget.Button[@content-desc="Add"])[{index}]'
            
            # Click the "Add" button
            click_element(driver, add_button_xpath, AppiumBy.XPATH)
            sleep(5)
            
            # Try sending a message (if applicable)
            try:
                # Locate message button and click it
                msg_buttons = driver.find_elements(AppiumBy.ID, "scu_quick_add_chat")
                if index - 1 < len(msg_buttons):  # Ensure the index is within range
                    msg_buttons[index - 1].click()
                    
                    # Type and send the message
                    type_element(driver, "com.snapchat.android:id/chat_input_text_field", message)
                    driver.press_keycode(66)  # Press Enter to send the message

                    sleep(3)
                    click_element(driver, '(//android.widget.ImageView[@resource-id="com.snapchat.android:id/0_resource_name_obfuscated"])[1]', AppiumBy.XPATH)
                else:
                    print("No chat button available for this friend.")
            
            except Exception as e:
                print(f"Error while sending message for button {index}: {e}")
                pass
            
            # Increment index for the next "Add" button
            index += 1

        except Exception as e:
            # If no more "Add" buttons are found, break the loop
            print(f"No more 'Add' buttons found after index {index - 1}. Exiting loop.")
            break
    
    # Exit the "Add Friends" section
    driver.press_keycode(4)  # Press back button to exit

