import time

from selenium import webdriver


class TestServiceApp(object):

    def setup():  # open Chrome and go to relevant webpage
        driver = webdriver.Chrome()
        driver.get("http://127.0.0.1:5000/")
        return driver

    def lookup(driver):
        # find input area
        search_box = driver.find_element_by_name('teaspoons')
        search_box.clear()  # make sure input area is empty
        try:
            search_box.send.keys('1')  # type in 1
            time.sleep(1)
            search_box.submit()  # click submit
            assert "[('teaspoons', 2)]" in driver.body
        except:
            pass
        driver.back()
        try:
            search_box.send.keys('aardvark')
            time.sleep(1)
            search_box.submit()
        except ValueError:
            print('Give a number')

    def teardown(driver):
        driver.close()

if "__main__" == __name__:
    main()
