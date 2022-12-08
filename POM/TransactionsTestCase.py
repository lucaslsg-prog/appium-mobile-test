import unittest
from datetime import date

from MainPage import MainPage
from BudgetPage import BudgetPage
from AddBudgetPage import AddBudgetPage
from appium import webdriver
from Data import TestData
import time

from AddExpensesPage import AddExpensesPage
from IntroPage import IntroPage
from TransactionsPage import TransactionsPage


class TransactionsTestCase(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'protect.budgetwatch'
        desired_caps['appActivity'] = '.MainActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test_create_new_expense(self):

    # Skip da tela de inicialização
        intro_page = IntroPage(self.driver)
        intro_page.click_skip()
        self.driver.implicitly_wait(30)
    # selecionar o item Budget do menu
        main_page = MainPage(self.driver)
        main_page.click_transactions()
    # Clicar para adicionar Budget
        transaction_page = TransactionsPage(self.driver)
        transaction_page.add_transaction_click()
        add_page = AddExpensesPage(self.driver)
        self.driver.implicitly_wait(30)
    # Inserir os dados de Budget na tela de adicionar
        add_page.type_name("teste")
        #add_page.budget_list_locator
        #add_page.budget_list_select()
        add_page.type_account("teste1")
        add_page.type_value("100")
        add_page.type_note("teste teste teste teste")
        self.driver.hide_keyboard()
        add_page.date_click()
        add_page.click_save_button()
       # budget_page = BudgetPage(self.driver)

    # verificação do resultado
      #  self.assertEqual(budget_page.get_first_budget(), TestData.budget_type)




if __name__ == '__main__':
    unittest.main()
