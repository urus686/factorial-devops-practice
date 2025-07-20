import math

def calculate_factorial(n):
    """Вычисляет факториал числа с использованием библиотеки math."""
    return math.factorial(n)

def get_positive_integer():
    """Запрашивает у пользователя положительное целое число."""
    while True:
        user_input = input("Введите положительное целое число: ")
        try:
            number = int(user_input)
            if number < 0:
                print("Ошибка: число должно быть неотрицательным.")
            else:
                return number
        except ValueError:
            print("Ошибка: введите именно целое число.")

def main():
    number = get_positive_integer()
    result = calculate_factorial(number)
    print(f"Факториал числа {number} равен {result}")

if __name__ == "__main__":
    main()
