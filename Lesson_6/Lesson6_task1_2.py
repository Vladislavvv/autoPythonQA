from selenium import webdriver
from selenium.webdriver.common.by import By

# Настройка драйвера (в данном случае используется Chrome)
driver = webdriver.Chrome()

try:
    # Переход на страницу
    driver.get("http://uitestingplayground.com/textinput")

    # Поиск поля ввода и ввод текста "SkyPro"
    input_field = driver.find_element(By.ID, 'newButtonName')
    input_field.send_keys("SkyPro")

    # Нажатие на синюю кнопку
    blue_button = driver.find_element(By.ID, 'updatingButton')
    blue_button.click()

    # Получение текста кнопки после изменения
    button_text = blue_button.text
    print(button_text)

finally:
    # Закрытие драйвера
    driver.quit()