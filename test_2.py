import time
import pytest
from start_page import StartPage
from cart_page import CartPage
from confirm_page import ConfirmPage


@pytest.mark.usefixtures("init_driver", "base_url")
class TestAddToCart:
    def test_add_product_to_cart(self, base_url):
        # Инициализация страниц
        start_page = StartPage(self.driver)
        cart_page = CartPage(self.driver)
        confirm_page = ConfirmPage(self.driver)

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

        # Переход к оформлению заказа
        cart_page.clic_to_button_confirm()
        time.sleep(5)

        # Заполнение формы заказа
        confirm_page.find_element(confirm_page.input_for_contact_locator()).send_keys("Иван Иванов")
        confirm_page.find_element(confirm_page.input_for_phone_locator()).send_keys("+71234567890")
        confirm_page.find_element(confirm_page.input_for_city_locator()).send_keys("Москва")

        # Выбор курьерской доставки
        confirm_page.click(confirm_page.chekbox_courier_locator())

        # Выбор способа оплаты
        confirm_page.click(confirm_page.chekbox_sberpay_locator())

        # Оформление заказа
        confirm_page.click(confirm_page.button_confirm_locator())

        # Проверка, что введенный адрес валиден
        entered_address = confirm_page.get_address_value()
        assert entered_address == "Москва", f"Expected address 'Москва', but got '{entered_address}'"
