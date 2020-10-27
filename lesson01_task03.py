# ввести число n и найти сумму чисел n + nn + nnn
# функция проверки корректности ввода целого числа

def chek_numeric(user_str):
    if user_str.isdigit():
        return 0
    else:
        try:
            float(user_str)
            return 1
        except ValueError:
            return 2


while True:
    n = input("Введите целое число >>>")
    if chek_numeric(n) == 0:
        break
    else:
        print("Это не целое число, повторите ввод!")
        continue
my_sum = int(n) + int(n + n) + int(n + n + n)
print(my_sum)
