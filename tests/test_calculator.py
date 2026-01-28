from appium import webdriver #session starter for the appium server
from appium.options.android import UiAutomator2Options #defines the android capabilites/options 
from appium.webdriver.common.appiumby import AppiumBy #strategy for the mobile elements e.g AppiumBy.ID
from selenium.webdriver.support.ui import WebDriverWait #explicit waits
from selenium.webdriver.support import expected_conditions as EC    #using expexted conditions as EC and prevents flaky tests
import time #not used very much (used for small hard waits)


def test_addition_2_plus_3(): #function starts with test so that python automatically detects that it is a test function
    """Test: 2 + 3 = 5 on Stock Android Calculator using UiAutomator2"""

    options = UiAutomator2Options() #assigning variable to the options that creates the capability for the appium server

    # Device capabilities
    options.platform_name = "Android"               #tells that it is an android session and provides its info on platform type
    options.device_name = "Android"                 #tells that it is an android session and provides its info on device name 
    options.udid = "emulator-5554"                  #tells that it is an android session and provides its info on device id using "adb devices"
    options.automation_name = "UiAutomator2"        #tells that it is an android session and provides its info on automation engine used

    # Calculator
    options.app_package = "com.google.android.calculator"       #launchges automatically installed app and no apk installation required
    options.app_activity = "com.android.calculator2.Calculator" 

    # Stability
    options.no_reset = True  #keeps app data and does not erase it 
    options.new_command_timeout = 300   #prevents session timeouts during debugging
    options.disable_window_animation = True     #speedy UI interactions

    driver = webdriver.Remote(                      
        command_executor="http://127.0.0.1:4723",                   #session creation in this part
        options=options  #setting the capabilities/environment/options 
    )

    wait = WebDriverWait(driver, 15)                        #waiting for 15 seconds before the session starts (it is a good practice)

    try:                                                    #writing the test in the try block 
        print("Calculator app launched...")
        time.sleep(2)

        # Click 2
        wait.until(EC.element_to_be_clickable(                                  #wait until tells to wait until the button is clicked to prevent the "ElementNotInteractableException"
            (AppiumBy.ID, "com.google.android.calculator:id/digit_2")   #notice how here we used clickable because we have to input data using the calculator
        )).click()

        # Click +
        wait.until(EC.element_to_be_clickable(
            (AppiumBy.ID, "com.google.android.calculator:id/op_add")
        )).click()

        # Click 3
        wait.until(EC.element_to_be_clickable(
            (AppiumBy.ID, "com.google.android.calculator:id/digit_3")
        )).click()

        # Click =
        wait.until(EC.element_to_be_clickable(
            (AppiumBy.ID, "com.google.android.calculator:id/eq")
        )).click()

        # Read result
        result = wait.until(EC.presence_of_element_located(     #notice how here we used presence because we just need to check whether the result has worked or not
            (AppiumBy.ID, "com.google.android.calculator:id/result_final")
        )).text

        print(f" Result shown: {result}")

        assert result == "5", f"Expected 5 but got {result}" #setting the fail result message (her f is a formatting string witout it it will not print the result it will be 'Expected 5 but got {result}' instead of 'Expected 5 but got 5'  )
        print("TEST PASSED!")   

    finally:                        #after the test completes we quit the driver session
        driver.quit()


if __name__ == "__main__":              #directly runs the test (ot required here as we can just run using pytest but its a good practice )
    test_addition_2_plus_3()
