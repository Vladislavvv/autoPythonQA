import pytest
from selenium import webdriver
from page_object3 import LoginPage, InventoryPage, CartPage, CheckoutPage, OverviewPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_sauce_demo_checkout(driver):
    # Переход на страницу и авторизация
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # Добавление товаров в корзину
    inventory_page = InventoryPage(driver)
    inventory_page.add_to_cart("add-to-cart-sauce-labs-backpack")
    inventory_page.add_to_cart("add-to-cart-sauce-labs-bolt-t-shirt")
    inventory_page.add_to_cart("add-to-cart-sauce-labs-onesie")
    inventory_page.go_to_cart()

    # Переход к оформлению заказа
    cart_page = CartPage(driver)
    cart_page.checkout()

    # Заполнение формы
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_information("Имя", "Фамилия", "123456")

    # Получение итоговой стоимости
    overview_page = OverviewPage(driver)
    total = overview_page.get_total()

    # Проверка итоговой суммы
    assert total == "Total: $58.29", f"Expected total to be 'Total: $58.29', but got {total}"