# переменные, запрос ввода чисел и строк, сохранение в переменные, вывод на экран,
# форматирование строки ( f, %, format() )
# функция проверки строковых переменных на ввод чисел, чтобы избежать ошибок при вводе

def chek_numeric(user_str):
    if user_str.isdigit():
        return 0
    else:
        try:
            float(user_str)
            return 1
        except ValueError:
            return 2


my_integer = 13
my_float = 33.2145
my_string = "Начинаем осваивать Python: "
print(f"f-строки: {my_integer:>8} {my_float:>10} {my_string}")
print("метод format(): {2} {0:>10} {1:>10} {3:>10.4f}".format(my_integer, my_float, my_string, my_integer / my_float))
print("метод оператор: %-35s %-7d %.2f" % (my_string, my_integer, my_float))

while True:
    user_integer = input("Введите целое число >>>")
    if chek_numeric(user_integer) == 0:
        user_integer = int(user_integer)
        break
    else:
        print("Это не целое число, повторите ввод!")
        continue

while True:
    user_float = input("Введите дробное число >>>")
    if chek_numeric(user_float) == 1:
        user_float = float(user_float)
        break
    else:
        print("Это не число c плавающей запятой!")
        continue

user_string = input("Введите строку приветствия:")
print(user_integer, user_float, user_string)
print(f'Делим целое число на число с плавающей запятой, 40 знаков: {(user_integer / user_float):.40f}')
print(f"2 знака: {user_integer} / {user_float} = {(user_integer / user_float):.2f}")
