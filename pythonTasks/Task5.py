import Input_data

def Task5(auto_input=False):
    """
    Основная функция для выполнения программы.
    """
    try:
        print("Выберите способ ввода данных:")
        choice = input("1 - Ручной ввод, 2 - Автоввод чисел: ")
    
        if choice == "2":
            auto_input = True
        elif choice == "1":
            auto_input = False
        else:
            print("Ошибка: Введите 1 или 2.")
            return
    except ValueError:
        print("Ошибка: Некорректный ввод.")
        return

    numbers = Input_data.input_float_list(auto_input)
    if not numbers:
        print("Ошибка: список пуст.")
        return

    Input_data.display_list(numbers)

    max_abs_index = Input_data.find_max_absolute_value(numbers)
    print(f"Номер максимального по модулю элемента: {max_abs_index}, значение: {numbers[max_abs_index]}")

    product = Input_data.product_between_zeros(numbers)
    if product is None:
        print("Не найдено два нулевых элемента для вычисления произведения.")
    else:
        print(f"Произведение элементов между первыми и вторыми нулями: {product}")

if __name__ == "__main__":
    Task5(auto_input=False)