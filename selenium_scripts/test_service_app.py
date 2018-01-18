from unittest import main, TestCase

from expects import expect, contain, equal
from selenium import webdriver


class TestServiceApp(TestCase):

    def setUp(self):  # open Chrome and go to relevant webpage
        self.driver = webdriver.Chrome()  # self

    def tearDown(self):
        self.driver.close()

    def test_value_error_message(self):
        self.driver.get("http://127.0.0.1:5000")
        search_box = self.driver.find_element_by_name('teaspoons')
        search_box.clear()  # make sure input area is empty
        search_box.send_keys('aardvark')  # type in str
        search_box.submit()
        first_paragraph = self.driver.find_element_by_xpath("//p")
        expect(first_paragraph.text).to(contain("give a number"))

    def test_one_background_color(self):
        self.driver.get("http://127.0.0.1:5000")
        search_box = self.driver.find_element_by_name('teaspoons')
        search_box.send_keys(1)
        search_box.submit()
        one_background_color = self.driver.find_element_by_css_selector(
            '#one').value_of_css_property('background-color')
        expect(one_background_color).to(equal('rgba(0, 0, 255, 1)'))
        # blue

    def test_hundred_background_color(self):
        self.driver.get("http://127.0.0.1:5000")
        search_box = self.driver.find_element_by_name('teaspoons')
        search_box.send_keys(100)
        search_box.submit()
        hundred_background_color = self.driver.find_element_by_css_selector(
            '#hundred').value_of_css_property('background-color')
        expect(hundred_background_color).to(equal('rgba(0, 128, 0, 1)'))
        # green

    def test_ten_thousand_background_color(self):
        self.driver.get("http://127.0.0.1:5000")
        search_box = self.driver.find_element_by_name('teaspoons')
        search_box.send_keys(10000)
        search_box.submit()
        ten_thousand_background = self.driver.find_element_by_css_selector(
            '#tenthousand').value_of_css_property('background-color')
        expect(ten_thousand_background).to(equal(
            'rgba(0, 0, 0, 1)'))
        # black


if "__main__" == __name__:
    main()
