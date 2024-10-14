import time
import pytest
from start_page import StartPage
from cart_page import CartPage
from confirm_page import ConfirmPage
@pytest.mark.usefixtures("init_driver", "base_url")
class TestRemoveItem:

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
        #Проверка, что форма заказа не видна при удалении товаров из корзины
        assert cart_page.form_order_locator().is_displayed() == False , "Форма заказа видна"

@pytest.mark.usefixtures("init_driver", "base_url")
class TestInvalidPromo:

    def test_add_product_to_cart(self, base_url):
        # Инициализация страницы
        start_page = StartPage(self.driver)
        cart_page = CartPage(self.driver)

        # Открытие стартовой страницы
        start_page.open_start_page()

        # ID продукта, который хотим добавить в корзину
        product_id = '253354942'

        # Добавление продукта в корзину
        start_page.add_product_to_cart(product_id)

        # Проверка, что товар добавлен в корзину
        assert start_page.is_product_added_to_cart(), "Product was not added to cart"
        time.sleep(5)
        # Кликаем по корзине справа наверху
        start_page.clic_to_icon_cart()

        #Вводим промокод
        cart_page.input_promo()

        #Кликаем применить промокод
        cart_page.clic_to_button_promo()

        # Проверка, что появилось сообщение "Указан несущ купон"
        assert cart_page.text_promo().count('Указан несуществующий купон, убедитесь, что он введен верно') == 1

@pytest.mark.usefixtures("init_driver", "base_url")
class TestInvalidClient:

    def test_add_product_to_cart(self, base_url):
        # Инициализация страницы
        start_page = StartPage(self.driver)
        cart_page = CartPage(self.driver)
        confirm_page = ConfirmPage(self.driver)

        # Открытие стартовой страницы
        start_page.open_start_page()

        # ID продукта, который хотим добавить в корзину
        product_id = '253354771'

        # Добавление продукта в корзину
        start_page.add_product_to_cart(product_id)
        time.sleep(3)
        # Кликаем по корзине справа наверху
        start_page.clic_to_icon_cart()

        # Кликаем по "оформить заказ"
        cart_page.clic_to_button_confirm()
        time.sleep(5)

        #Оставляем все поля пустыми и кликаем "Оформить заказ"
        confirm_page.clic_to_button_confirm()
        time.sleep(3)

        # проверяем, что появляется сообщение "Поле не заполнено"
        assert confirm_page.is_text_error().count("Поле не заполнено") == 1
        time.sleep(2)
