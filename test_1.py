import time
import pytest
from start_page import StartPage
from cart_page import CartPage
from selenium import webdriver

# Путь к локальному драйверу
chrome_driver_path = ./Drivers/chromedriver.exe  # или chromedriver.exe для Windows

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=options)


@pytest.mark.usefixtures("init_driver", "base_url")
class TestAddToCart:

    def test_add_product_to_cart(self, base_url):
        # Инициализация страницы
        start_page = StartPage(self.driver)
        cart_page = CartPage(self.driver)

        # Открытие стартовой страницы
        start_page.open_start_page()

        # ID продукта, который хотим добавить в корзину
        product_id = '253354771'

        # Добавление продукта в корзину
        start_page.add_product_to_cart(product_id)

        # Проверка, что товар добавлен в корзину
        assert start_page.is_product_added_to_cart(), "Product was not added to cart"
        time.sleep(5)
        # Кликаем по корзине справа наверху
        start_page.clic_to_icon_cart()
        time.sleep(5)

        # Кликаем по удалить
        cart_page.clic_to_icon_trash(product_id)
        time.sleep(5)
