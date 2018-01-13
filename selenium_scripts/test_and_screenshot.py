import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5000/")
time.sleep(1)  # number of seconds to stay the page
search_box = driver.find_element_by_name('teaspoons')
search_box.send_keys('1536')
search_box.submit()
driver.save_screenshot('1536.png')
time.sleep(1)  # number of seconds to stay the page

driver.back()

search_box = driver.find_element_by_name('teaspoons')
search_box.clear()
search_box.send_keys('25000')
time.sleep(1)
search_box.submit()
driver.save_screenshot('25000.png')

driver.close()
