import pytest
from selenium import webdriver

# Импортируем класс страницы
from page_object import DataTypesPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_form_submission(driver):
    # Переход на страницу
    page = DataTypesPage(driver)
    page.open()

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
    page.fill_form(form_data)

    # Нажатие на кнопку Submit
    page.submit_form()

    # Проверка цвета рамки для поля Zip code
    zip_code_color = page.get_border_color('zip-code')
    assert zip_code_color == '#f5c2c7', f"Zip code field should be red, but it is {zip_code_color}"

    # Проверка цвета рамки для остальных полей
    field_ids = ['first-name', 'last-name', 'address', 'e-mail', 'phone', 'city', 'country', 'job-position', 'company']
    for field_id in field_ids:
        border_color = page.get_border_color(field_id)
        assert border_color == '#badbcc', f"Field {field_id} should be green, but it is {border_color}"

if __name__ == "__main__":
    pytest.main()