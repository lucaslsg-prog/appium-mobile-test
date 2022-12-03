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

####################### CASE1: SAVE OPERATION SUCCESS #####################################################################################################

    def test_app_budget_add(self):

        if self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Welcome to Budget Watch')]"):
            skip = self.driver.find_element(By.ID, 'protect.budgetwatch:id/skip')
            skip.click()
        else: 
            print("Skip button is not visible")
        
        # clicar em budget
        self.driver.implicitly_wait(5)
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
            
            self.driver.implicitly_wait(5) # waits 5 seconds
            name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/budgetNameEdit')
            name.set_text('Lucas')
            self.driver.implicitly_wait(5)
            value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
            value.set_text('1000')
            self.driver.implicitly_wait(5)
            save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
            save.click()
            saved=True
        else:
            print("Budget page was not opened")
        
        if saved == True:
            self.driver.implicitly_wait(10) # waits 5 seconds
            self.assertEqual('Lucas', self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Lucas')]").get_attribute('text'))

####################### CASE2: TRY SAVE BUDGET WITHOUT FILL REQUIRED FIELDS (NAME/VALUE EMPTY) ############################################################# 

    def test_app_budget_add_value_empty(self):
        if self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Welcome to Budget Watch')]"):
            skip = self.driver.find_element(By.ID, 'protect.budgetwatch:id/skip')
            skip.click()

        # clicar em budget
        self.driver.implicitly_wait(5) # waits 5 seconds
        budget = self.driver.find_element(By.XPATH,"//android.widget.TextView[contains(@text, 'Budgets')]")
        budget.click()

        self.driver.implicitly_wait(5)
        add = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_add')
        add.click()

        self.driver.implicitly_wait(5)
        name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/budgetNameEdit')
        name.set_text("error")

        #value field empty
    
        self.driver.implicitly_wait(5)
        save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
        save.click()
       
        self.driver.implicitly_wait(5)
        self.assertEqual('Budget value is empty',self.driver.find_element(By.ID, 'protect.budgetwatch:id/snackbar_text').get_attribute('text'))


    def test_app_budget_add_name_empty(self):
        if self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Welcome to Budget Watch')]"):
            skip = self.driver.find_element(By.ID, 'protect.budgetwatch:id/skip')
            skip.click()

        # clicar em budget
        self.driver.implicitly_wait(5) # waits 5 seconds
        budget = self.driver.find_element(By.XPATH,"//android.widget.TextView[contains(@text, 'Budgets')]")
        budget.click()

        self.driver.implicitly_wait(5)
        add = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_add')
        add.click()

        self.driver.implicitly_wait(5)
        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
        value.set_text("100")

        #name field empty

        self.driver.implicitly_wait(5)
        save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
        save.click()
        
        self.driver.implicitly_wait(5)
        self.assertEqual('Budget type is empty',self.driver.find_element(By.ID, 'protect.budgetwatch:id/snackbar_text').get_attribute('text'))


###################### CASE3: TRY SAVE BUDGET WITH INVALID DATA (LETTER IN VALUE, NUMBER IN NAME, 11 CHARACTERS IN VALUE) #################################

    def test_insert_letter_in_value(self):
        if self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Welcome to Budget Watch')]"):
            skip = self.driver.find_element(By.ID, 'protect.budgetwatch:id/skip')
            skip.click()

        # clicar em budget
        self.driver.implicitly_wait(5) # waits 5 seconds
        budget = self.driver.find_element(By.XPATH,"//android.widget.TextView[contains(@text, 'Budgets')]")
        budget.click()

        self.driver.implicitly_wait(5)
        add = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_add')
        add.click()

        self.driver.implicitly_wait(5)
        name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/budgetNameEdit')
        name.set_text('lucas')

        self.driver.implicitly_wait(5)
        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
        value.set_text("abc")

        self.driver.implicitly_wait(5)
        save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
        save.click()
        
        self.driver.implicitly_wait(5)
        self.assertEqual('Budget value is empty',self.driver.find_element(By.ID, 'protect.budgetwatch:id/snackbar_text').get_attribute('text'))
        

    def test_insert_number_in_name(self):
        if self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Welcome to Budget Watch')]"):
            skip = self.driver.find_element(By.ID, 'protect.budgetwatch:id/skip')
            skip.click()

        # clicar em budget
        self.driver.implicitly_wait(5) # waits 5 seconds
        budget = self.driver.find_element(By.XPATH,"//android.widget.TextView[contains(@text, 'Budgets')]")
        budget.click()

        self.driver.implicitly_wait(5)
        add = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_add')
        add.click()

        self.driver.implicitly_wait(5)
        name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/budgetNameEdit')
        name.set_value(100)

        self.driver.implicitly_wait(5)
        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
        value.set_text("100")

        self.driver.implicitly_wait(5)
        save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
        save.click()
        
        self.driver.implicitly_wait(5)
        self.assertEqual('Budget type is empty',self.driver.find_element(By.ID, 'protect.budgetwatch:id/snackbar_text').get_attribute('text'))


    def test_insert_11_characters_in_value(self):
        if self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Welcome to Budget Watch')]"):
            skip = self.driver.find_element(By.ID, 'protect.budgetwatch:id/skip')
            skip.click()

        # clicar em budget
        self.driver.implicitly_wait(5) # waits 5 seconds
        budget = self.driver.find_element(By.XPATH,"//android.widget.TextView[contains(@text, 'Budgets')]")
        budget.click()

        self.driver.implicitly_wait(5)
        add = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_add')
        add.click()

        self.driver.implicitly_wait(5)
        name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/budgetNameEdit')
        name.set_text('lucas')

        self.driver.implicitly_wait(5)
        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
        value.set_text("12345678910") #11 characters

        self.driver.implicitly_wait(5)
        save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
        save.click()
        
        self.driver.implicitly_wait(10)
        self.assertEqual('Budget value is empty',self.driver.find_element(By.ID, 'protect.budgetwatch:id/snackbar_text').get_attribute('text'))
       
###################### CASE4: MAX LIMIT VALUE AND NAME ###################################################################################################

    def test_max_limit_name(self):
        if self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Welcome to Budget Watch')]"):
            skip = self.driver.find_element(By.ID, 'protect.budgetwatch:id/skip')
            skip.click()

        # clicar em budget
        self.driver.implicitly_wait(5) # waits 5 seconds
        budget = self.driver.find_element(By.XPATH,"//android.widget.TextView[contains(@text, 'Budgets')]")
        budget.click()

        self.driver.implicitly_wait(5)
        add = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_add')
        add.click()

        self.driver.implicitly_wait(5)
        name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/budgetNameEdit')
        name.set_text("qwertyuiopasdfghjklçzxcvbnmqwet") #31 characters

        self.driver.implicitly_wait(5)
        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
        value.set_text("100")

        self.driver.implicitly_wait(5)
        save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
        save.click()
        
        self.driver.implicitly_wait(10)
        # Should not allow insert more than 30 characters
        self.assertFalse("qwertyuiopasdfghjklçzxcvbnmqwet",self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'qwertyuiopasdfghjklçzxcvbnmqwet')]").get_attribute('text'))

    def test_max_limit_value(self):
        if self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Welcome to Budget Watch')]"):
            skip = self.driver.find_element(By.ID, 'protect.budgetwatch:id/skip')
            skip.click()

        # clicar em budget
        self.driver.implicitly_wait(5) # waits 5 seconds
        budget = self.driver.find_element(By.XPATH,"//android.widget.TextView[contains(@text, 'Budgets')]")
        budget.click()

        self.driver.implicitly_wait(5)
        add = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_add')
        add.click()

        self.driver.implicitly_wait(5)
        name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/budgetNameEdit')
        name.set_text("test_max_value") 

        self.driver.implicitly_wait(5)
        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
        value.set_text("1234567891") #10 caracteres

        self.driver.implicitly_wait(5)
        save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
        save.click()
        
        self.driver.implicitly_wait(10)
        # Should allow insert until 10 characters
        self.assertEqual("0/1234567891",self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, '0/1234567891')]").get_attribute('text'))

###################### CASE5: MIN LIMIT VALUE AND NAME ###################################################################################################

    def test_min_limit_name(self):
        if self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Welcome to Budget Watch')]"):
            skip = self.driver.find_element(By.ID, 'protect.budgetwatch:id/skip')
            skip.click()

        # clicar em budget
        self.driver.implicitly_wait(5) # waits 5 seconds
        budget = self.driver.find_element(By.XPATH,"//android.widget.TextView[contains(@text, 'Budgets')]")
        budget.click()

        self.driver.implicitly_wait(5)
        add = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_add')
        add.click()

        self.driver.implicitly_wait(5)
        name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/budgetNameEdit')
        name.set_text("aqwertyuiopasdfghjklçzxcvbnmq") #29 characters

        self.driver.implicitly_wait(5)
        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
        value.set_text("100")

        self.driver.implicitly_wait(5)
        save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
        save.click()
        
        self.driver.implicitly_wait(10)
        self.assertEqual("aqwertyuiopasdfghjklçzxcvbnmq",self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'aqwertyuiopasdfghjklçzxcvbnmq')]").get_attribute('text'))


    def test_min_limit_value(self):
        if self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Welcome to Budget Watch')]"):
            skip = self.driver.find_element(By.ID, 'protect.budgetwatch:id/skip')
            skip.click()

        # clicar em budget
        self.driver.implicitly_wait(5) # waits 5 seconds
        budget = self.driver.find_element(By.XPATH,"//android.widget.TextView[contains(@text, 'Budgets')]")
        budget.click()

        self.driver.implicitly_wait(5)
        add = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_add')
        add.click()

        self.driver.implicitly_wait(5)
        name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/budgetNameEdit')
        name.set_text("test_min_value") 

        self.driver.implicitly_wait(5)
        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
        value.set_text("123456789") #9 characters

        self.driver.implicitly_wait(5)
        save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
        save.click()
        
        self.driver.implicitly_wait(10)
        self.assertEqual("0/123456789",self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, '0/123456789')]").get_attribute('text'))



    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidBudget)
    unittest.TextTestRunner(verbosity=2).run(suite)
