from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Настройка драйвера (в данном случае используется Chrome)
driver = webdriver.Chrome()

try:
    # Переход на страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    # Ожидание загрузки всех картинок или текста "Done"
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'Done')]"))
    )

    # Получение третьего изображения по его индексу
    images = driver.find_elements(By.TAG_NAME, 'img')
    third_image_src = images[2].get_attribute('src')

    # Вывод значения атрибута src в консоль
    print(third_image_src)

finally:
    # Закрытие драйвера
    driver.quit()