from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DataTypesPage:
    URL = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def fill_form(self, form_data):
        for name, value in form_data.items():
            try:
                print(f"Пытаемся найти поле с name: {name}")
                input_element = WebDriverWait(self.driver, 15).until(
                    EC.presence_of_element_located((By.NAME, name))
                )
                print(f"Заполняем поле {name} значением {value}")
                input_element.send_keys(value)
            except Exception as e:
                print(f"Ошибка при попытке заполнить поле {name}: {e}")

    def submit_form(self):
        try:
            submit_button = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Submit']"))
            )
            print("Нажимаем кнопку Submit")
            submit_button.click()
        except Exception as e:
            print(f"Ошибка при попытке нажать кнопку Submit: {e}")

    def get_border_color(self, field_id):
        try:
            input_element = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.ID, field_id))
            )
            # Получение атрибута цвета рамки
            border_color = input_element.value_of_css_property('border-color')
            print(f"Цвет рамки для поля {field_id}: {border_color}")

            return self.get_color_value_from_rgb(border_color)
        except Exception as e:
            print(f"Ошибка при получении цвета рамки для поля с id '{field_id}': {e}")
            return None

    @staticmethod
    def get_color_value_from_rgb(rgb):
        rgb = rgb.replace('rgb(', '').replace(')', '')
        rgb = [int(x) for x in rgb.split(',')]
        return "#{:02x}{:02x}{:02x}".format(*rgb)