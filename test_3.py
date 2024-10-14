import time
import pytest
from start_page import StartPage
from cart_page import CartPage



@pytest.mark.usefixtures("init_driver", "base_url")
class TestNavigate:
    def test_navigate_back_to_start_page(self, base_url):
        # Инициализация страниц
        start_page = StartPage(self.driver)
        cart_page = CartPage(self.driver)

        # Открытие стартовой страницы
        start_page.open_start_page()

        # Кликаем по корзине
        start_page.clic_to_icon_cart()

        # Проверка, что находимся на странице корзины
        assert "cart_items" in self.driver.current_url, "Not on cart page"

        # Переход обратно на главную страницу
        start_page.open_start_page()

        # Проверка, что вернулись на главную страницу
        assert "yookassa" in self.driver.current_url, "Not on start page"