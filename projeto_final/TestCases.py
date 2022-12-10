import unittest
from datetime import date

from ViewRecordsPage import ViewRecordsPage
from AddRegisterPages import AddRegisterPages
from appium import webdriver
from Data import TestData
import time



class MyTestCase(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'Money Track'
        desired_caps['appActivity'] = '.MainActivity'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def test_add_new_income(self):
        records_page = ViewRecordsPage(self.driver)
        records_page.open_add_income_page()
        self.driver.implicitly_wait(30)
        income_page = AddRegisterPages(self.driver)
        income_page.insert_price(TestData.valid_price)
        income_page.insert_title(TestData.valid_title)
        income_page.insert_category(TestData.valid_category)
        self.driver.implicitly_wait(30)
        income_page.save_new_register()
        self.driver.implicitly_wait(30)
        self.assertEqual(records_page.get_title(), TestData.valid_title)
        
if __name__ == '__main__':
    unittest.main()
