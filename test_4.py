import time
import pytest
from selenium.webdriver.common.by import By

from start_page import StartPage
from cart_page import CartPage


@pytest.mark.usefixtures("init_driver", "base_url")
class TestProductPrice:
    def test_product_price_displayed_correctly_in_cart(self, base_url):
        # Инициализация страниц
        start_page = StartPage(self.driver)
        cart_page = CartPage(self.driver)

        # Открытие стартовой страницы
        start_page.open_start_page()

        # ID продукта
        product_id = '253354771'

        # Добавление продукта в корзину
        start_page.add_product_to_cart(product_id)
        assert start_page.is_product_added_to_cart(), "Product was not added to cart"
        time.sleep(5)

        # Кликаем по корзине
        start_page.clic_to_icon_cart()
        time.sleep(5)

        # Получаем локатор для товара
        item_locator = cart_page.cart_item_locator(product_id)

        # Теперь используем локатор для поиска цены
        price_locator = (By.XPATH, f'{item_locator[1]}//span[contains(@class, "price")]')
        price_element = cart_page.find_element(price_locator)

        assert price_element.is_displayed(), "Price element is not displayed"
        # Проверяем цену без " руб"
        assert price_element.text.replace(" руб",
                                          "") == "10.00", f"Expected price to be '10.00', but got '{price_element.text}'"
