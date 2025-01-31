"""
STORY VIEW BOOSTING
"""

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
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
    element = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((type, element_id))
    )
    element.click()

# Function to swipe between stories
def swipe_story(driver):
    size = driver.get_window_size()
    start_x = size['width'] * 0.8  # Start from right side
    end_x = size['width'] * 0.2    # Swipe left
    start_y = size['height'] * 0.5 # Middle of the screen
    driver.swipe(start_x, start_y, end_x, start_y, 500)

def click_story(driver):
    size = driver.get_window_size()
    start_x = size['width'] * 0.8  # Start from right side
    end_x = size['width'] * 0.2    # Swipe left
    start_y = size['height'] * 0.5 # Middle of the screen
    driver.swipe(start_x, start_y, end_x, start_y, 500)


# Initialize Appium driver
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

# Navigate to the Stories page
click_element(driver, "com.snapchat.android:id/ngs_community_icon_container")
sleep(3)

# Open the first story
try:
    click_element(driver, '(//android.widget.FrameLayout[@resource-id="com.snapchat.android:id/friend_card_frame"])[1]', AppiumBy.XPATH)
    sleep(2)
except:
    print("No stories available.")
    driver.quit()
    exit()

while True:
    print('Viewing stories...')
    sleep(6)

    try:
        click_element(driver, '(//androidx.recyclerview.widget.RecyclerView[@resource-id="com.snapchat.android:id/0_resource_name_obfuscated"])[1]', AppiumBy.XPATH)
    except:
        break

print("Story viewing completed.")

# Exit the story view
driver.press_keycode(4)  # Android back button
sleep(1)
driver.quit()
