# самая большая цифра в числе

my_number = int(input("Введите целое число >>>"))
my_list = []

while my_number >= 1:
    my_list.append(my_number % 10)
    my_number //= 10

print("полный листинг: ", my_list)
my_max = max(my_list)
print("максимальная цифра в числе >>> ", my_max)
