from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from appium.options.android import UiAutomator2Options
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

# Appium Desired Capabilities
options = UiAutomator2Options().load_capabilities({
    "platformName": "Android",
    "platformVersion": android_version,
    "deviceName": device_name,
    "appActivity": "com.snapchat.android.LandingPageActivity",
    "appPackage": "com.snapchat.android",
    "autoGrantPermissions": True,
    "noReset": True,
    "fullReset": False,
    "disableIdLocatorAutocompletion": True,
})

# Function to click an element by ID or XPath
def click_element(driver, element_id, type=AppiumBy.ID):
    element = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((type, element_id))
    )
    element.click()

def do_snap(driver):
    chat_elements = driver.find_elements(AppiumBy.XPATH, "//androidx.recyclerview.widget.RecyclerView[@resource-id='com.snapchat.android:id/0_resource_name_obfuscated']/android.widget.FrameLayout")
    
    for chat in chat_elements:
        try:
            # Check if "Delivered" is inside the chat element
            delivered = chat.find_element(AppiumBy.XPATH, ".//android.view.View[@content-desc='Delivered']")
            if delivered:
                print("✅ This chat is already delivered. Skipping...")
                continue  # Move to the next chat
            
        except NoSuchElementException:
            pass  # No "Delivered" element found, continue checking

        try:
            # Check if "Received" is inside the chat element
            received = chat.find_element(AppiumBy.XPATH, ".//android.view.View[@content-desc='Received']")
            if received:
                print("✅ Replying to a recieved snap...")
                chat.find_element(AppiumBy.XPATH, '//android.view.View[@content-desc="Camera Reply"]').click()
                capture = driver.find_element(AppiumBy.XPATH, '//android.widget.FrameLayout[@content-desc="Camera Capture"]')
                capture.click()
                send_btn = driver.find_element(AppiumBy.XPATH, '(//android.widget.LinearLayout[@resource-id="com.snapchat.android:id/0_resource_name_obfuscated"])[3]')
                send_btn.click()
                continue  # Move to the next chat
            
        except NoSuchElementException:
            pass  # No "Recieved" element found, continue checking

        try:
            # Check if "New Snap" is inside the chat element
            new_snap = chat.find_element(AppiumBy.XPATH, ".//android.view.View[@content-desc='New Snap']")
            if new_snap:
                print("📩 New Snap found! Opening it...")
                chat.click()  # Open the new snap
                time.sleep(4)  # Wait for it to open

                driver.press_keycode(4)
                time.sleep(3)

                # Open camera to send a snap
                try:
                    # Capture and send snap
                    print("✅ Replying to a recieved snap...")
                    chat.find_element(AppiumBy.XPATH, '//android.view.View[@content-desc="Camera Reply"]').click()
                    capture = driver.find_element(AppiumBy.XPATH, '//android.widget.FrameLayout[@content-desc="Camera Capture"]')
                    capture.click()
                    send_btn = driver.find_element(AppiumBy.XPATH, '(//android.widget.LinearLayout[@resource-id="com.snapchat.android:id/0_resource_name_obfuscated"])[3]')
                    send_btn.click()
                    # camera_button = driver.find_element(AppiumBy.ID, "com.snapchat.android:id/ngs_camera_icon_container")
                    # camera_button.click()
                    # time.sleep(2)

                    # send_button = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'Send')]")
                    # send_button.click()
                    # time.sleep(2)

                    # # Go back to the streaks list
                    # driver.press_keycode(4)  # Android back button
                    # time.sleep(2)
                
                except NoSuchElementException:
                    print("Could not find camera button, skipping...")
                    driver.press_keycode(4)  # Go back
            
        except NoSuchElementException:
            print("⏭️ No new snap, moving to the next chat.")
            continue  # Move to the next chat

# Initialize Appium driver
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

click_element(driver, "com.snapchat.android:id/ngs_chat_icon_container")

do_snap(driver)