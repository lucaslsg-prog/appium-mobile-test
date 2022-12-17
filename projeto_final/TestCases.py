import unittest
from datetime import date
import pytest
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

    @pytest.mark.order(1)
    def test_try_add_register_old_date(self):
        records_page = ViewRecordsPage(self.driver)
        records_page.open_add_income_page()
        self.driver.implicitly_wait(30)
        income_page = AddRegisterPages(self.driver)
        self.driver.implicitly_wait(30)
        income_page.insert_price(TestData.valid_price)
        income_page.insert_title(TestData.valid_title)
        income_page.insert_category(TestData.valid_category)
        currentDate = income_page.get_current_date()
        income_page.open_calendar()
        self.driver.implicitly_wait(30)

        if income_page.goTo_previous_month():
            self.driver.implicitly_wait(30)
            income_page.click_on_day('1')
            self.driver.implicitly_wait(30)
            self.driver.implicitly_wait(30)
            income_page.click_on_btn_ok()
        
        new_currentDate = income_page.get_current_date()
        self.driver.implicitly_wait(30)
        if new_currentDate != currentDate:
            self.driver.implicitly_wait(30)
            income_page.save_new_register()

        self.driver.implicitly_wait(30)
        records_page.open_week_list()
        records_page.get_period_records('All time')
        self.assertEqual(records_page.get_title(), TestData.valid_title)
        
    @pytest.mark.order(2)
    def test_try_add_register_future_date(self):
        records_page = ViewRecordsPage(self.driver)
        records_page.open_add_income_page()
        self.driver.implicitly_wait(30)
        income_page = AddRegisterPages(self.driver)
        self.driver.implicitly_wait(30)
        income_page.insert_price(TestData.valid_price)
        income_page.insert_title(TestData.valid_title)
        income_page.insert_category(TestData.valid_category)
        currentDate = income_page.get_current_date()
        income_page.open_calendar()

        if income_page.goTo_next_month():
            self.driver.implicitly_wait(30)
            income_page.click_on_day('1')
            self.driver.implicitly_wait(30)
            selectedDate = income_page.get_selected_date()
            self.driver.implicitly_wait(30)
            income_page.click_on_btn_ok()

        self.driver.implicitly_wait(30)
        self.assertNotEqual(currentDate, selectedDate)

    @pytest.mark.order(3)
    def test_edit_register(self):
        records_page = ViewRecordsPage(self.driver)
        records_page.open_add_income_page()
        self.driver.implicitly_wait(30)
        income_page = AddRegisterPages(self.driver)
        self.driver.implicitly_wait(30)
        income_page.insert_price(TestData.valid_price)
        income_page.insert_title(TestData.valid_title)
        income_page.insert_category(TestData.valid_category)
        income_page.save_new_register()
        self.driver.implicitly_wait(30)
        records_page.open_edit_page()
        income_page.insert_title(TestData.title_edited)
        income_page.save_new_register()
        self.driver.implicitly_wait(30)
        self.assertEqual(records_page.get_title(), TestData.title_edited)

    @pytest.mark.order(4)
    def test_delete_register(self):
        records_page = ViewRecordsPage(self.driver)
        records_page.open_add_income_page()
        self.driver.implicitly_wait(30)
        income_page = AddRegisterPages(self.driver)
        self.driver.implicitly_wait(30)
        income_page.insert_price(TestData.valid_price)
        income_page.insert_title(TestData.valid_title)
        income_page.insert_category(TestData.valid_category)
        income_page.save_new_register()
        self.driver.implicitly_wait(30)
        records_page.open_edit_page()
        self.driver.implicitly_wait(30)
        income_page.click_on_delete_icon()
        self.assertEqual(records_page.get_total(),TestData.total_after_delete)

    @pytest.mark.order(5)
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

    @pytest.mark.order(6)
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
        
    @pytest.mark.order(7)
    def test_add_new_price_with_letter(self):
        self.driver.implicitly_wait(30)
        records_page = ViewRecordsPage(self.driver)
        records_page.open_add_income_page()
        self.driver.implicitly_wait(30)
        income_page = AddRegisterPages(self.driver)
        income_page.insert_price(TestData.invalid_price_with_letter)
        income_page.insert_title(TestData.valid_title)
        income_page.insert_category(TestData.valid_category)
        self.driver.implicitly_wait(30)
        income_page.save_new_register()
        self.driver.implicitly_wait(40)
        self.assertEqual(income_page.get_error(), TestData.msg_input_required_empty)
        
    @pytest.mark.order(8)
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
        
    @pytest.mark.order(9)
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
    
    @pytest.mark.order(10)
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
        
    @pytest.mark.order(11)
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

    @pytest.mark.order(12)
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
        
if __name__ == '__main__':
    unittest.main()
