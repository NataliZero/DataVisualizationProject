from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import matplotlib.pyplot as plt
import time
import csv

# Инициализация Selenium WebDriver
print("Инициализация драйвера...")
driver = webdriver.Firefox()
url = 'https://www.divan.ru/category/divany'
print("Открытие страницы...")
driver.get(url)

# Ждем загрузки страницы
print("Ожидание 5 секунд...")
time.sleep(5)

# Парсинг цен
print("Начало парсинга цен...")
prices = driver.find_elements(By.CLASS_NAME, "price__main-value")
print(f"Найдено {len(prices)} цен.")

# Сохранение данных в CSV
print("Сохранение данных в CSV...")
with open('sofa_prices.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Price'])  # Заголовок столбца
    for price in prices:
        writer.writerow([price.text])
print("Парсинг завершен. Данные сохранены в sofa_prices.csv")

# Закрытие драйвера
driver.quit()

# Чтение данных из CSV
print("Чтение данных из CSV файла...")
data = pd.read_csv('sofa_prices.csv')
print(data.head())

# Обработка данных: удаление нечисловых символов и преобразование в числовой тип
print("Обработка данных...")
data['Price'] = data['Price'].str.replace('₽', '').str.replace(' ', '').astype(int)

# Подсчет средней цены
mean_price = data['Price'].mean()
print(f"Средняя цена на диваны: {mean_price:.2f} ₽")

# Построение гистограммы
print("Построение гистограммы цен...")
plt.hist(data['Price'], bins=10, edgecolor='black')
plt.title("Гистограмма цен на диваны")
plt.xlabel("Цена (₽)")
plt.ylabel("Частота")
plt.show()
