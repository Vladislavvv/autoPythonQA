from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

class LoginPage(BasePage):
    def open(self):
        self.driver.get("https://www.saucedemo.com/")
    
    def login(self, username, password):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

class InventoryPage(BasePage):
    def add_to_cart(self, item_id):
        self.driver.find_element(By.ID, item_id).click()

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

class CartPage(BasePage):
    def checkout(self):
        self.driver.find_element(By.ID, "checkout").click()

class CheckoutPage(BasePage):
    def fill_information(self, first_name, last_name, postal_code):
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()

class OverviewPage(BasePage):
    def get_total(self):
        total = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label"))
        ).text
        return total