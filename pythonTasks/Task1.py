import math
import Input_data
from tabulate import tabulate

def Task1():
    """
    Computes ln(1 - x) using Taylor series expansion.
    """

    max_iterations = 500
    
    try:
        choice = Input_data.Input_data("Введите 1 для самостоятельного ввода, 2 для автоматического: ", int, 1, 2)
    except ValueError:
        print("Ошибка: Введите целое число 1 или 2.")
        return

    # Getting input data
    if choice == 1:
        try:
            x = Input_data.Input_data("Введите x (-1 < x < 1): ", float, -0.999999, 0.999999)
            eps = Input_data.Input_data("Введите точность  (0 < eps < 1): ", float, 0.0000001, 1)
        except ValueError:
            print("Ошибка: Введены некорректные данные.")
            return
    else:
        x = Input_data.Random_Input(float, -0.999999, 0.999999)
        eps = Input_data.Random_Input(float, 0.0000001, 1)

    # Series calculation
    sum_series = 0.0
    n = 1
    series_term = x  # First term of the series

    while abs(series_term) > eps and n <= max_iterations:
        series_term = (-1)**n * (x**n) / n
        sum_series += series_term
        n += 1

    exact_value = math.log(1 - x)

    # Output result in table format
    table = [[x, n - 1, sum_series, exact_value, eps]]
    headers = ["x", "n", "F(x)", "Exact F(x)", "eps"]
    print(tabulate(table, headers=headers, floatfmt=".8f"))

if __name__ == "__main__":
    Task1()
