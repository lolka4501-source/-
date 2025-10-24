import numpy as np
import math

def eigen_2x2(matrix: np.ndarray):
    a, b = matrix[0, 0], matrix[0, 1]
    c, d = matrix[1, 0], matrix[1, 1]

    # Характеристическое уравнение: |A - λI| = 0
    # λ² - (a + d)λ + (ad - bc) = 0
    trace = a + d
    det = a * d - b * c

    # Дискриминант
    discriminant = trace**2 - 4 * det

    if discriminant < 0:
        print("⚠️ Собственные значения комплексные (эта версия работает только с вещественными).")
        return None

    # Собственные значения
    lambda1 = (trace + math.sqrt(discriminant)) / 2
    lambda2 = (trace - math.sqrt(discriminant)) / 2

    # Собственные векторы
    eigenvectors = []
    for lambd in (lambda1, lambda2):
        # (A - λI)x = 0
        a11 = a - lambd
        a22 = d - lambd

        if abs(b) > 1e-9:
            x2 = 1.0
            x1 = -a11 / b
        elif abs(c) > 1e-9:
            x1 = 1.0
            x2 = -a22 / c
        else:
            # Диагональная матрица
            x1, x2 = 1.0, 0.0

        # Нормируем вектор (чтобы не выглядели громоздко)
        vec = np.array([x1, x2], dtype=float)
        norm = np.sqrt(vec.dot(vec))
        if norm != 0:
            vec = vec / norm
        eigenvectors.append(vec)

    return (lambda1, lambda2), eigenvectors


def main():
    print("Введите элементы матрицы 2×2:")
    data = []
    for i in range(2):
        row = list(map(float, input(f"Строка {i+1}: ").split()))
        if len(row) != 2:
            print("Ошибка: нужно ввести 2 числа в строке.")
            return
        data.append(row)

    matrix = np.array(data, dtype=float)
    result = eigen_2x2(matrix)

    if result is None:
        return

    (λ1, λ2), vectors = result

    print(f"\nСобственные значения:")
    print(f"λ₁ = {λ1:.4f}, λ₂ = {λ2:.4f}")

    print("\nСобственные векторы (нормированные):")
    print(f"v₁ = {vectors[0]}")
    print(f"v₂ = {vectors[1]}")


if __name__ == "__main__":
    main()
