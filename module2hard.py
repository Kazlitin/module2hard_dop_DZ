def find_password1(n):
    password = n
         # Перебираем все возможные пары чисел от 1 до n
    for i in range(1, n + 1):
        for j in range(i + 1, n):
            if n % (i + j) == 0:
                i > j
                i !=j
                password = str(i) + str(j)
                if not found_password1:
                    return password
         # Если пароль не найден, возвращаем None
    return None


found_password1 = False

     # Вводим число n
num = int(input("Введите число n (от 3 до 20): "))

     # Получаем пароль
result = find_password1(num)

if result is not None:
    print("Нужный пароль:", result)
else:
    print("Пароль не найден.")