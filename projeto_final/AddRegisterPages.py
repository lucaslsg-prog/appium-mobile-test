from appium.webdriver.common.appiumby import By
from BasePage import BasePage
from appium.webdriver.common.touch_action import TouchAction

class AddRegisterPages(BasePage):
    input_price_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/etPrice')
    input_title_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/etTitle')
    input_category_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/etCategory')
    save_register_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/fabDone')
    get_msg_error = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/textinput_error')
    date_element_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/tvDate')
    month_view_locator = (By.ID,'android:id/month_view')
    previous_month_locator = (By.ID, 'android:id/prev')
    next_month_locator = (By.ID, 'android:id/next')
    first_day_locator = (By.XPATH, "//android.view.View[contains(@text,'1')]")
    button_ok = (By.ID, 'android:id/button1')
    button_cancel = (By.ID, 'android:id/button2')
    delete_icon = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/action_delete')
    current_date = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/tvDate')
    selected_date = (By.ID, 'android:id/date_picker_header_date')

    def insert_price(self, text):
        price = self.driver.find_element(*AddRegisterPages.input_price_locator)
        price.send_keys(text)

    def insert_title(self, text):
        title = self.driver.find_element(*AddRegisterPages.input_title_locator)
        title.send_keys(text)

    def insert_category(self, text):
        category = self.driver.find_element(*AddRegisterPages.input_category_locator)
        category.send_keys(text)
    
    def save_new_register(self):
        save = self.driver.find_element(*AddRegisterPages.save_register_locator)
        save.click()
        
    def get_error(self):
        msg_error = self.driver.find_element(*AddRegisterPages.get_msg_error)
        return msg_error.text

    def open_calendar(self):
        calendar = self.driver.find_element(*AddRegisterPages.date_element_locator)
        calendar.click()
    
    def goTo_previous_month(self):
        prev_month = self.driver.find_element(*AddRegisterPages.previous_month_locator)
        res = False
        if prev_month:
            prev_month.click()
            res = True
        return res

    def goTo_next_month(self):
        next_month = self.driver.find_element(*AddRegisterPages.next_month_locator)
        res = False
        if next_month:
            next_month.click()
            res = True
        return res

    def click_on_day(self,day):
        day = self.driver.find_element(By.XPATH, f"//android.view.View[contains(@text,'{day}')]")
        day.click()
    
    def get_current_date(self):
        date = self.driver.find_element(*AddRegisterPages.current_date).get_attribute('text')
        current_day = date.split('-')[2]
        return current_day

    def get_selected_date(self):
        register_date = self.driver.find_element(*AddRegisterPages.selected_date).get_attribute('text')
        selected_day = register_date.split(' ')[2]
        return selected_day

    def click_on_btn_ok(self):
        btn_ok = self.driver.find_element(*AddRegisterPages.button_ok)
        btn_ok.click()

    def click_on_delete_icon(self):
        del_icon = self.driver.find_element(*AddRegisterPages.delete_icon)
        del_icon.click()