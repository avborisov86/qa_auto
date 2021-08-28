from selenium.webdriver.common.by import By
from homework5.page_objects.BasePage import BasePage
from random import randint


class AdminCatalogProductsPage(BasePage):
    # Элемент - кнопка открытия категории "Каталог"
    CATALOG_BTN = (By.CSS_SELECTOR, 'a[href*="#collapse1"]')
    # Элемент - кнопка открытия категории "Продукты"
    PRODUCTS_BTN = (By.CSS_SELECTOR, 'a[href*="product&user"]')
    # Элемент - ряд с любым продуктом
    PRODUCT_ROW = (By.CSS_SELECTOR, 'tr')
    # Элемент - чек-бокс для отметки всех товаров одновременно
    MARK_BOX = (By.CSS_SELECTOR, 'thead > tr > td:nth-child(1) > input[type=checkbox]')
    # Элемент - заголовок после удаления всех продуктов
    NO_RESULTS_ELEM = (By.CSS_SELECTOR, 'tbody > tr > td')
    # Элемент - кнопка "Удалить"
    DELETE_BTN = (By.CSS_SELECTOR, '.btn-danger')
    # Элемент - кнопка "Добавить новый"
    ADD_NEW_BTN = (By.CSS_SELECTOR, 'a[href*="add&user"]')
    # Элемент - поле ввода "Название продукта"
    PROD_NAME_INP = (By.CSS_SELECTOR, '#input-name1')
    # Элемент - поле ввода "Meta Tag Title"
    META_TAG_TITLE_INP = (By.CSS_SELECTOR, '#input-meta-title1')
    # Элемент - таб Data
    DATA_TAB = (By.CSS_SELECTOR, 'a[href*="#tab-data"]')
    # Элемент - поле ввода "Model'
    MODEL_INP = (By.CSS_SELECTOR, '#input-model')
    # Элемент - кнопка "Сохранить"
    SAVE_BTN = (By.CSS_SELECTOR, 'button[type=submit]')

    def push_catalog_link(self):
        self.move_and_click(self.CATALOG_BTN)

    def push_products_link(self):
        self.move_and_click(self.PRODUCTS_BTN)

    def enter_catalog_products(self):
        self.move_and_click(self.CATALOG_BTN)
        self.move_and_click(self.PRODUCTS_BTN)

    def mark_random_product(self):
        random_product = randint(0, self.get_quantity(self.PRODUCT_ROW))
        self.move_and_click(
            (By.CSS_SELECTOR, f'tbody > tr:nth-child({random_product}) > td:nth-child(1) > input[type=checkbox]'))

    def mark_all_products_by_one(self):
        quantity = self.get_quantity(self.PRODUCT_ROW)
        for i in range(1, quantity):
            self.move_and_click(
                (By.CSS_SELECTOR, f'tbody > tr:nth-child({i}) > td:nth-child(1) > input[type=checkbox]'))

    def mark_all_products_together(self):
        self.move_and_click(self.MARK_BOX)

    def push_delete_btn(self):
        self.move_and_click(self.DELETE_BTN)

    def push_add_new_btn(self):
        self.move_and_click(self.ADD_NEW_BTN)
