from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Appium Desired Capabilities
capabilities = {
    "platformName": "Android",
    "deviceName": "4845395858364798",
    "appPackage": "com.snapchat.android",
    "appActivity": "com.snapchat.android.LandingPageActivity",
    "noReset": True,  # Keeps Snapchat logged in
    "autoGrantPermissions": True,
}

# Initialize Appium Driver
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)

# Function to detect story mentions
def detect_story_mentions():
    print("Checking for story mentions...")

    # Open Snapchat (if it's not already open)
    driver.activate_app("com.snapchat.android")

    # Click on the "Chats" tab where mentions appear
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((AppiumBy.ID, "com.snapchat.android:id/ngs_chat_icon_container"))
    ).click()

    # Find any mention messages
    mentions = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'mentioned')]"))
    )

    if mentions:
        print(f"Found {len(mentions)} mention(s). Replying...")
        for mention in mentions:
            mention.click()
            reply_to_mention()
            time.sleep(2)  # Short delay before the next reply
    else:
        print("No new mentions found.")

# Function to reply to a story mention
def reply_to_mention():
    try:
        # Wait for the reply text field
        reply_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.snapchat.android:id/chat_input_text_field"))
        )

        # Type the auto-reply message
        auto_reply = "Hey! Thanks for mentioning me 😊"
        reply_field.send_keys(auto_reply)

        # Press Enter to send the message
        driver.press_keycode(66)
        print("✅ Reply sent!")
    except Exception as e:
        print(f"❌ Failed to send reply: {e}")

# Continuous Loop to Keep Checking for Mentions
while True:
    try:
        detect_story_mentions()
        time.sleep(30)  # Wait 30 seconds before checking again
    except Exception as error:
        print(f"Error: {error}")
        time.sleep(5)  # Retry after 5 seconds if an error occurs
