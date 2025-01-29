"""
SCHEDULE STORY POSTS
"""

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import schedule
import time
from datetime import datetime

# Appium Desired Capabilities
options = UiAutomator2Options().load_capabilities({
    "platformName": "Android",
    "platformVersion": "10",
    "deviceName": "4845395858364798",
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

def to_story(driver):
    # Click "My Story" option
    click_element(driver, '(//android.widget.ImageView[@resource-id="com.snapchat.android:id/0_resource_name_obfuscated"])[2]', AppiumBy.XPATH)
    time.sleep(2)

def to_friends(driver):
    friend_elements = driver.find_elements(AppiumBy.XPATH, '(//androidx.recyclerview.widget.RecyclerView[@resource-id="com.snapchat.android:id/0_resource_name_obfuscated"])[1]/android.view.View')
    friend_elements = friend_elements[4:]
    print(friend_elements)
    for friend in friend_elements:
        print(friend)
        friend.click()

# Function to upload and post a story
def post_story(driver, where):
    # Open the Snapchat camera
    click_element(driver, "com.snapchat.android:id/ngs_camera_icon_container")  
    time.sleep(1)

    # Upload media from gallery
    click_element(driver, "com.snapchat.android:id/ngs_memories_icon")
    time.sleep(1)

    # Move to camera roll
    click_element(driver, '//javaClass[@text="Camera Roll"]', AppiumBy.XPATH)

    # Select the first item from the gallery (replace if needed)
    click_element(driver, '(//android.view.ViewGroup[@resource-id="com.snapchat.android:id/grid_frameable_container"])[1]', AppiumBy.XPATH)
    time.sleep(1)

    if where == 1:
        # Click "Send to" button
        click_element(driver, "com.snapchat.android:id/send_btn")
        time.sleep(1)
        # Post the story
        to_story(driver)
    elif where == 2:
        # Click "Send to" button
        click_element(driver, "com.snapchat.android:id/send_btn")
        time.sleep(1)
        # Send to friends
        to_friends(driver) 
    else:
        # Click "Send to" button
        click_element(driver, "com.snapchat.android:id/send_btn")
        time.sleep(1)
        # Post to story and send to friends
        to_story(driver)
        to_friends(driver)
    
    click_element(driver, "com.snapchat.android:id/send_to_send_button")
    print(f"Story posted at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Function to schedule a post
def schedule_story(post_time):
    schedule.every().day.at(post_time).do(run_scheduled_post, where_to)

# Function to run the scheduled task
def run_scheduled_post(where):
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    post_story(driver, where)
    driver.quit()

# User input for scheduling
post_time = input("Enter the scheduled post time (HH:MM 24-hour format): ")
print("Where do you want to post to?")
print("1. Story")
print("2. Send to friends")
print("3. Post to story and send to friends")
where_to = input("Enter 1, 2, or 3: ")

schedule_story(post_time)

print(f"Story scheduled for {post_time}. Waiting...")
while True:
    schedule.run_pending()
    time.sleep(1)
