from selenium.webdriver.common.by import By
from base_page import BasePage


class StartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Локатор для поиска товара по data-product-id
    def product_form_locator(self, product_id):
        return By.XPATH, f'//form[@data-product-id="{product_id}"]'

    # Локатор для кнопки "В корзину" внутри формы продукта
    def add_to_cart_button_locator(self, product_id):
        return (
            By.XPATH, f'//form[@data-product-id="{product_id}"]//button[contains(@class, "product-preview__buy-btn")]')

    # Локатор для проверки успешного добавления в корзину (пример, может отличаться)
    def cart_success_locator(self):
        return By.XPATH, '//div[contains(@class, "micro-alert-item")]'

    # Локатор для иконки корзины справа наверху (добавила я)
    def cart_icon_locator(self):
        return By.XPATH, '//*[@class="icon icon-cart"]'

    # Метод для клика по иконке коризны справа наверху
    def clic_to_icon_cart(self):
        # Найти иконку коризины
        icon_cart = self.find_element(self.cart_icon_locator())

        # Кликнуть по иконке
        self.click(self.cart_icon_locator())

    # Метод для добавления продукта в корзину
    def add_product_to_cart(self, product_id):
        # Найти форму продукта
        product_form = self.find_element(self.product_form_locator(product_id))

        # Навести на кнопку "В корзину"
        self.hover(self.add_to_cart_button_locator(product_id))

        # Кликнуть по кнопке "В корзину"
        self.click(self.add_to_cart_button_locator(product_id))

    # Метод для проверки, что товар добавлен в корзину
    def is_product_added_to_cart(self):
        return self.find_element(self.cart_success_locator())

    # Метод для открытия главной страницы (или другой нужной страницы)
    def open_start_page(self):
        self.open_page()




