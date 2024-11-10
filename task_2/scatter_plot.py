import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
x = np.random.rand(50)  # Набор случайных чисел для оси X
y = np.random.rand(50)  # Набор случайных чисел для оси Y

# Построение диаграммы рассеяния
plt.scatter(x, y)
plt.title("Диаграмма рассеяния для двух наборов случайных данных")
plt.xlabel("Значения X")
plt.ylabel("Значения Y")
plt.show()
