import unittest, time, os
from builtins import id

import self as self
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from datetime import date
from time import sleep


class AndroidTransactions(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'protect.budgetwatch'
        desired_caps['appActivity'] = '.MainActivity'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        
            
    def test_app_transactions_expenses_add(self):

        if self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Welcome to Budget Watch')]"):
            skip = self.driver.find_element(By.ID, 'protect.budgetwatch:id/skip')
            skip.click()
        else: 
            print("Skip button is not visible")

        if self.driver.find_element(By.XPATH,"//android.widget.TextView[contains(@text, 'Budget Watch')]"):
            transactions = self.driver.find_element(By.XPATH,"//android.widget.TextView[contains(@text, 'Transactions')]")
            transactions.click()
            page = True
        else:
            page = False 
            print("Not able to get main page")

        if page == True:

            # Automation only for required inputs 
            add = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_add')
            add.click()

            name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/nameEdit')
            name.set_text("teste_expense")

            account = self.driver.find_element(By.ID, 'protect.budgetwatch:id/accountEdit')
            account.set_text("test_account")

            value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
            value.set_text("1000")

            note = self.driver.find_element(By.ID, 'protect.budgetwatch:id/noteEdit')
            note.set_text("test_note")

            save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
            save.click()
            saved=True

        if saved == True:
            self.driver.implicitly_wait(5) # waits 5 seconds
            self.assertEqual("teste_expense", self.driver.find_element(By.ID, 'protect.budgetwatch:id/name').get_attribute('text'))

   
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidTransactions)
    unittest.TextTestRunner(verbosity=2).run(suite)
