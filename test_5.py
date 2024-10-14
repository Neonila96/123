import time
import pytest
from start_page import StartPage
from cart_page import CartPage


@pytest.mark.usefixtures("init_driver", "base_url")
class TestAddToCart:
    def test_add_multiple_products_to_cart(self, base_url):
        # Инициализация страниц
        start_page = StartPage(self.driver)
        cart_page = CartPage(self.driver)

        # Открытие стартовой страницы
        start_page.open_start_page()

        # ID продуктов, которые хотим добавить в корзину
        product_ids = ['253354771', '253354942', '253355137']

        for product_id in product_ids:
            # Добавление продукта в корзину
            start_page.add_product_to_cart(product_id)
            assert start_page.is_product_added_to_cart(), f"Product {product_id} was not added to cart"
        time.sleep(5)
        # Кликаем по корзине
        start_page.clic_to_icon_cart()
        time.sleep(5)
        # Проверка, что все продукты отображаются в корзине
        for product_id in product_ids:
            assert cart_page.find_element(cart_page.cart_item_locator(product_id)), (f"Product {product_id} is not "
                                                                                     f"displayed in the cart")
