from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

timeout = 15

time_start = time.time()

while time.time() < time_start + timeout:
    cookie_button = driver.find_element(By.ID,"cookie")
    cookie_button.click()
    if (time_start) % 300000000 == 0:
        time.sleep(5)
print(time_start + timeout)
print(time_start)