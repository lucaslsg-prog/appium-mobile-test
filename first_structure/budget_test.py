import unittest, time, os
from builtins import id
from first_structure.testData import TestData
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

####################### CASE1: SAVE OPERATION SUCCESS #####################################################################################################
    
    def test_app_budget_add(self):

        if self.skipIntro():
            self.driver.implicitly_wait(5)
            if self.openBudgetPage():
                self.addNewItem()
                self.fillNameInput().set_text(TestData.valid_data_list[0])
                self.fillValueInput().set_text(TestData.valid_data_list[1])
                self.saveNewItem()
            else:
                print("Budget page was not opened")
        else:
            print("Not clicked on Skip button")
        
        self.driver.implicitly_wait(10) # waits 5 seconds
        self.assertEqual( # compare the first parameter with what is returned of the second
            TestData.valid_data_list[0], 
            self.driver.find_element(By.ID,"protect.budgetwatch:id/budgetName").get_attribute('text')
        )

####################### CASE2: TRY SAVE BUDGET WITHOUT FILL REQUIRED FIELDS (NAME/VALUE EMPTY) ############################################################# 

    def test_app_budget_add_value_empty(self):
        if self.skipIntro():
            self.driver.implicitly_wait(5)
            if self.openBudgetPage():
                self.addNewItem()
                self.fillNameInput().set_text(TestData.valid_data_list[0])
                self.fillValueInput().set_text("")
                self.saveNewItem()
            else:
                print("Budget page was not opened")
        else:
            print("Not clicked on Skip button")
        self.driver.implicitly_wait(5)
        self.assertEqual(
            TestData.toast_data_list[1],
            self.driver.find_element(By.ID, 'protect.budgetwatch:id/snackbar_text').get_attribute('text')
        )

    def test_app_budget_add_name_empty(self):
        if self.skipIntro():
            self.driver.implicitly_wait(5)
            if self.openBudgetPage():
                self.addNewItem()
                self.fillNameInput().set_text("")
                self.fillValueInput().set_text(TestData.valid_data_list[1])
                self.saveNewItem()
            else:
                print("Budget page was not opened")
        else:
            print("Not clicked on Skip button")
        self.driver.implicitly_wait(5)
        self.assertEqual(
            TestData.toast_data_list[0],
            self.driver.find_element(By.ID, 'protect.budgetwatch:id/snackbar_text').get_attribute('text')
        )

###################### CASE3: TRY SAVE BUDGET WITH INVALID DATA (LETTER IN VALUE, NUMBER IN NAME) #################################

    def test_insert_letter_in_value(self):
        if self.skipIntro():
            self.driver.implicitly_wait(5)
            if self.openBudgetPage():
                self.addNewItem()
                self.fillNameInput().set_text(TestData.valid_data_list[0])
                self.fillValueInput().set_text(TestData.invalid_data_list[1])
                self.saveNewItem()
            else:
                print("Budget page was not opened")
        else:
            print("Not clicked on Skip button")
        self.driver.implicitly_wait(5)
        self.assertEqual(
            TestData.toast_data_list[1],
            self.driver.find_element(By.ID, 'protect.budgetwatch:id/snackbar_text').get_attribute('text')
        )

    def test_insert_number_in_name(self):
        if self.skipIntro():
            self.driver.implicitly_wait(5)
            if self.openBudgetPage():
                self.addNewItem()
                self.fillNameInput().set_text(TestData.invalid_data_list[0])
                self.fillValueInput().set_text(TestData.valid_data_list[1])
                self.saveNewItem()
            else:
                print("Budget page was not opened")
        else:
            print("Not clicked on Skip button")
        self.driver.implicitly_wait(5)
        self.assertEqual(
            TestData.toast_data_list[0],
            self.driver.find_element(By.ID, 'protect.budgetwatch:id/snackbar_text').get_attribute('text')
        )

###################### CASE4: OVER LIMIT IN VALUE AND NAME FIELDS ###################################################################################################

    def test_over_limit_name(self):
        if self.skipIntro():
            self.driver.implicitly_wait(5)
            if self.openBudgetPage():
                self.addNewItem()
                self.fillNameInput().set_text(TestData.invalid_data_list[2])
                self.fillValueInput().set_text(TestData.valid_data_list[1])
                self.saveNewItem()
            else:
                print("Budget page was not opened")
        else:
            print("Not clicked on Skip button")
        self.driver.implicitly_wait(5)
        self.assertFalse(
            TestData.invalid_data_list[2],
            self.driver.find_element(By.XPATH, f"//android.widget.TextView[contains(@text, '{TestData.invalid_data_list[2]}')]").get_attribute('text')
        )

    def test_over_limit_value(self):
        if self.skipIntro():
            self.driver.implicitly_wait(5)
            if self.openBudgetPage():
                self.addNewItem()
                self.fillNameInput().set_text(TestData.valid_data_list[0])
                self.fillValueInput().set_text(TestData.invalid_data_list[3])
                self.saveNewItem()
            else:
                print("Budget page was not opened")
        else:
            print("Not clicked on Skip button")
        self.driver.implicitly_wait(5)
        self.assertEqual(
            TestData.toast_data_list[1],
            self.driver.find_element(By.ID, 'protect.budgetwatch:id/snackbar_text').get_attribute('text')
        )

###################### CASE5: MAX LIMIT VALUE AND NAME (10 AND 30 CHARACTERS) ###################################################################################################

    def test_insert_max_characters_in_name(self):
        if self.skipIntro():
            self.driver.implicitly_wait(5)
            if self.openBudgetPage():
                self.addNewItem()
                self.fillNameInput().set_text(TestData.valid_data_list[2])
                self.fillValueInput().set_text(TestData.valid_data_list[1])
                self.saveNewItem()
            else:
                print("Budget page was not opened")
        else:
            print("Not clicked on Skip button")
        self.driver.implicitly_wait(10)
        self.assertEqual(
            TestData.valid_data_list[2],
            self.driver.find_element(By.XPATH, 
            f"//android.widget.TextView[contains(@text, '{TestData.valid_data_list[2]}')]").get_attribute('text')
        )

    def test_insert_max_characters_in_value(self):
        if self.skipIntro():
            self.driver.implicitly_wait(5)
            if self.openBudgetPage():
                self.addNewItem()
                self.fillNameInput().set_text(TestData.valid_data_list[0])
                self.fillValueInput().set_text(TestData.valid_data_list[3])
                self.saveNewItem()
            else:
                print("Budget page was not opened")
        else:
            print("Not clicked on Skip button")
        self.driver.implicitly_wait(10)
        self.assertEqual(
            f"0/{TestData.valid_data_list[3]}",
            self.driver.find_element(By.XPATH, 
            f"//android.widget.TextView[contains(@text, '0/{TestData.valid_data_list[3]}')]").get_attribute('text')
        )

    def tearDown(self):
        self.driver.quit()

    def skipIntro(self):
        if self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Welcome to Budget Watch')]"):
            skip = self.driver.find_element(By.ID, 'protect.budgetwatch:id/skip')
            skip.click()
            skiped = True
        else: 
            print("Skip button is not visible")
            skiped = False
        return skiped

    def openBudgetPage(self):
        if self.driver.find_element(By.XPATH,"//android.widget.TextView[contains(@text, 'Budget Watch')]"):
            budget = self.driver.find_element(By.XPATH,"//android.widget.TextView[contains(@text, 'Budgets')]")
            budget.click()
            opened = True
        else:
            opened = False 
            print("Not able to get main page")
        return opened

    def addNewItem(self):
        add = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_add')
        add.click()
    
    def fillNameInput(self): 
        name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/budgetNameEdit')
        return name
        
    def fillValueInput(self): 
        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
        return value
        
    def saveNewItem(self):
        save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
        save.click()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidBudget)
    unittest.TextTestRunner(verbosity=2).run(suite)
