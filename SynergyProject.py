import datetime
from datetime import date


def validate_date(day, month, year):
    """Проверяет корректность введенной даты"""
    try:
        datetime.date(year, month, day)
        return True
    except ValueError:
        return False


def get_valid_input(prompt, min_val=None, max_val=None):
    """Запрашивает ввод от пользователя с проверкой"""
    while True:
        try:
            value = int(input(prompt))

            # Проверяем диапазон значений
            if min_val is not None and value < min_val:
                print(f"Значение должно быть не менее {min_val}")
                continue
            if max_val is not None and value > max_val:
                print(f"Значение должно быть не более {max_val}")
                continue

            return value

        except ValueError:
            print("Пожалуйста, введите целое число")


def get_day_of_week(birthday):
        return birthday.strftime("%A")


def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 == 0:
        return False
    else:
        return True


def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age


def print_digit_with_stars(digit):
    # Шаблоны цифр из звёздочек
    patterns = {
        '0': [
            "*****",
            "*   *",
            "*   *",
            "*   *",
            "*****"
        ],
        '1': [
            "  *  ",
            " **  ",
            "  *  ",
            "  *  ",
            "*****"
        ],
        '2': [
            "*****",
            "    *",
            "*****",
            "*    ",
            "*****"
        ],
        '3': [
            "*****",
            "    *",
            "*****",
            "    *",
            "*****"
        ],
        '4': [
            "*   *",
            "*   *",
            "*****",
            "    *",
            "    *"
        ],
        '5': [
            "*****",
            "*    ",
            "*****",
            "    *",
            "*****"
        ],
        '6': [
            "*****",
            "*    ",
            "*****",
            "*   *",
            "*****"
        ],
        '7': [
            "*****",
            "    *",
            "   * ",
            "  *  ",
            " *   "
        ],
        '8': [
            "*****",
            "*   *",
            "*****",
            "*   *",
            "*****"
        ],
        '9': [
            "*****",
            "*   *",
            "*****",
            "    *",
            "*****"
        ]
    }

    # Получаем шаблон для указанной цифры
    return patterns.get(str(digit), ["     "] * 5)


def print_number_with_stars(number):
    # Преобразуем число в строку и получаем шаблоны для каждой цифры
    digits = [print_digit_with_stars(d) for d in str(number)]

    # Выводим цифры построчно
    for i in range(5):
        print(" ".join(digit[i] for digit in digits))


def main():
    print("Введите дату вашего рождения:")

    # Получаем день с проверкой (1-31)
    day = get_valid_input("День (1-31): ", 1, 31)

    # Получаем месяц с проверкой (1-12)
    month = get_valid_input("Месяц (1-12): ", 1, 12)

    # Получаем год с проверкой (1900-2025)
    year = get_valid_input("Год (1900-2025): ", 1900, 2025)

    # Создаем объект даты
    birthday = datetime.date(year, month, day)

    # Использование функции get_day_of_week
    day_of_week = get_day_of_week(birthday)

    # Использование функции is_leap_year
    is_leap = is_leap_year(year)

    # Использование функции
    age = calculate_age(birthday)

    # Проверяем корректность всей даты
    if validate_date(day, month, year):
        print(f"\nВаша информация:\nДата вашего рождения - {day}.{month}.{year} корректна!")
        print(f"День вашего дня рождения - это {day_of_week}")
        print(f"Год {year} {'високосный' if is_leap else 'не является високосным'}")
        print(f"Ваш текущий возраст: {age} года/лет")
    else:
        print("\nОшибка: такая дата невозможна!")

    #Использование электронного табло
    number = day, month, year
    print("Дата вашего рождения в формате электронного табло: ")
    print_number_with_stars(number)

if __name__ == "__main__":
    main()