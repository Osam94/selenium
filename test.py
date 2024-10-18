

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

driver = webdriver.Chrome()
driver.get("https://quotes.toscrape.com/page/1/")

quotes = []

while True:
    quote_elements = driver.find_elements(By.XPATH, "//div[@class='quote']")

    for quote_element in quote_elements:
        quote = quote_element.find_element(By.XPATH, ".//span[@class='text']").text
        author = quote_element.find_element(By.XPATH, ".//small[@class='author']").text
        quotes.append({"quote": quote, "author": author})

    try:
        # Используем явное ожидание для кнопки "Далее"
        next_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//li[@class='next']/a"))
        )
        next_button.click()
        time.sleep(1)  # Задержка для загрузки следующей страницы
    except Exception as e:
        print("No more pages or an error occurred:", e)
        break

# Выводим собранные цитаты
with open("quotes.csv", 'w', newline="", encoding='utf-8') as file:  # Указана кодировка utf-8
    writer = csv.DictWriter(file, fieldnames=["quote", "author"])
    writer.writeheader()
    writer.writerows(quotes)




driver.quit()

