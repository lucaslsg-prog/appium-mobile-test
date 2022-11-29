import unittest, time, os
from builtins import id

import self as self
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from datetime import date
from time import sleep


class AndroidBudget(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '11'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'protect.budgetwatch'
        desired_caps['appActivity'] = '.MainActivity'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def test_app_budget_add(self):

        if self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Welcome to Budget Watch')]"):
            skip = self.driver.find_element(By.ID, 'protect.budgetwatch:id/skip')
            skip.click()
        else: 
            print("Skip button is not visible")
        
        # clicar em budget
        
        if self.driver.find_element(By.XPATH,"//android.widget.TextView[contains(@text, 'Budget Watch')]"):
            budget = self.driver.find_element(By.XPATH,"//android.widget.TextView[contains(@text, 'Budgets')]")
            budget.click()
            page = True
        else:
            page = False 
            print("Not able to get main page")

        if page == True:
            add = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_add')
            add.click()
            
            name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/budgetNameEdit')
            name.set_text("teste2")

            value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
            value.set_text("1000")

            save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
            save.click()
            self.time.sleep(3000)
            saved=True
        else:
            print("Budget page was not opened")
        
        if saved == True:
            self.assertEqual("teste2", self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'teste2')]").get_attribute('text'))


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidBudget)
    unittest.TextTestRunner(verbosity=2).run(suite)
