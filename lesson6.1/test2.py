import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_slow_calculator():
    # Инициализация веб-драйвера
    driver = webdriver.Chrome()
    
    try:
        # Открытие страницы калькулятора
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        
        # Ввод значения задержки 45 секунд
        delay_input = driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys("45")
        
        # Нажатие кнопок 7, +, 8, =
        driver.find_element(By.XPATH, "//span[text()='7']").click()
        driver.find_element(By.XPATH, "//span[text()='+']").click()
        driver.find_element(By.XPATH, "//span[text()='8']").click()
        driver.find_element(By.XPATH, "//span[text()='=']").click()
        
        # Ожидание результата в течение 45 секунд
        time.sleep(45)
        
        # Проверка, что результат равен 15
        result = driver.find_element(By.CLASS_NAME, "screen").text
        assert result == "15"
    
    finally:
        # Закрытие веб-драйвера
        driver.quit()