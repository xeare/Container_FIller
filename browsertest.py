import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5000/")
time.sleep(5)  # Let the user actually see something!
search_box = driver.find_element_by_id('form')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5)  # Let the user actually see something!
driver.close()
