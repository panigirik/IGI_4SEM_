import Task1
import Task2
import Task3 
import Task4
import Task5
from Input_data import Input_data

def main_menu():
    """
    Функция для отображения главного меню и выполнения выбранной задачи.

    Функция отображает меню с опциями для каждой задачи и запрашивает ввод от пользователя.
    В зависимости от выбора пользователя выполняет соответствующую задачу или завершает программу.

    Аргументы: Нет

    Возвращает: Нет
    """

    while True:
        print("МЕНЮ")
        print("1. Задача 1")
        print("2. Задача 2")
        print("3. Задача 3")
        print("4. Задача 4")
        print("5. Задача 5")
        print("0. Выход")

        выбор = Input_data("Введите номер задачи: ", int, 0, 5)

        if выбор == 1:
            Task1.Task1()
        elif выбор == 2:
            Task2.Task2()
        elif выбор == 3:
            Task3.Task3()
        elif выбор == 4:
            print(dir(Task4))
            Task4.Task4()
        elif выбор == 5:
            Task5.Task5()
        elif выбор == 0:
            print("Выход из программы...")
            break