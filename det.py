import numpy as np

def determinant(matrix: np.ndarray):
    n = matrix.shape[0]
    if n == 1:
        return matrix[0, 0]
    if n == 2:
        return matrix[0, 0]*matrix[1, 1] - matrix[0, 1]*matrix[1, 0]

    det = 0.0
    for j in range(n):
        minor = np.delete(np.delete(matrix, 0, axis=0), j, axis=1)
        cofactor = ((-1) ** j) * matrix[0, j] * determinant(minor)
        det += cofactor

    return det



print("Определитель квадратной матрицы")
print("1 — Ввести матрицу вручную")
print("2 — Сгенерировать случайную матрицу")

cond = input()

if cond == "1":
    n = int(input("Введите размерность матрицы n: "))
    print(f"Введите элементы матрицы {n}×{n}:")
    matrix = np.zeros((n, n), dtype=float)
    for i in range(n):
        row = list(map(float, input(f"Строка {i+1}: ").split()))
        matrix[i] = row

elif cond == "2":
    n = int(input("Введите размерность матрицы n: "))
    matrix = np.random.uniform(-10, 10, (n, n)).astype(float)
    print("Сгенерированная матрица:")
    print(matrix)

else:
    print("Некорректный выбор.")


det = determinant(matrix)
print(f"\nОпределитель = {det:.6f}")

