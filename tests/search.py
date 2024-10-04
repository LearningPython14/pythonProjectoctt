import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
time.sleep(4)
driver.get("https://tutorialsninja.com/demo/")
driver.find_element(By.XPATH,"//*[@id=\"search\"]/input")
