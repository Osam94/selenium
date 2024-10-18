from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

try:
    driver.get("https://www.imdb.com/chart/top")

    movie_title_element=driver.find_elements(By.CSS_SELECTOR,"div.sc-ab348ad5-0 a h3")
    rating_elements=driver.find_elements(By.CSS_SELECTOR,"div.sc-e2dbc1a3-0  span.ipc-rating-star--rating")

    
    titles = [element.text for element in movie_title_element]
    ratings = [element.text for element in rating_elements]

    print("Найдено названий фильмов:", len(titles))
    print("Найдено рейтингов:", len(ratings))

    if len(titles) > 0 and len(ratings) > 0:
        for i in range(min(len(titles), len(ratings), 10)):  # Ограничиваем до 10
            print("Рейтинг {}: {} ({})".format(i + 1, titles[i], ratings[i]))
    else:
        print("Не удалось найти названия фильмов или рейтинги.")

finally:
    driver.quit()




