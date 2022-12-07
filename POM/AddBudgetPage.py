from appium.webdriver.common.appiumby import By
from BasePage import BasePage


class AddBudgetPage(BasePage):
    budget_type_locator = (By.ID, 'protect.budgetwatch:id/budgetNameEdit')
    budget_value_locator = (By.ID, 'protect.budgetwatch:id/valueEdit')
    save_button_locator = (By.ID, 'protect.budgetwatch:id/action_save')
    msg_error_locator = (By.ID, 'protect.budgetwatch:id/snackbar_text')

    def type_budget_type(self, text):
        budget_type = self.driver.find_element(*AddBudgetPage.budget_type_locator)
        budget_type.send_keys(text)

    def type_budget_value(self, text):
        budget_value = self.driver.find_element(*AddBudgetPage.budget_value_locator)
        budget_value.send_keys(text)

    def click_save_button(self):
        save_button = self.driver.find_element(*AddBudgetPage.save_button_locator)
        save_button.click()

    def get_error(self):
        msg_error = self.driver.find_element(*AddBudgetPage.msg_error_locator)
        return msg_error.text

    def is_budget_type_enabled(self):
        budget_type = self.driver.find_element(*AddBudgetPage.budget_type_locator)
        return budget_type.is_enabled()


