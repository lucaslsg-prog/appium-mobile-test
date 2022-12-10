from appium.webdriver.common.appiumby import By
from BasePage import BasePage

class AddRegisterPages(BasePage):
    input_price_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/etPrice')
    input_title_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/etTitle')
    input_category_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/etCategory')
    save_register_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/fabDone')
    get_msg_error = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/textinput_error')
    date_element_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/tvDate')
    button_ok = (By.ID, 'android:id/button1')
    button_cancel = (By.ID, 'android:id/button2')

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