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
    print(sorted_data)

    min_val = sorted_data[0]
    max_val = sorted_data[-1]
    print(f"Минимальное значение = {min_val}\nМаксимальное значение = {max_val}\nРазмах = {max_val - min_val}")

    count = [0 for i in range(len(no_dups_data))]

    for i in range(len(no_dups_data)):
        for j in sorted_data:
            if no_dups_data[i] == j:
                count[i] += 1

    possibilities = [i / sum(count) for i in count]

    print(f"Вариационный ряд: {no_dups_data}")

    Data_M = M(no_dups_data, possibilities)
    Data_D = D(no_dups_data, possibilities)
    Data_D_Corrected = n / (n - 1) * Data_D
    Data_Sko = Data_D ** 0.5
    Data_Sko_Corrected = (n / (n - 1) * Data_D) ** 0.5

    print(
        f"M(X) = {Data_M}\nD(X) = {Data_D}\nИсправленная D(X) = {Data_D_Corrected}\nСКО = {Data_Sko}\nИсправленное СКО = {Data_Sko_Corrected}")

    # F
    # m = math.ceil(1 + math.log(n, 2))
    m = 9
    h = (max_val - min_val) / m
    print(f"Количество интервалов m = {m}, шаг = {h}")
    interval_points = [min_val + (i - 1) * h for i in range(m + 3)]
    print(interval_points)

    F = [0]
    i = 0
    while True:
        p = 0
        for j in data:
            if interval_points[i] <= j < interval_points[i + 1]:
                p += 1
        p = p / n
        if abs(F[-1] + p - 1) > 0.0000001:
            F.append(F[-1] + p)
            i += 1
        else:
            break
    F.append(1)

    # x_values = interval_points.copy()
    x_values = no_dups_data.copy()
    x_values.insert(0, x_values[0] - (max_val - min_val) / 10)
    x_values.append(x_values[-1] + (max_val - min_val) / 10)

    y_values = [0]
    F_str = "{:5.2f},          x < {:5.2f}\n".format(0, x_values[1])
    for i in range(len(possibilities) - 1):
        y_values.append(y_values[-1] + possibilities[i])
        F_str += "{:5.2f}, {:5.2f} <= x < {:5.2f}\n".format(y_values[-1], x_values[i + 1], x_values[i + 2])
    y_values.append(1)
    F_str += "{:5.2f},          x >={:5.2f}\n".format(1, x_values[-2])

    print(f"F(x) = \n{F_str}")

    plt.figure()
    for i in range(len(y_values)):
        plt.plot([x_values[i], x_values[i + 1]], [y_values[i], y_values[i]], color="blue")

    # Poly

    x_values = interval_points[1:-1]
    y_values = []
    for i in range(m):
        y = 0
        for x in data:
            if x_values[i] <= x < x_values[i + 1]:
                y += 1
        y_values.append(y)
    y_values[-1] += sum([1 if t >= x_values[-1] else 0 for t in data])

    plt.figure()
    plt.ylim(0, max(y_values) + 3)
    plt.plot([(x_values[i] + x_values[i + 1]) / 2 for i in range(len(y_values))], y_values, color="blue", marker="o")

    # Hist

    x_values = interval_points[1:-1]
    y_values = []
    for i in range(m):
        y = 0
        for x in data:
            if x_values[i] <= x < x_values[i + 1]:
                y += 1
        y_values.append(y / n)
    y_values[-1] += sum([1 / n if x >= x_values[-1] else 0 for x in data])
    plt.figure()
    plt.hist(x_values[:-1], x_values, weights=y_values, color="blue", edgecolor="black")
    plt.show()


# numbers = [-0.26, -0.58, 1.49, -0.84, -1.54, 1.13, -1.33, -0.78, -1.68, -0.94, -1.55, 1.54, 0.34, 0.58, -0.84, -1.58, -1.72, -0.49, 0.34, -0.14]

home_work_numbers = [81, 106, 135, 170, 206, 60, 181, 178, 154, 103,
                     78, 176, 31, 204, 145, 85, 229, 47, 108, 234,
                     110, 207, 241, 168, 133, 68, 174, 143, 89, 182,
                     203, 153, 172, 93, 48, 228, 255, 134, 112, 58,
                     144, 235, 114, 77, 208, 183, 59, 170, 95, 154,
                     104, 202, 39, 164, 247, 226, 110, 67, 121, 193,
                     123, 91, 164, 57, 209, 30, 185, 162, 250, 225,
                     201, 160, 239, 211, 131, 142, 101, 153, 76, 125,
                     137, 54, 127, 87, 66, 190, 158, 241, 33, 221,
                     100, 195, 156, 146, 231, 220, 129, 83, 151, 56]

# practise_5(home_work_numbers)

x = [210, 220, 230, 240, 250, 260]
y = [1470, 1540, 1610, 1680, 1750, 1820, 1890, 1960]
repeats = [
    [3, 2, 3, 0, 0, 0, 0, 0],
    [0, 1, 4, 5, 0, 0, 0, 0],
    [0, 0, 7, 13, 8, 0, 0, 0],
    [0, 0, 0, 0, 9, 6, 6, 0],
    [0, 0, 0, 0, 0, 7, 8, 3],
    [0, 0, 0, 0, 0, 4, 6, 5],
]

x_values = []
y_values = []

for i in range(6):
    for j in range(8):
        for k in range(repeats[i][j]):
            x_values.append(x[i])
            y_values.append(y[j])

plt.figure()
plt.scatter(x_values, y_values, color="black")

x_values = [x[0] - 20, x[-1] + 20]
y_x = lambda x: 7.532 * x - 29.723
y_values = [y_x(x_i) for x_i in x_values]
plt.plot(x_values, y_values, color="blue")

plt.show()