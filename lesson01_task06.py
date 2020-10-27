# расчет количества дней для достижения результата пробежки

distance_start = int(input("Результат пробежки первого дня, км: "))
distance_finish = int(input("Требуемый результат пробежки , км: "))
list_day = [distance_start]
counter = 1

while distance_start <= distance_finish:
    counter += 1
    distance_start *= 1.1
    list_day.append(round(distance_start, 2))

print("До требуемого результата потребуется >>> ", counter, " дней")
