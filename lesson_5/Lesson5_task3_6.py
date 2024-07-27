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
        driver.get('http://the-internet.herokuapp.com/login')

        # Находим поле ввода для username и вводим значение
        username_field = driver.find_element(By.ID, 'username')
        username_field.send_keys('tomsmith')
        sleep(1)  # Пауза для наглядности

        # Находим поле ввода для password и вводим значение
        password_field = driver.find_element(By.ID, 'password')
        password_field.send_keys('SuperSecretPassword!')
        sleep(1)  # Пауза для наглядности

        # Находим кнопку Login и нажимаем на нее
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()
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