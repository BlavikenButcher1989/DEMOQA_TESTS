from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as W
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open_site(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator):
        return W(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator):
        return W(self.driver, 10).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator):
        return W(self.driver, 10).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator):
        return W(self.driver, 10).until(EC.presence_of_all_elements_located(locator))

    def element_is_clickable(self, locator):
        return W(self.driver, 10).until(EC.element_to_be_clickable(locator))

    def action_double_click(self, element):
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    def action_right_click(self, element):
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()

    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def switch_to_frame(self, locator):
        self.driver.switch_to.frame(locator)

    def slide_drag_and_drop(self, element, x_coord, y_coord):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, x_coord, y_coord)
        action.perform()

    def action_move_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    def drag_and_drop_elements(self, drag, drop):
        action = ActionChains(self.driver)
        action.drag_and_drop(drag, drop)
        action.perform()


