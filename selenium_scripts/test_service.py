import unittest

from selenium import webdriver


class ServiceAppTest (unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:5000/")

    def test_title_name(self):
        self.assertIn('Container', self.driver.title)


    def tearDown(self):
        self.driver.close()

if "__main__" == __name__:
    unittest.main()
