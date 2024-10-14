from selenium.webdriver.common.by import By
from base_page import BasePage


class ConfirmPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Локатор для кнопки оформить заказ"
    def button_confirm_locator(self):
        return By.XPATH, f'//button[@id="create_order"]'

    # Локатор для ввода контактного телефона"
    def input_for_phone_locator(self):
        return By.XPATH, f'//input[@id="client_phone"]'

    # Локатор для ввода населенного пункта"
    def input_for_city_locator(self):
        return By.XPATH, f'//input[@id="shipping_address_full_locality_name"]'

    # Локатор для водда контактного лица"
    def input_for_contact_locator(self):
        return By.XPATH, f'//input[@id="client_name"]'

    # Локатор для чекбокса курьер"
    def chekbox_courier_locator(self):
        return By.XPATH, f'//*[@id="delivery_variants"]/div[2]/label[2]/span[1]'

    # Локатор для чекбокса сбер"

    def chekbox_sberpay_locator(self):
        return By.XPATH, f'//*[@id="payment_gateways"]/div/label[2]/span[1]'

        # Локатор для поля адреса
    def input_for_address_locator(self):
            return By.XPATH, f'//input[@id="shipping_address_full_locality_name"]'

        # Метод для получения текста из поля адреса
    def get_address_value(self):
            return self.find_element(self.input_for_address_locator()).get_attribute('value')

     # Локатор для кнопки оформить заказ"
    def button_confirm_locator(self):
        return By.XPATH, f'//button[@id="create_order"]'

    # Локатор для ввода контактного телефона"
    def input_for_phone_locator(self):
        return By.XPATH, f'//input[@id="client_phone"]'

    # Локатор для ввода населенного пункта"
    def input_for_city_locator(self):
        return By.XPATH, f'//input[@id="shipping_address_full_locality_name"]'

    # Локатор для водда контактного лица"
    def input_for_contact_locator(self):
        return By.XPATH, f'//input[@id="client_name"]'

    # Локатор для чекбокса курьер"
    def chekbox_courier_locator(self):
        return By.XPATH, f'//label[@for="order_delivery_variant_id_7870784"]//span[@class="radio co-delivery_method-input co-toggable_field-input co-toggable_field-input--radio"]'

    # Локатор для чекбокса сбер"
    def chekbox_sberpay_locator(self):
        return By.XPATH, f'//label[@for="order_payment_gateway_id_2646307"]//span[@class="co-payment_method-input co-toggable_field-input  co-toggable_field-input--radio"]'

    # # Локаторы для сообщения "поле не заполнено"
    # def error_message_locator1(self):
    #     return By.XPATH, f'//*[@id="delivery_address"]/div[2]/div[1]/div'

    def error_message_locator2(self):
        return By.XPATH, f'//*[@id="tabs-person"]/div[1]/div'

    # Локатор для поля адреса
    def input_for_address_locator(self):
        return By.XPATH, f'//input[@id="shipping_address_full_locality_name"]'

    # Метод для проверки видимости сообщения "поле не заполнено"
    def is_text_error(self):
        error_message = self.find_element(self.error_message_locator2())
        text = error_message.text
        return text

    #Метод для заполнения ФИО
    def enter_fio(self):
        self.send_keys(self.input_for_contact_locator(), "Иванов Иван")


    #Метод для клика по "оформить заказ"
    def clic_to_button_confirm(self):
        self.find_element(self.button_confirm_locator())
        self.click(self.button_confirm_locator())

    # Метод для получения текста из поля адреса
    def get_address_value(self):
        return self.find_element(self.input_for_address_locator()).get_attribute('value')