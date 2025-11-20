import math
import random

# ====== ДАННЫЕ (20 наблюдений) ======
y = [
    30.8, 31.2, 33.2, 35.6, 36.7,
    39.2, 40.3, 40.4, 40.3, 41.8,
    40.4, 41.8, 40.4, 40.7, 42.7,
    44.1, 46.7, 50.6, 50.1, 52.9
]

x1 = [
    459.7, 492.9, 528.6, 560.0, 666.4,
    772.6, 843.3, 911.6, 843.3, 911.6,
    931.1, 1021.5, 1165.9, 1349.6, 1449.4,
    1575.5, 1759.1, 1994.2, 2258.1, 2478.7
]

x2 = [
    39.0, 37.3, 38.1, 39.3, 37.6,
    38.4, 38.2, 38.6, 39.8, 39.7,
    52.1, 48.9, 58.3, 57.9, 56.5,
    63.7, 61.6, 58.9, 66.4, 70.4
]

x3 = [
    55.3, 54.7, 63.7, 69.8, 65.9,
    64.5, 73.2, 73.2, 67.8, 79.1,
    95.4, 94.2, 123.5, 129.9, 117.6,
    130.9, 129.8, 128.0, 141.0, 168.2
]


# ====== ЛОГ-ПРЕОБРАЗОВАНИЕ ======
ln_y  = [math.log(v) for v in y]
ln_x1 = [math.log(v) for v in x1]
ln_x2 = [math.log(v) for v in x2]
ln_x3 = [math.log(v) for v in x3]

# ====== Монте-Карло ======
N = 30000
best_sse = float("inf")
best_params = None

def sse(A, B1, B2, B3):
    """SSE в лог-масштабе"""
    total = 0.0
    for i in range(len(y)):
        pred = A + B1*ln_x1[i] + B2*ln_x2[i] + B3*ln_x3[i]
        total += (ln_y[i] - pred) ** 2
    return total

for _ in range(N):
    A  = random.uniform(-10, 10)
    B1 = random.uniform(-5, 5)
    B2 = random.uniform(-5, 5)
    B3 = random.uniform(-5, 5)

    current_sse = sse(A, B1, B2, B3)

    if current_sse < best_sse:
        best_sse = current_sse
        best_params = (A, B1, B2, B3)

A, B1, B2, B3 = best_params
beta0 = math.exp(A)

# ====== ПРЕДСКАЗАНИЯ ПО ИКСАМ ======
pred_y = []
for i in range(len(y)):
    pred_ln = A + B1*ln_x1[i] + B2*ln_x2[i] + B3*ln_x3[i]
    pred_y.append(math.exp(pred_ln))


# ====== ВЫВОД ======
print("=== Найденная модель ===")
print(f"y = {beta0:.5f} * x1^{B1:.5f} * x2^{B2:.5f} * x3^{B3:.5f}")
print()
print("=== Предсказанные значения y ===")
print(pred_y)
