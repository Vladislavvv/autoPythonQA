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
        driver.get('http://uitestingplayground.com/classattr')

        # Кликаем на синюю кнопку
        blue_button = driver.find_element(By.CLASS_NAME, 'btn-primary')
        blue_button.click()

        sleep(2)  # Добавляем паузу для наглядности

    except Exception as ex:
        print(f"Exception occurred: {ex}")
    finally:
        driver.quit()

# Запускаем скрипт три раза подряд для каждого браузера
for i in range(3):
    print(f"Running test iteration {i+1} for Chrome")
    run_test('chrome')
    sleep(2)  # Пауза между запусками

for i in range(3):
    print(f"Running test iteration {i+1} for Firefox")
    run_test('firefox')
    sleep(2)  # Пауза между запусками