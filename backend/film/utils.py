from datetime import datetime

from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import requests
from bs4 import BeautifulSoup
from film.models import Film
from database import async_session_maker
from config import settings
# service = Service('path/to/chromedriver')  # Укажите путь к chromedriver


async def parse_films():
    options = Options()
    options.add_argument('--headless')  # Запуск в фоновом режиме
    service = Service('chromedriver.exe')  # Укажите путь к chromedriver
    driver = webdriver.Chrome()

    # driver.get('https://www.kinopoisk.ru/lists/movies/100_greatest_movies_XXI/')
    driver.get('https://www.imdb.com/chart/top/?ref_=nv_mv_100')
    print(11111111111111)
    films = []
    items = driver.find_elements(By.CSS_SELECTOR, '.ipc-metadata-list--base')
    print(f'count films {len(items)}')

    for item in items:
        # Получаем ссылку на страницу фильма
        film_link = item.find_element(By.TAG_NAME, 'a').get_attribute('href')
        driver.get(film_link)  # Переходим на страницу фильма

        try:
            name = driver.find_element(By.CSS_SELECTOR, '.hero__primary-text').text  # Название фильма
            print(name)
            # image_url = driver.find_element(By.CSS_SELECTOR, 'div.poster img').get_attribute('src')  # URL постера
            # producer = driver.find_element(By.CSS_SELECTOR, '.ipc-metadata-list-item__label').text  # Продюсер
            # year = driver.find_element(By.CSS_SELECTOR, '.ipc-link--baseAlt').text  # Год
            # genre = driver.find_element(By.CSS_SELECTOR, '.ipc-chip').text  # Жанр
            # rating = float(driver.find_element(By.CSS_SELECTOR, '.sc-d541859f-1').text)  # Рейтинг

            # Сохраняем изображение в папку static
            image_path = f'static/{name.replace(" ", "_")}.jpg'  # Формируем путь к изображению
            # response = requests.get(image_url)
            # if response.status_code == 200:
            #     with open(image_path, 'wb') as f:
            #         f.write(response.content)

            # name = item.find_element(By.CSS_SELECTOR, '.ipc-title__text').text
            # year_element = item.find_element(By.CSS_SELECTOR, '.cli-title-metadata-item')  # Убедитесь, что селектор правильный
            # year_str = year_element.text.strip()  # Получаем текст и убираем лишние пробелы
            # # Преобразуем строку в целое число
            # year = int(year_str)  # Сохраняем год как целое число
            # rating = float(item.find_element(By.CSS_SELECTOR, '.ipc-rating-star--rating').text)

            film = Film(name=name,
                        # image_path=image_path, producer=producer, year=year, genre=genre, rating=rating
                        )
            films.append(film)
        except StaleElementReferenceException:
            print(f"Ошибка при извлечении данных для фильма:")

        driver.back()
        items = driver.find_elements(By.CSS_SELECTOR, '.ipc-metadata-list-summary-item')

    async with async_session_maker() as session:
        session.add_all(films)
        await session.commit()

    driver.quit()
