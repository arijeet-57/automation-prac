from selenium import webdriver
from selenium.webdriver.common.by import By

def test_submit():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(3.5)

    #Assertions
    assert driver.title == "Swag Labs"

    #Interact
    username = driver.find_element(By.NAME, "user-name")
    password = driver.find_element(By.NAME, "password")
    login = driver.find_element(By.ID, "login-button")

    username.send_keys("standard_user")
    password.send_keys("secret_sauce")

    login.click()

    item = driver.find_element(By.CLASS_NAME, "inventory_item_name ")
    item.click()

    cart = driver.find_element(By.NAME, "add=to-cart")
    cart.click()
    
    back = driver.find_element(By.ID,"back-to-products")
    back.click()

    cart_link = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_link.click()

    checkout = driver.find_element(By.ID, "checkout")
    checkout.click()

    continue_cart = driver.find_element(By.ID, "continue")
    continue_cart.click()

    

    #Takedown
    driver.quit()