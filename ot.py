#0 0 4 4 0 4 4 0
def get_k(x1, y1, x2, y2):
    if x1 == x2:
        return None
    return (y2-y1)/(x2-x1)


def on_segment(x, y, x1, y1, x2, y2):
    return min(x1,x2)-1e-9 <= x <= max(x1,x2)+1e-9 and min(y1,y2)-1e-9 <= y <= max(y1,y2)+1e-9


def segments(x1, y1, x2, y2, x3, y3, x4, y4):
    # две не совпадающие точки
    if x1 == x2 and y1 == y2 and x3 == x4 and y3 == y4 and x1 != x3 and y1 != y3:
        return "NO"
    # две совпадающие точки
    if x1 == x2 == x3 == x4 == y1 == y2 == y3 == y4:
        return f'{x1}, {y1}'

    k1 = get_k(x1, y1, x2, y2)
    k2 = get_k(x3, y3, x4, y4)
    # вертикальные
    # вертикальный/нормальный
    if k1 is None and not(k2 is None):
        b = y3 - k2 * x3
        y = k2 * x1 + b
        if on_segment(x1, y, x3, y3, x4, y4):
            return f'{float(x1)}, {y}'
    # нормальный/вертикальный
    if k2 is None and not(k1 is None):
        b = y1 - k1 * x1
        y = k1 * x1 + b
        if on_segment(x3, y, x1, y1, x2, y2):
            return f'{float(x3)}, {y}'

    # вертикальный/вертикальный
    if k1 is None and k2 is None:
        if x1 != x3:
            return "NO"
        else:
            overlap_y1 = max(min(y1, y2), min(y3, y4))
            overlap_y2 = min(max(y1, y2), max(y3, y4))
            if overlap_y1 <= overlap_y2:
                return f'отрезок , {x1} {overlap_y1} {x1} {overlap_y2}'


    # точка отрезок
    if x1 == x2 and y1 == y2 and x3 != x4 and y3 != y4:
        b2 = y3 - k2 * x3
        y = k2 * x1 + b2
        if on_segment(x1, y, x3, y3, x4, y4):
            return f'{x1}, {y}'

    if x3 == x4 and y3 == y4 and x1 != x2 and y1 != y2:
        b = y1 - k1 * x1
        y = k1 * x3 + b
        if on_segment(x1, y, x1, y1, x2, y2):
            return f'{x3}, {y}'


    # два нормальных отрезка
    if k1 is not None and k2 is not None:

        b1 = y1 - k1*x1
        b2 = y3 - k2*x3

        if k1 == k2 and b1 != b2:
            return "NO"
        if k1 == k2 and b1 == b2:
            x_start = max(min(x1, x2) , min(x3, x4))
            x_end = min(max(x1, x2) , max(x3, x4))
            if x_start > x_end:
                return 'NO'
            y_start = k1 * x_start + b1
            y_end = k1 * x_end + b1
            if x_start != x_end:
                return f'отрезок , {float(x_start)} {y_start} {float(x_end)} {y_end}'
            if x_start == x_end:
                return f'{float(x_start)}, {y_start}'
        if k1 != k2:
            x_per = (b2 - b1) / (k1 - k2)
            y_per = k1 * x_per + b1
            if on_segment(x_per, y_per, x1, y1, x2, y2) and on_segment(x_per, y_per, x3, y3, x4, y4):
                return f'{x_per}, {y_per}'

            else:
                return "NO"
    return "NO"


#x1, y1, x2, y2, x3, y3, x4, y4 = map(float, input().split())

#print(segments(x1, y1, x2, y2, x3, y3, x4, y4))



# Формат: (x1,y1,x2,y2, x3,y3,x4,y4, ожидаемый результат)

tests = [
    # 1. Пересечение под углом
    (0,0,4,4, 0,4,4,0, "2.0, 2.0"),
    # 2. Параллельные, не пересекаются
    (0,0,4,0, 5,0,8,0, "NO"),
    # 3. Совпадающие частично (горизонтальные)
    (0,0,4,0, 2,0,6,0, "отрезок , 2 0 4 0"),
    # 4. Совпадающие частично (вертикальные)
    (2,1,2,5, 2,3,2,7, "отрезок , 2 3 2 5"),
    # 5. Пересечение вертикального и горизонтального
    (2,1,2,5, 0,3,4,3, "2.0, 3.0"),
    # 6. Пересечение на границе (конец отрезка)
    (0,0,4,4, 4,4,6,6, "4.0, 4.0"),
    # 7. Вертикальный отрезок пересекает горизонтальный в точке
    (3,1,3,5, 0,3,6,3, "3.0, 3.0"),
    # 8. Один из отрезков — точка, лежит на другом
    (1,1,1,1, 0,0,2,2, "1.0, 1.0"),
    # 9. Один из отрезков — точка, не лежит на другом
    (5,5,5,5, 0,0,2,2, "NO"),
    # 10. Оба отрезка — одна и та же точка
    (2,2,2,2, 2,2,2,2, "2, 2"),
    # 11. Оба вертикальные, не пересекаются
    (1,1,1,3, 2,1,2,4, "NO"),
    # 12. Оба горизонтальные, не пересекаются
    (0,0,4,0, 0,1,4,1, "NO"),
]

# Цикл для проверки
for i, (x1,y1,x2,y2,x3,y3,x4,y4, expected) in enumerate(tests, 1):
    result = segments(x1,y1,x2,y2,x3,y3,x4,y4)
    status = "PASS" if str(result) == expected else "FAIL"
    print(f"Test {i}: {status} | Expected: {expected} | Got: {result}")



