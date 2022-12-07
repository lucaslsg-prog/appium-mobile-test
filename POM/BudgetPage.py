from appium.webdriver.common.appiumby import By
from BasePage import BasePage
from appium.webdriver.common.touch_action import TouchAction


class BudgetPage(BasePage):
    add_locator = (By.ID, 'protect.budgetwatch:id/action_add')
    first_budget_locator = (By.XPATH,
                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout/android.widget.TextView')
    new_value_locator = (By.XPATH,
                         '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView')
    edit_locator = (By.ID, 'android:id/title')
    empty_list_locator = (By.ID, 'protect.budgetwatch:id/helpText')
    calendar_locator = (By.ID, "protect.budgetwatch:id/action_calendar")
    setdate_locator = (By.ID, "android:id/button1")
    text_date_locator = (By.ID, "protect.budgetwatch:id/dateRange")

    def click_add(self):
        add_budget = self.driver.find_element(*BudgetPage.add_locator)
        add_budget.click()

    def get_first_budget(self):
        first_element = self.driver.find_element(*BudgetPage.first_budget_locator)
        return first_element.text

    def long_click_first_budget(self):
        first_element = self.driver.find_element(*BudgetPage.first_budget_locator)
        actions = TouchAction(self.driver)
        actions.long_press(first_element)
        actions.perform()

    def get_new_value(self):
        new_value = self.driver.find_element(*BudgetPage.new_value_locator)
        return new_value.text

    def click_edit(self):
        edit = self.driver.find_element(*BudgetPage.edit_locator)
        edit.click()

    def get_emptylist_msg(self):
        empty_list = self.driver.find_element(*BudgetPage.empty_list_locator)
        return empty_list.text

    def get_text_date(self):
        text_date = self.driver.find_element(*BudgetPage.text_date_locator)
        return text_date.text
