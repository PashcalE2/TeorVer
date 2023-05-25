import matplotlib.pyplot as plt
import math


def M(data=[], p=[]):
    return sum([data[i] * p[i] for i in range(len(data))])


def D(data=[], p=[]):
    return M([i ** 2 for i in data], p) - M(data, p) ** 2


def practise_5(data=[]):
    n = len(data)
    sorted_data = sorted(data)
    no_dups_data = sorted(list(set(data)))

    min_val = sorted_data[0]
    max_val = sorted_data[-1]
    print(f"Минимальное значение = {min_val}\nМаксимальное значение = {max_val}\nРазмах = {max_val - min_val}")

    count = [0 for i in range(len(no_dups_data))]

    for i in range(len(no_dups_data)):
        for j in sorted_data:
            if no_dups_data[i] == j:
                count[i] += 1

    possibilities = [i / sum(count) for i in count]
    F = [0]
    for i in range(len(possibilities)):
        F.append(possibilities[i] + F[i])

    print(f"Вариационный ряд: {no_dups_data}")

    Data_M = M(no_dups_data, possibilities)
    Data_D = D(no_dups_data, possibilities)
    Data_D_Corrected = n / (n - 1) * Data_D
    Data_Sko = Data_D ** 0.5
    Data_Sko_Corrected = (n / (n - 1) * Data_D) ** 0.5

    print(f"M(X) = {Data_M}\nD(X) = {Data_D}\nИсправленная D(X) = {Data_D_Corrected}\nСКО = {Data_Sko}\nИсправленное СКО = {Data_Sko_Corrected}")

    # F
    m = math.ceil(1 + math.log(n, 2))
    h = (max_val - min_val) / (m - 1)
    print(f"Количество интервалов = {m}, шаг = {h}")
    interval_points = [min_val + ((i - 0.5) * h) for i in range(m + 1)]

    F_str = "{:5.2f},         x < {:5.2f}\n".format(0, interval_points[0])
    for i in range(len(interval_points) - 1):
        p = 0
        for j in data:
            if interval_points[i] <= j < interval_points[i + 1]:
                p += 1
        F_str += "{:5.2f}, {:5.2f} <= x < {:5.2f}\n".format(p / n, interval_points[i], interval_points[i + 1])
    F_str += "{:5.2f},         x >=  {:5.2f}\n".format(1, interval_points[-1])

    print(f"F(x) = \n{F_str}")

    x_values = interval_points.copy()
    x_values.insert(0, x_values[0] - 0.5)
    x_values.append(x_values[-1] + 0.5)

    y_values = []
    for i in range(len(x_values) - 1):
        y = 0
        for x in data:
            if x_values[i] < x <= x_values[i + 1]:
                y += 1
        y /= n
        if i > 0:
            y += y_values[-1]
        y_values.append(y)

    plt.figure()
    for i in range(len(y_values)):
        plt.plot([x_values[i], x_values[i + 1]], [y_values[i], y_values[i]], color="blue")

    # Poly

    x_values = interval_points.copy()
    y_values = []
    for i in range(m + 1):
        y = 0
        for x in data:
            if x_values[i] < x <= x_values[i + 1]:
                y += 1
        y_values.append(y / n)

    plt.figure()
    plt.plot(x_values, y_values, color="blue", marker="o")

    # Hist

    x_values = interval_points.copy()
    y_values = []
    for i in range(m):
        y = 0
        for x in data:
            if x_values[i] < x <= x_values[i + 1]:
                y += 1
        y_values.append(y)

    plt.figure()
    plt.hist(x_values[:-1], x_values, weights=y_values, color="blue", edgecolor="black")
    plt.show()


numbers = [-0.26, -0.58, 1.49, -0.84, -1.54, 1.13, -1.33, -0.78, -1.68, -0.94,
           -1.55, 1.54, 0.34, 0.58, -0.84, -1.58, -1.72, -0.49, 0.34, -0.14]

practise_5(numbers)
