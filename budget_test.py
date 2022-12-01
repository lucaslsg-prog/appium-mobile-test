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
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'protect.budgetwatch'
        desired_caps['appActivity'] = '.MainActivity'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def test_app_budget_add(self):

        test_names= [""," ",12,"Lucas"]
        test_values= [" ","","teste_letras",1000]

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
            name.set_text(test_names[3])

            value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
            value.set_text(test_values[3])

            save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
            save.click()
            saved=True
        else:
            print("Budget page was not opened")
        
        if saved == True:
            self.driver.implicitly_wait(5) # waits 5 seconds
            self.assertEqual(test_names[3], self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Lucas')]").get_attribute('text'))

    def test_empty_name(self):
        test_names= [""," ",12,"Lucas"]
        test_values= [""," ","teste_letras",1000]

        if self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Welcome to Budget Watch')]"):
            skip = self.driver.find_element(By.ID, 'protect.budgetwatch:id/skip')
            skip.click()
        else: 
            print("Skip button is not visible")

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
            name.set_text(test_names[0])
            
            value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
            value.set_text(test_values[3])

            save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
            save.click()
            saved=True
            
        else:
            print("Budget page was not opened")
    
        if saved == True:
            toast_empty = self.driver.find_element(By.ID, "protect.budgetwatch:id/snackbar_text")
            self.assertEqual('Budget type is empty', toast_empty.get_attribute('text'))
            self.driver.implicitly_wait(5) # waits 5 seconds
           
            
            
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
            add = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_add')
            add.click()

            name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/nameEdit')
            name.set_text("teste_expense")

            # budget = self.driver.find_element(By.ID,"protect.budgetwatch:id/budgetSpinner")
            # budget.click()
            # select = self.driver.find_element(By.ID,"protect.budgetwatch:id/text[contains(@text, 'test')]")
            # select.click()
            self.driver.implicitly_wait(5)

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
            self.assertEqual("teste_expense", self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'test_expense')]").get_attribute('text'))

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidBudget)
    unittest.TextTestRunner(verbosity=2).run(suite)
