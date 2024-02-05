import subprocess

from appium.options.android import UiAutomator2Options


def android_get_desired_capabilities():
    capabilities = {
        'autoGrantPermissions': True,
        'automationName': 'uiautomator2',
        'newCommandTimeout': 500,
        'noSign': True,
        'platformName': 'Android',
        'platformVersion': '11',
        'resetKeyboard': True,
        'systemPort': 8301,
        'takesScreenshot': True,
        'appPackage': 'com.ajaxsystems',
        'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity'
    }
    if udid := get_udid():
        capabilities.update({'udid': udid})
    return UiAutomator2Options().load_capabilities(capabilities)


def get_udid():
    try:
        result = subprocess.check_output(["adb", "devices"], text=True, stderr=subprocess.STDOUT)
        devices = [line.split('\t')[0] for line in result.strip().split('\n')[1:] if 'device' in line]
        return devices[0] if devices else None
    except Exception as e:
        #log this exeption
        return None
