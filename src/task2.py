decimal_number = input("Введіть десяткове число: ")

# Перевірка на валідність
if decimal_number.isdigit():
    # конвертація рядка у список цифр
    digits = [int(digit) for digit in decimal_number]

    # знаходження найбільшої цифри
    max_digit = max(digits)

    print(f"Найбільша цифра в числі {decimal_number} - це {max_digit}")
else:
    print("Введене значення не є десятковим числом.")
