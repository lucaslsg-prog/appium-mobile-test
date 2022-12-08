from appium.webdriver.common.appiumby import By
from BasePage import BasePage


class TransactionsPage(BasePage):
    add_transaction_locator = (By.ID, 'protect.budgetwatch:id/action_add')

    def add_transaction_click(self):
        add_transaction = self.driver.find_element(*TransactionsPage.add_transaction_locator)
        add_transaction.click()
