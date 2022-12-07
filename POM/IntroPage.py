from appium.webdriver.common.appiumby import By
from BasePage import BasePage


class IntroPage(BasePage):
    skip_locator = (By.ID, 'protect.budgetwatch:id/skip')

    def click_skip(self):
        skip = self.driver.find_element(*IntroPage.skip_locator)
        skip.click()
