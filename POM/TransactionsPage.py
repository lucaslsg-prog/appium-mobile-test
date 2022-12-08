from appium.webdriver.common.appiumby import By
from BasePage import BasePage


class TransactionsPage(BasePage):
    add_transaction_locator = (By.ID, 'protect.budgetwatch:id/action_add')
    get_transaction_locator =  (By.XPATH,"//android.widget.TextView[contains(@text, 'Transactions')]")

    def add_transaction_click(self):
        add_transaction = self.driver.find_element(*TransactionsPage.add_transaction_locator)
        add_transaction.click()

    def get_first_expense(self):
        get_transaction = self.driver.find_element(*TransactionsPage.get_transaction_locator)
        get_transaction.click()