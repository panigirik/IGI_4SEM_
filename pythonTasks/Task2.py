import Input_data

def Task2():
    """
    Counts the number of even numbers entered by the user.
    Input can be manual or automatic.
    Terminates if a number greater than 1000 is entered.
    """
    even_count = 0  # Counter for even numbers
    
    try:
        choice = Input_data.Input_data("введите 1 для самостоятельного ввода, 2 для автоматического: ", int, 1, 2)
    except ValueError:
        print("Ошибка: Введите целое число 1 или 2.")
        return
    
    if choice == 1:
        # Manual input
        while True:
            try:
                number = Input_data.Input_data("Введите число (x > 1000 чтобы остановить цикл): ", int, None, None)
            except ValueError:
                print("Ошибка: Введите корректное целое число.")
                continue
            
            if number > 1000:
                break  # Stop the loop
            
            if number % 2 == 0:
                even_count += 1  # Increment even number counter
    
    elif choice == 2:
        # Automatic random input
        while True:
            number = Input_data.Random_Input(int, -1000, 1100)  # Generate random number
            print(f"Сгенерированное число: {number}")  # Print generated number
            
            if number > 1000:
                break  # Stop the loop
            
            if number % 2 == 0:
                even_count += 1  # Increment even number counter
    
    print(f"Всего четных чисел: {even_count}")

if __name__ == "__main__":
    Task2()
