# перевод числа секунд в часы, минуты, секунды
# формат вывода - чч:мм:сс
number_seconds = int(input("Введите количество секунд:"))
my_hours = number_seconds // 3600
my_minutes = (number_seconds - my_hours * 3600) // 60
my_seconds = number_seconds % 60
print("%02d:%02d:%02d" % (my_hours, my_minutes, my_seconds))
