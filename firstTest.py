from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

title = driver.title

driver.implicitly_wait(2)

print("Page Title: ", title)

username = driver.find_element(by=By.NAME, value="user-name")
username.send_keys("standard_user")

driver.quit()