from appium.webdriver.common.appiumby import By
from BasePage import BasePage

class ViewRecordsPage(BasePage):
    list_title_records_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/tvTitle')
    list_category_records_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/tvCategory')
    list_price_records_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/tvPrice')
    total_income_locator = (By.ID,'com.blogspot.e_kanivets.moneytracker:id/tvTotalIncome')
    button_add_income = (By.ID,'com.blogspot.e_kanivets.moneytracker:id/btnAddIncome')
    button_add_expense = (By.ID,'com.blogspot.e_kanivets.moneytracker:id/btnAddExpense')
    
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