from selenium import webdriver
from selenium.webdriver.common.by import By

def test_submit():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(2)

    #Assertions
    assert driver.title == "Swag Labs"
    
    #Interact
    username = driver.find_element(By.NAME, "user-name")
    password = driver.find_element(By.NAME, "password")
    login = driver.find_element(By.ID, "login-button")

    username.send_keys("locked_out_user")
    password.send_keys("secret_sauce")

    login.click()

    #Takedown
    driver.quit()