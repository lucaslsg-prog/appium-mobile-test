from appium.webdriver.common.appiumby import By
from BasePage import BasePage

class AddExpensesPage(BasePage):

    name_expense_locator = (By.ID,'protect.budgetwatch:id/nameEdit')
    budget_selector_locator = (By.ID,'protect.budgetwatch:id/budgetSpinner')
    account_locator = (By.ID,'protect.budgetwatch:id/accountEdit')
    value_locator = (By.ID,'protect.budgetwatch:id/valueEdit')
    note_locator = (By.ID,'protect.budgetwatch:id/noteEdit')
    date_locator =(By.ID,'protect.budgetwatch:id/dateEdit')
    receipt_locator = (By.ID,'protect.budgetwatch:id/captureButton')
    save_button_locator = (By.ID,'protect.budgetwatch:id/action_save')
    budget_list_locator = (By.ID, 'protect.budgetwatch:id/text')
    select_date_locator = (By.XPATH,"//android.widget.TextView[contains(@text, '8')]")
    ok_date_locator = (By.ID, 'android:id/button1')


    def type_name(self,text):
        name_expense = self.driver.find_element(*AddExpensesPage.name_expense_locator)
        name_expense.send_keys(text)

    def budget_selector_click(self):
        budget_selector = self.driver.find_element(*AddExpensesPage.budget_selector_locator)
        budget_selector.click()

    def budget_list_select(self):
        budget_list = self.driver.find_elements(*AddExpensesPage.budget_list_locator)
        budget_list[0].click()

    def type_account(self,text):
        account_name = self.driver.find_element(*AddExpensesPage.account_locator)
        account_name.send_keys(text)

    def type_value(self, text):
        value = self.driver.find_element(*AddExpensesPage.value_locator)
        value.send_keys(text)

    def type_note(self, text):
        note = self.driver.find_element(*AddExpensesPage.note_locator)
        note.send_keys(text)

    def date_click(self):
        date = self.driver.find_element(*AddExpensesPage.date_locator)
        #select_date = self.driver.find_element(*AddExpensesPage.select_date_locator)
        date.click()
        self.driver.implicitly_wait(30)
        ok_date = self.driver.find_element(*AddExpensesPage.ok_date_locator)
        #select_date.click()
        ok_date.click()

    def receipt_click(self):
        receipt = self.driver.find_element(*AddExpensesPage.receipt_locator)
        receipt.click()

    def click_save_button(self):
        save_button = self.driver.find_element(*AddExpensesPage.save_button_locator)
        save_button.click()








