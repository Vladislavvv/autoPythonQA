from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Настройка драйвера (в данном случае используется Chrome)
driver = webdriver.Chrome()

try:
    # Переход на страницу
    driver.get("http://uitestingplayground.com/ajax")

    # Нажатие на синюю кнопку
    blue_button = driver.find_element(By.CSS_SELECTOR, 'button.btn-primary')
    blue_button.click()

    # Ожидание появления текста в зеленой плашке
    green_plate = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#content > p'))
    )

    # Получение текста
    loaded_text = green_plate.text
    print(loaded_text)

except TimeoutException:
    print("Элемент не найден на странице в течение заданного времени ожидания.")

finally:
    # Закрытие драйвера
    driver.quit()