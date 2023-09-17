user_input = input("Введіть ваш рядок тексту: ")

if len(user_input) >= 20:
    # Отримання кожного 3-го символу від 4-го символа до 20-го символа
    result_slice = user_input[3:20:3]
    print(result_slice)
else:
    print("Рядок занадто короткий для виконання операції зрізу.")
