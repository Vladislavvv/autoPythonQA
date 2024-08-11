import pytest
from selenium import webdriver

# Импортируем класс страницы
from page_object2 import SlowCalculatorPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_slow_calculator(driver):
    # Переход на страницу
    page = SlowCalculatorPage(driver)
    page.open()

    # Ввод значения задержки 45 секунд
    page.set_delay("45")

    # Нажатие кнопок 7, +, 8, =
    page.click_button("7")
    page.click_button("+")
    page.click_button("8")
    page.click_button("=")

    # Ожидание результата в течение 45 секунд
    page.wait_for_result(45)

    # Проверка, что результат равен 15
    result = page.get_result()
    assert result == "15", f"Expected result to be 15, but got {result}"

if __name__ == "__main__":
    pytest.main()