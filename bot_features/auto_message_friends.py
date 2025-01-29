from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from utils import get_device_name, get_android_version
import sys

device_name = get_device_name()
android_version = get_android_version()

if not device_name:
    print(device_name)
    print("\n❌ Device not detected! Please make sure your phone is connected and USB debugging is enabled.")
    print("👉 Steps to enable USB Debugging:\n1. Go to 'Settings' > 'About phone'\n2. Tap 'Build number' 7 times to enable Developer mode\n3. Go to 'Developer options' and enable 'USB Debugging'\n")
    sys.exit(1)  # Exit the script

# Check if Android version is detected
if not android_version:
    print("\n❌ Could not detect Android version. Make sure ADB is properly set up and your phone is connected.")
    sys.exit(1)

options = UiAutomator2Options().load_capabilities({
    "platformName": "Android",
    "platformVersion": android_version,
    "deviceName": device_name,
    "appActivity": "com.snapchat.android.LandingPageActivity",
    "appPackage": "com.snapchat.android",
    "autoGrantPermissions": True,
    "noReset" : True,
    "fullReset": False,
    "disableIdLocatorAutocompletion": True,
})

# Function to click an element by ID or XPath
def click_element(driver, element_id, type=AppiumBy.ID):
    element = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((type, element_id))
    )
    element.click()

# Function to type text in an input field
def type_element(driver, element_id, text):
    element = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((AppiumBy.ID, element_id))
    )
    element.click()
    element.send_keys(text)

# Initialize Appium driver
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

# User inputs for mass messaging
usernames = input("Enter Snapchat usernames (comma-separated): ").split(',')
message = input("Enter the message you want to send: ")

# Navigate to chat section
click_element(driver, "com.snapchat.android:id/ngs_chat_icon_container")
time.sleep(2)

# Iterate through each username and send message
for username in usernames:
    # Click search icon
    click_element(driver, "com.snapchat.android:id/hova_header_search_icon")
    time.sleep(2)

    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((AppiumBy.ID, "search-textfield"))
    )
    
    search_box.clear()
    time.sleep(1)

    # Type the username
    type_element(driver, search_box, username.strip())
    time.sleep(2)

    # Select the user from search results
    click_element(driver, '(//android.view.View[@resource-id="friend-result-cell"])'.format(username.strip()), AppiumBy.XPATH)
    time.sleep(2)

    # Type the message
    type_element(driver, "com.snapchat.android:id/chat_input_text_field", message)
    time.sleep(1)

    # Press send button (Enter key simulation)
    driver.press_keycode(66)  # Keycode 66 is the "Enter" key
    time.sleep(2)

    print(f"Message sent to {username}")

    time.sleep(3)
    click_element(driver, '(//android.widget.ImageView[@resource-id="com.snapchat.android:id/0_resource_name_obfuscated"])[1]', AppiumBy.XPATH)

print("All messages sent successfully!")

# Close the driver
driver.quit()
