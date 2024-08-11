from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def run_test(browser_name):
    if browser_name == 'chrome':
        driver = webdriver.Chrome()
    elif browser_name == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise ValueError("Unsupported browser!")

    try:
        driver.get('http://the-internet.herokuapp.com/entry_ad')

        # Ждем появления кнопки 'Close' в модальном окне
        close_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//p[text()='Close']"))
        )
        close_button.click()

        sleep(2)  # Добавляем паузу для наглядности

    except Exception as ex:
        print(f"Exception occurred: {ex}")
    finally:
        driver.quit()

# Запускаем скрипт один раз для каждого браузера
print("Running test for Chrome")
run_test('chrome')
sleep(2)  # Пауза между запусками

print("Running test for Firefox")
run_test('firefox')
sleep(2)  # Пауза между запусками