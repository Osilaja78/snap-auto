import subprocess

def get_device_name():
    try:
        result = subprocess.run(["adb", "devices"], capture_output=True, text=True)
        lines = result.stdout.splitlines()
        for line in lines[1:]:
            if line.strip() and "device" in line:
                return line.split("\t")[0]  # Returns the first connected device ID
    except Exception as e:
        print(f"Error getting device name: {e}")
    return None

device_name = get_device_name()

def get_android_version():
    try:
        result = subprocess.run(["adb", "shell", "getprop", "ro.build.version.release"], capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        print(f"Error getting Android version: {e}")
    return None

android_version = get_android_version()
print(f"Detected Android Name: {device_name}")
print(f"Detected Android Version: {android_version}")



