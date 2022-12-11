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
        desired_caps['appPackage'] = 'com.blogspot.e_kanivets.moneytracker'
        desired_caps['appActivity'] = '.activity.record.MainActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

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

    def test_add_new_price_max_characters(self):
        records_page = ViewRecordsPage(self.driver)
        records_page.open_add_income_page()
        self.driver.implicitly_wait(30)
        income_page = AddRegisterPages(self.driver)
        income_page.insert_price(TestData.max_valid_characters_price)
        income_page.insert_title(TestData.valid_title)
        income_page.insert_category(TestData.valid_category)
        self.driver.implicitly_wait(30)
        income_page.save_new_register()
        self.driver.implicitly_wait(30)
        self.assertEqual(records_page.get_title(), TestData.valid_title)
        
    def test_add_new_price_over_limit_characters(self):
        records_page = ViewRecordsPage(self.driver)
        records_page.open_add_income_page()
        self.driver.implicitly_wait(30)
        income_page = AddRegisterPages(self.driver)
        income_page.insert_price(TestData.over_limit_characters_price)
        income_page.insert_title(TestData.valid_title)
        income_page.insert_category(TestData.valid_category)
        self.driver.implicitly_wait(30)
        income_page.save_new_register()
        self.driver.implicitly_wait(30)
        self.assertEqual(income_page.get_error(), TestData.msg_input_over_limit)
        
    def test_add_new_price_with_letter(self):
        records_page = ViewRecordsPage(self.driver)
        records_page.open_add_income_page()
        self.driver.implicitly_wait(30)
        income_page = AddRegisterPages(self.driver)
        income_page.insert_price(TestData.invalid_price_with_letter)
        income_page.insert_title(TestData.valid_title)
        income_page.insert_category(TestData.valid_category)
        self.driver.implicitly_wait(30)
        income_page.save_new_register()
        self.driver.implicitly_wait(30)
        self.assertEqual(income_page.get_error(), TestData.msg_input_required_empty)
        
    def test_add_new_price_empty(self):
        records_page = ViewRecordsPage(self.driver)
        records_page.open_add_income_page()
        self.driver.implicitly_wait(30)
        income_page = AddRegisterPages(self.driver)
        income_page.insert_title(TestData.valid_title)
        income_page.insert_category(TestData.valid_category)
        self.driver.implicitly_wait(30)
        income_page.save_new_register()
        self.driver.implicitly_wait(30)
        self.assertEqual(income_page.get_error(), TestData.msg_input_required_empty)
        
    def test_add_new_category_with_numbers(self):
        records_page = ViewRecordsPage(self.driver)
        records_page.open_add_income_page()
        self.driver.implicitly_wait(30)
        income_page = AddRegisterPages(self.driver)
        income_page.insert_price(TestData.valid_price)
        income_page.insert_title(TestData.valid_title)
        income_page.insert_category(TestData.invalid_category_with_number)
        self.driver.implicitly_wait(30)
        income_page.save_new_register()
        self.driver.implicitly_wait(30)
        self.assertFalse(records_page.get_title(), TestData.valid_title)
        
    def test_add_new_category_empty(self):
        records_page = ViewRecordsPage(self.driver)
        records_page.open_add_income_page()
        self.driver.implicitly_wait(30)
        income_page = AddRegisterPages(self.driver)
        income_page.insert_price(TestData.valid_price)
        income_page.insert_title(TestData.valid_title)
        self.driver.implicitly_wait(30)
        income_page.save_new_register()
        self.driver.implicitly_wait(30)
        self.assertEqual(income_page.get_error(), TestData.msg_input_required_empty)
        
    def test_add_new_title_empty(self):
        records_page = ViewRecordsPage(self.driver)
        records_page.open_add_income_page()
        self.driver.implicitly_wait(30)
        income_page = AddRegisterPages(self.driver)
        income_page.insert_price(TestData.valid_price)
        income_page.insert_category(TestData.valid_category)
        self.driver.implicitly_wait(30)
        income_page.save_new_register()
        self.driver.implicitly_wait(30)
        self.assertEqual(records_page.get_title(), TestData.valid_category)
        
if __name__ == '__main__':
    unittest.main()
