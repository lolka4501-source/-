# lab7.py
# Лабораторная работа №7
# Используется только numpy и matplotlib

import numpy as np
import matplotlib.pyplot as plt

# ========== ЗАДАНИЕ 1 ==========
# 10 точек, построить:
# 1) точки; 2) линию; 3) замкнутую кривую
x = np.random.rand(10)
y = np.random.rand(10)

plt.figure(figsize=(12,4))

# 1) только точки
plt.subplot(1,3,1)
plt.scatter(x, y, color='blue', label='Точки')
plt.title('Только точки')
plt.xlabel('x'); plt.ylabel('y')
plt.legend(); plt.grid(True)

# 2) линейный график
plt.subplot(1,3,2)
plt.plot(x, y, marker='o', color='green', label='Линия')
plt.title('Линейный график')
plt.xlabel('x'); plt.ylabel('y')
plt.legend(); plt.grid(True)

# 3) замкнутая кривая (соединяем последнюю с первой)
x_closed = np.append(x, x[0])
y_closed = np.append(y, y[0])
plt.subplot(1,3,3)
plt.plot(x_closed, y_closed, marker='o', color='red', label='Замкнутая кривая')
plt.title('Замкнутая кривая')
plt.xlabel('x'); plt.ylabel('y')
plt.legend(); plt.grid(True)

plt.tight_layout()
plt.show()


# ========== ЗАДАНИЕ 2 ==========
# Фигуры Лиссажу
t = np.linspace(0, 2*np.pi, 1000)

# первая
x1 = np.sin(3 * t + np.pi/2)
y1 = np.sin(2 * t)

# вторая
x2 = np.sin(5 * t)
y2 = np.sin(4 * t + np.pi/3)

plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.plot(x1, y1, color='purple')
plt.title('Лиссажу 1 (a=3, b=2)')
plt.xlabel('x'); plt.ylabel('y'); plt.grid(True)

plt.subplot(1,2,2)
plt.plot(x2, y2, color='orange')
plt.title('Лиссажу 2 (a=5, b=4)')
plt.xlabel('x'); plt.ylabel('y'); plt.grid(True)

plt.tight_layout()
plt.show()


# ========== ЗАДАНИЕ 3 ==========
# Построить на одной плоскости две полиномные кривые
x = np.linspace(-3, 3, 200)
y1 = 5*x**3 + 2*x**2 - 7*x + 10
y2 = 3*x**2

plt.figure(figsize=(6,4))
plt.plot(x, y1, label='y = 5x³ + 2x² - 7x + 10')
plt.plot(x, y2, label='y = 3x²', linestyle='--')
plt.title('Две полиномные кривые')
plt.xlabel('x'); plt.ylabel('y')
plt.legend(); plt.grid(True)
plt.show()


# ========== ЗАДАНИЕ 4 ==========
# Стаж и зарплата
np.random.seed(0)
experience = np.random.randint(1, 11, 30)   # стаж 1–10 лет
salary = np.random.randint(30, 120, 30)     # зарплата 30–120 тыс

# Гистограмма
plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.hist(experience, bins=[1,3,7,10], color='skyblue', edgecolor='black', rwidth=0.9)
plt.title('Гистограмма стажа')
plt.xlabel('Стаж (лет)'); plt.ylabel('Количество сотрудников'); plt.grid(axis='y')

# Диаграмма рассеяния
plt.subplot(1,2,2)
plt.scatter(experience, salary, color='green', label='Сотрудники')
plt.title('Стаж vs Зарплата')
plt.xlabel('Стаж (лет)'); plt.ylabel('Зарплата (тыс)')
plt.legend(); plt.grid(True)

plt.tight_layout()
plt.show()


# ========== ЗАДАНИЕ 5 ==========
# Тор в 3D
from mpl_toolkits.mplot3d import Axes3D

R = 2  # большой радиус
r = 0.7  # малый радиус

u = np.linspace(0, 2*np.pi, 60)
v = np.linspace(0, 2*np.pi, 30)
U, V = np.meshgrid(u, v)

X = (R + r*np.cos(V)) * np.cos(U)
Y = (R + r*np.cos(V)) * np.sin(U)
Z = r * np.sin(V)

fig = plt.figure(figsize=(7,6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, color='coral', alpha=0.9)
ax.set_title('Тор в 3D')
ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
plt.show()
