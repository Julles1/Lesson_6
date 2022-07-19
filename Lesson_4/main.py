def quadratic_formula(a, b, c):
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    c = int(input("Введите третье число: "))

    discr = b**2 - 4 * a * c
    print("Дискриминант =", int(discr))
    if discr < 0:
        return "Корни отсутствуют"
    elif discr == 0:
        x = -b / (2 * a)
        return int(x)
    else:
        x_1 = (-b + discr ** 0.5) / (2 * a)
        x_2 = (-b - discr ** 0.5) / (2 * a)
        return int(x_1), int(x_2)

print(quadratic_formula(1, -2, 1))
