import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_sauce_demo_checkout():
    # Инициализация веб-драйвера
    driver = webdriver.Chrome()
    
    try:
        # Открытие страницы магазина
        driver.get("https://www.saucedemo.com/")
        
        # Авторизация
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        
        # Добавление товаров в корзину
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
        
        # Переход в корзину
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        
        # Нажатие Checkout
        driver.find_element(By.ID, "checkout").click()
        
        # Заполнение формы
        driver.find_element(By.ID, "first-name").send_keys("Имя")
        driver.find_element(By.ID, "last-name").send_keys("Фамилия")
        driver.find_element(By.ID, "postal-code").send_keys("123456")
        driver.find_element(By.ID, "continue").click()
        
        # Ожидание и чтение итоговой стоимости
        total = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label"))
        ).text
        
        # Проверка итоговой суммы
        assert total == "Total: $58.29"
    
    finally:
        # Закрытие веб-драйвера
        driver.quit()