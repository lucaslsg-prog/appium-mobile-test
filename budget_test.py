import unittest, time, os
from builtins import id

#import self as self
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
        desired_caps['deviceName'] = 'RX8NB0E61AH'
        desired_caps['appPackage'] = 'protect.budgetwatch'
        desired_caps['appActivity'] = '.MainActivity'
        self.driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)

    def test_app_budget_add(self):

        if self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Welcome to Budget Watch')]"):
            skip = self.driver.find_element(By.ID, 'protect.budgetwatch:id/skip')
            skip.click()

        # clicar em budget
        budget = self.driver.find_element(By.XPATH,
                                          "//android.widget.TextView[contains(@text, 'Budgets')]")
        budget.click()

        add = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_add')
        add.click()

        name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/budgetNameEdit')
        name.set_text("energia")

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
        value.set_text("500")

        save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
        save.click()

        self.assertEqual("energia", self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'energia')]").get_attribute('text'))

    def test_app_budget_add_error(self):
        if self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Welcome to Budget Watch')]"):
            skip = self.driver.find_element(By.ID, 'protect.budgetwatch:id/skip')
            skip.click()

        # clicar em budget
        budget = self.driver.find_element(By.ID, 'protect.budgetwatch:id/image')
        budget.click()

        add = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_add')
        add.click()

        name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/budgetNameEdit')
        name.set_text("test123")

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
        value.set_text("abcdefg")

        save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
        save.click()

        self.assertEqual('Budget value is empty',
                         self.driver.find_element(By.ID, 'protect.budgetwatch:id/snackbar_text').get_attribute('text'))

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidBudget)
    unittest.TextTestRunner(verbosity=2).run(suite)
