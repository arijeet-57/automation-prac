from appium import webdriver
from appium.options.android import EspressoOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_addition_2_plus_3():
    """Test: 2 + 3 = 5 on MIUI Calculator using Espresso"""
    
    # ✅ Espresso Options (Works perfectly with MIUI)
    options = EspressoOptions()
    options.platform_name = "Android"
    options.device_name = "Android"
    options.udid = "5d2b4c4a0521"
    
    # MIUI specific
    options.no_reset = True
    
    # App
    options.app_package = "com.miui.calculator"
    options.app_activity = ".cal.CalculatorActivity"
    
    # Espresso server config (IMPORTANT)
    options.espresso_server_launch_timeout = 45000
    
    driver = webdriver.Remote(
        command_executor="http://127.0.0.1:4723/wd/hub",
        options=options
    )
    
    wait = WebDriverWait(driver, 10)
    
    try:
        print("🚀 Calculator app starting...")
        time.sleep(3)
        
        # Click 2
        print("Clicking 2...")
        wait.until(EC.element_to_be_clickable(
            (AppiumBy.ID, "com.miui.calculator:id/btn_2_s")
        )).click()
        time.sleep(0.5)
        
        # Click +
        print("Clicking +...")
        wait.until(EC.element_to_be_clickable(
            (AppiumBy.ID, "com.miui.calculator:id/btn_plus_s")
        )).click()
        time.sleep(0.5)
        
        # Click 3
        print("Clicking 3...")
        wait.until(EC.element_to_be_clickable(
            (AppiumBy.ID, "com.miui.calculator:id/btn_3_s")
        )).click()
        time.sleep(0.5)
        
        # Click =
        print("Clicking =...")
        wait.until(EC.element_to_be_clickable(
            (AppiumBy.ID, "com.miui.calculator:id/btn_equal_s")
        )).click()
        time.sleep(1)
        
        # Get result
        print("Reading result...")
        result = wait.until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.miui.calculator:id/result"]')
            )
        ).text
        
        print(f"✅ Result: {result}")
        
        # Verify
        assert result == "5", f"Expected 5, but got {result}"
        print("✅✅ TEST PASSED!")
        
    except Exception as e:
        print(f"❌ TEST FAILED: {str(e)}")
        raise
        
    finally:
        driver.quit()


if __name__ == "__main__":
    test_addition_2_plus_3()