import time

from selenium import webdriver

from expects import expect, equal


class TestServiceApp(object):

    def setup():  # open Chrome and go to relevant webpage
        driver = webdriver.Chrome()
        return driver

    def lookup(driver):
        # find input area
        driver.get("http://127.0.0.1:5000")
        time.sleep(1)
        search_box = driver.find_element_by_name('teaspoons')
        search_box.clear()  # make sure input area is empty
        search_box.send_keys('1')  # type in 1
        time.sleep(1)
        search_box.submit()
        time.sleep(3)
        expected_result = driver.find_element_by_id('one')
        expect(expected_result).to(equal('_'))
        driver.back()
        try:
            search_box.send_keys('aardvark')
            time.sleep(1)
            search_box.submit()
        except ValueError:
            pass

    def teardown(driver):
        driver.close()

    if "__main__" == __name__:
        driver = setup()
        lookup(driver)
        teardown(driver)
