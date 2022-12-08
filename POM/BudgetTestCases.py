import unittest
from datetime import date

from MainPage import MainPage
from BudgetPage import BudgetPage
from AddBudgetPage import AddBudgetPage
from appium import webdriver
from Data import TestData
import time

from IntroPage import IntroPage


class MyTestCase(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'protect.budgetwatch'
        desired_caps['appActivity'] = '.MainActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test_create_new_budget(self):
        intro_page = IntroPage(self.driver)
        intro_page.click_skip()
        self.driver.implicitly_wait(30)
        main_page = MainPage(self.driver)
        main_page.click_budget()
        budget_page = BudgetPage(self.driver)
        budget_page.click_add()
        add_page = AddBudgetPage(self.driver)
        self.driver.implicitly_wait(30)
        add_page.type_budget_type(TestData.budget_type)
        add_page.type_budget_value(TestData.budget_value)
        add_page.click_save_button()
        budget_page = BudgetPage(self.driver)
        self.assertEqual(budget_page.get_first_budget(), TestData.budget_type)

    def test_new_budget_without_name(self):
        intro_page = IntroPage(self.driver)
        intro_page.click_skip()
        self.driver.implicitly_wait(30)
        main_page = MainPage(self.driver)
        main_page.click_budget()
        budget_page = BudgetPage(self.driver)
        budget_page.click_add()
        add_page = AddBudgetPage(self.driver)
        self.driver.implicitly_wait(20)
        time.sleep(5)
        add_page.type_budget_value(TestData.budget_value)
        add_page.click_save_button()
        self.assertEqual(add_page.get_error(), TestData.msg_budget_type_empty)

    def test_new_budget_without_value(self):
        intro_page = IntroPage(self.driver)
        intro_page.click_skip()
        self.driver.implicitly_wait(30)
        main_page = MainPage(self.driver)
        main_page.click_budget()
        budget_page = BudgetPage(self.driver)
        budget_page.click_add()
        add_page = AddBudgetPage(self.driver)
        self.driver.implicitly_wait(20)
        add_page.type_budget_type(TestData.budget_type)
        add_page.click_save_button()
        self.assertEqual(add_page.get_error(), TestData.msg_budget_value_empty)

    def test_insert_letter_in_value(self):
        intro_page = IntroPage(self.driver)
        intro_page.click_skip()
        self.driver.implicitly_wait(30)
        main_page = MainPage(self.driver)
        main_page.click_budget()
        budget_page = BudgetPage(self.driver)
        budget_page.click_add()
        add_page = AddBudgetPage(self.driver)
        self.driver.implicitly_wait(20)
        add_page.type_budget_type(TestData.budget_type)
        add_page.type_budget_value(TestData.value_with_letter)
        add_page.click_save_button()
        self.assertEqual(add_page.get_error(), TestData.msg_budget_value_empty)

    def test_insert_number_in_name(self):
        intro_page = IntroPage(self.driver)
        intro_page.click_skip()
        self.driver.implicitly_wait(30)
        main_page = MainPage(self.driver)
        main_page.click_budget()
        budget_page = BudgetPage(self.driver)
        budget_page.click_add()
        add_page = AddBudgetPage(self.driver)
        self.driver.implicitly_wait(20)
        add_page.type_budget_type(TestData.name_with_number)
        add_page.type_budget_value(TestData.budget_value)
        add_page.click_save_button()
        self.assertEqual(add_page.get_error(), TestData.msg_budget_type_empty)

    def test_over_limit_name(self):
        intro_page = IntroPage(self.driver)
        intro_page.click_skip()
        self.driver.implicitly_wait(30)
        main_page = MainPage(self.driver)
        main_page.click_budget()
        budget_page = BudgetPage(self.driver)
        budget_page.click_add()
        add_page = AddBudgetPage(self.driver)
        self.driver.implicitly_wait(20)
        add_page.type_budget_type(TestData.invalid_name_over_limit)
        add_page.type_budget_value(TestData.budget_value)
        add_page.click_save_button()
        self.assertEqual(add_page.get_error(), TestData.msg_budget_type_empty)

    def test_over_limit_value(self):
        intro_page = IntroPage(self.driver)
        intro_page.click_skip()
        self.driver.implicitly_wait(30)
        main_page = MainPage(self.driver)
        main_page.click_budget()
        budget_page = BudgetPage(self.driver)
        budget_page.click_add()
        add_page = AddBudgetPage(self.driver)
        self.driver.implicitly_wait(20)
        time.sleep(5)
        add_page.type_budget_type(TestData.budget_value)
        add_page.type_budget_value(TestData.invalid_value_over_limit)
        add_page.click_save_button()
        self.assertEqual(add_page.get_error(), TestData.msg_budget_value_empty)

    def test_insert_max_characters_in_name(self):
        intro_page = IntroPage(self.driver)
        intro_page.click_skip()
        self.driver.implicitly_wait(30)
        main_page = MainPage(self.driver)
        main_page.click_budget()
        budget_page = BudgetPage(self.driver)
        budget_page.click_add()
        add_page = AddBudgetPage(self.driver)
        self.driver.implicitly_wait(20)
        add_page.type_budget_type(TestData.valid_max_name)
        add_page.type_budget_value(TestData.budget_value)
        add_page.click_save_button()
        self.assertEqual(budget_page.get_first_budget(), TestData.valid_max_name)

    def test_insert_max_characters_in_value(self):
        intro_page = IntroPage(self.driver)
        intro_page.click_skip()
        self.driver.implicitly_wait(30)
        main_page = MainPage(self.driver)
        main_page.click_budget()
        budget_page = BudgetPage(self.driver)
        budget_page.click_add()
        add_page = AddBudgetPage(self.driver)
        self.driver.implicitly_wait(20)
        add_page.type_budget_type(TestData.budget_type)
        add_page.type_budget_value(TestData.valid_max_value)
        add_page.click_save_button()
        self.assertEqual(budget_page.get_first_budget(), TestData.budget_type)


if __name__ == '__main__':
    unittest.main()
