import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Преобразование rgb цвета в hex
def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(*rgb)

def get_color_value_from_rgb(rgb):
    """Функция для получения значения цвета из rgb."""
    rgb = rgb.replace('rgb(', '').replace(')', '')
    rgb = [int(x) for x in rgb.split(',')]
    return rgb_to_hex(tuple(rgb))

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_form_submission(driver):
    # Переход на страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Заполнение формы
    form_data = {
        'first-name': 'Иван',
        'last-name': 'Петров',
        'address': 'Ленина, 55-3',
        'e-mail': 'test@skypro.com',
        'phone': '+7985899998787',
        'city': 'Москва',
        'country': 'Россия',
        'job-position': 'QA',
        'company': 'SkyPro'
    }

    for name, value in form_data.items():
        try:
            print(f"Пытаемся найти поле с name: {name}")
            input_element = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.NAME, name))
            )
            print(f"Заполняем поле {name} значением {value}")
            input_element.send_keys(value)
        except Exception as e:
            print(f"Ошибка при попытке заполнить поле {name}: {e}")

    # Нажимаем кнопку Submit
    try:
        submit_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Submit']"))
        )
        print("Нажимаем кнопку Submit")
        submit_button.click()
    except Exception as e:
        print(f"Ошибка при попытке нажать кнопку Submit: {e}")

    # Функция для получения цвета рамки
    def get_border_color(field_id):
        try:
            input_element = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.ID, field_id))
            )
            # Получение атрибута цвета рамки
            border_color = input_element.value_of_css_property('border-color')
            print(f"Цвет рамки для поля {field_id}: {border_color}")

            return get_color_value_from_rgb(border_color)
        except Exception as e:
            print(f"Ошибка при получении цвета рамки для поля с id '{field_id}': {e}")
            return None

    # Проверка цвета рамки для поля Zip code
    zip_code_color = get_border_color('zip-code')
    assert zip_code_color == '#f5c2c7', f"Zip code field should be red, but it is {zip_code_color}"

    # Проверка цвета рамки для остальных полей
    field_ids = ['first-name', 'last-name', 'address', 'e-mail', 'phone', 'city', 'country', 'job-position', 'company']
    for field_id in field_ids:
        border_color = get_border_color(field_id)
        assert border_color == '#badbcc', f"Field {field_id} should be green, but it is {border_color}"

if __name__ == "__main__":
    pytest.main()