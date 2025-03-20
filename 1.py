while True:
    data = set()
    while True:
        user_input = input("Введите данные (Enter для завершения ввода): ")
        if user_input == "":
            break
        data.add(user_input)
    print("Уникальные значения:", data)
