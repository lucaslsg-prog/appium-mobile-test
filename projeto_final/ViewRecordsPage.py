from appium.webdriver.common.appiumby import By
from BasePage import BasePage

class ViewRecordsPage(BasePage):
    list_title_records_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/tvTitle')
    list_category_records_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/tvCategory')
    list_price_records_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/tvPrice')
    total_locator = (By.ID,'com.blogspot.e_kanivets.moneytracker:id/tvTotal')
    button_add_income = (By.ID,'com.blogspot.e_kanivets.moneytracker:id/btnAddIncome')
    button_add_expense = (By.ID,'com.blogspot.e_kanivets.moneytracker:id/btnAddExpense')
    week_list_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/spinner')
    
    def open_add_income_page(self):
        income_page_btn = self.driver.find_element(*ViewRecordsPage.button_add_income)
        income_page_btn.click()
    
    def open_add_expense_page(self):
        expense_page_btn = self.driver.find_element(*ViewRecordsPage.button_add_expense)
        expense_page_btn.click()
    
    def get_price(self):
        price = self.driver.find_element(*ViewRecordsPage.list_price_records_locator)
        return price.text

    def get_title(self):
        title = self.driver.find_element(*ViewRecordsPage.list_title_records_locator)
        return title.text

    def get_category(self):
        category = self.driver.find_element(*ViewRecordsPage.list_category_records_locator)
        return category.text

    def open_edit_page(self):
        edit = self.driver.find_element(*ViewRecordsPage.list_title_records_locator)
        edit.click()

    def get_total(self):
        total = self.driver.find_element(*ViewRecordsPage.total_locator)
        return total.text

    def open_week_list(self):
        options = self.driver.find_element(*ViewRecordsPage.week_list_locator)
        options.click()
    
    def get_period_records(self,period):
        select_period = self.driver.find_element(By.XPATH, f"//android.widget.TextView[contains(@text,'{period}')]")
        select_period.click()