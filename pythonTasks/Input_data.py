import random
import string

def Input_data(prompt, data_type, min_value=None, max_value=None, auto_input=False):
    """
    Function to get user input with data type validation and optional value range constraints.

    Args:
    - prompt (str): The prompt message for the user.
    - data_type (type): The expected data type for user input (int, float, or str).
    - min_value (int/float, optional): The minimum allowed value (inclusive). Defaults to None.
    - max_value (int/float, optional): The maximum allowed value (inclusive). Defaults to None.
    - auto_input (bool, optional): If True, generates a random input automatically for testing purposes.

    Returns:
    - user_input (int/float/str): The validated user input.

    Raises:
    - ValueError: If the user input does not match the specified data type or falls outside the specified range.
    """

    if auto_input:
        return Random_Input(data_type, min_value, max_value)
    
    while True:
        try:
            user_input = data_type(input(prompt))
            if min_value is not None and user_input < min_value:
                raise ValueError(f"Значение должно быть не менее {min_value}")
            if max_value is not None and user_input > max_value:
                raise ValueError(f"Значение должно быть не более {max_value}")
            return user_input
        except ValueError as e:
            print(f"Ошибка: {e}. Пожалуйста, введите корректное значение.")

def Random_Input(data_type, min_value=None, max_value=None):
    """
    Function to generate random data based on the specified data type and optional value range constraints.

    Args:
    - data_type (type): The data type for the generated value (int, float, or str).
    - min_value (int/float, optional): The minimum allowed value (inclusive). Defaults to None.
    - max_value (int/float, optional): The maximum allowed value (inclusive). Defaults to None.

    Returns:
    - generated_value (int/float/str): The randomly generated value.

    Raises:
    - ValueError: If the specified data type is not supported (supported types: int, float, str).
    """

    if data_type == str:
        if min_value is None:
            min_value = 1
        if max_value is None:
            max_value = 10

        generated_value = ''.join(
            random.choices(string.ascii_letters + string.digits, k=random.randint(min_value, max_value)))
        return generated_value

    if min_value is None:
        min_value = float('-inf')
    if max_value is None:
        max_value = float('inf')

    if data_type == int:
        generated_value = random.randint(min_value, max_value)
    elif data_type == float:
        generated_value = random.uniform(min_value, max_value)
    else:
        raise ValueError("Неподдерживаемый тип данных. Поддерживаемые типы: int, float, str.")

    return generated_value


def input_float_list(auto_input=False):
    """
    Функция для ввода списка вещественных чисел.
    Запрашивает размер списка и генерирует случайные числа.
    
    Если auto_input=True, заполняет список случайными значениями автоматически.
    """

    size = int(input("Введите размер списка: "))

    if auto_input:
        float_list = [random.uniform(-10, 10) for _ in range(size)]
    else:
        float_list = [float(input(f"Введите число {i + 1}: ")) for i in range(size)]

    print(f"Список: {float_list}")
    
    return float_list



def find_max_absolute_value(float_list):
    """
    Функция для нахождения номера максимального по модулю элемента списка.
    """
    if not float_list:
        return None
    max_abs_index = max(range(len(float_list)), key=lambda i: abs(float_list[i]))
    return max_abs_index


def product_between_zeros(float_list):
    """
    Функция для нахождения произведения элементов, расположенных между первыми и вторыми нулями списка.
    """
    zero_indices = [i for i, num in enumerate(float_list) if num == 0]

    if len(zero_indices) < 2:
        return None

    product = 1
    for num in float_list[zero_indices[0] + 1:zero_indices[1]]:
        product *= num

    return product


def display_list(float_list):
    """
    Функция для вывода списка на экран.
    """
    print("Список чисел:", float_list)
