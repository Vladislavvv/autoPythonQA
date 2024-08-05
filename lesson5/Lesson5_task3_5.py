from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def run_test(browser_name):
    if browser_name == 'chrome':
        driver = webdriver.Chrome()
    elif browser_name == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise ValueError("Unsupported browser!")

    try:
        driver.get('http://the-internet.herokuapp.com/inputs')

        # Находим поле ввода
        input_field = driver.find_element(By.TAG_NAME, 'input')

        # Вводим текст 1000
        input_field.send_keys('1000')
        sleep(2)  # Пауза для наглядности

        # Очищаем поле
        input_field.clear()
        sleep(2)  # Пауза для наглядности

        # Вводим текст 999
        input_field.send_keys('999')
        sleep(2)  # Пауза для наглядности

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