#cdscsdcs
import Input_data


from tabulate import tabulate


import math


def Task1():
    """
    Computes ln(1 - x) using Taylor series expansion.

    Uses Input_data for input handling and tabulate for formatted output.
    """

    max_iterations = 500
    choice = Input_data.Input_data("Write 1 for manual input, 2 for automatic input: ", int, 1, 2)

    # Получение входных данных
    if choice == 1:
        x = Input_data.Input_data("Write x (-1 < x < 1): ", float, -0.999999, 0.999999)
        eps = Input_data.Input_data("Write eps (0 < eps < 1): ", float, 0.0000001, 1)
    else:
        x = Input_data.Random_Input(float, -0.999999, 0.999999)
        eps = Input_data.Random_Input(float, 0.0000001, 1)

    # Вычисление ряда
    sum_result = 0.0
    n = 1
    term = x  # Первый член ряда

    while abs(term) > eps and n <= max_iter:
        term = (-1)**n * (x**n) / n
        sum_result += term
        n += 1

    actual_value = math.log(1 - x)

    # Вывод результата в таблице
    table_data = [[x, n - 1, sum_result, actual_value, eps]]
    table_headers = ["x", "n", "F(x)", "Math F(x)", "eps"]
    print(tabulate(table_data, headers=table_headers, floatfmt=".8f"))