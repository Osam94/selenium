from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Настройка опций для Chrome
options = Options()
options.add_argument('start-maximized')  # Открыть браузер в максимальном размере

# Инициализация веб-драйвера
driver = webdriver.Chrome(options=options)

try:
    # Переход на сайт Perekrestok
    driver.get("https://www.perekrestok.ru/")

    # Ввод названия продукта через стандартный ввод 
    product_name = input("Введите название продукта: ")

    # Поиск по каталогу 
    search_input = driver.find_element(By.XPATH, "//input[@placeholder='Поиск по каталогу']")
    search_input.send_keys(product_name)
    search_input.send_keys(Keys.ENTER)

    # Ожидание загрузки результатов
    time.sleep(5)  # Можно использовать WebDriverWait для более надежного ожидания

    # Извлечение названий продуктов и их цен 
    prods = driver.find_elements(By.XPATH, "//div[@class='product-card__title']")
    prices = driver.find_elements(By.XPATH, "//div[@class='product-card__price']")

    # Создание списка для хранения информации о товарах 
    products = []

    # Печать названий продуктов и их цен
    for card, price in zip(prods, prices):
        products.append(f"{card.text}: {price.text}")

    # Вывод списка продуктов и цен
    for product in products:
        print(product)

finally:
    # Закрытие браузера 
    driver.quit()

