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

############# CASE1: SAVE OPERATION SUCCESS ##################################################################

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

####################### CASE2: SAVE OPERATION ERROR (NAME EMPTY) ##################################################################### 

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
        self.assertEqual('Budget value is empty',self.driver.find_element(By.ID, 'protect.budgetwatch:id/snackbar_text').get_attribute('text'))


############################# CASE3: INVALID NAME (NUMBER IN NAME) #########################################################

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
        name.set_value(12)

        self.driver.implicitly_wait(5)
        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
        value.set_text("100")

        self.driver.implicitly_wait(5)
        save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
        save.click()
        
        self.driver.implicitly_wait(5)
        #not should allow number
        self.assertNotEqual(12,self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, '12')]").get_attribute('text'))
############################# CASE4: MAX LIMIT VALUE AND NAME ######################################################

    def max_limit_name(self):
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
        name.set_text("qwertyuiopasdfghjklçzxcvbnmqwet") #32 caracteres

        self.driver.implicitly_wait(5)
        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
        value.set_text("100")

        self.driver.implicitly_wait(5)
        save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
        save.click()
        
        self.driver.implicitly_wait(5)
        self.assertFalse("qwertyuiopasdfghjklçzxcvbnmqwet",self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'qwertyuiopasdfghjklçzxcvbnmqwet')]").get_attribute('text'))

    def min_limit_name(self):
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
        name.set_text("aqwertyuiopasdfghjklçzxcvbnmq") #29 caracteres

        self.driver.implicitly_wait(5)
        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
        value.set_text("100")

        self.driver.implicitly_wait(5)
        save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
        save.click()
        
        self.driver.implicitly_wait(5)
        self.assertEqual("aqwertyuiopasdfghjklçzxcvbnmq",self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'aqwertyuiopasdfghjklçzxcvbnmq')]").get_attribute('text'))


############################# CASE5: MIN LIMIT VALUE AND NAME ######################################################

    def max_limit_value(self):
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
        value.set_text("12345678910111") #14 caracteres

        self.driver.implicitly_wait(5)
        save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
        save.click()
        
        self.driver.implicitly_wait(5)
        self.assertFalse("12345678910111",self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, '12345678910111')]").get_attribute('text'))


    def min_limit_value(self):
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
        value.set_text("123456789101") #12 caracteres

        self.driver.implicitly_wait(5)
        save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
        save.click()
        
        self.driver.implicitly_wait(5)
        self.assertFalse("123456789101",self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, '123456789101')]").get_attribute('text'))



    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidBudget)
    unittest.TextTestRunner(verbosity=2).run(suite)
