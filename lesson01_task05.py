# выручка и издержки компании, рентабельность, прибыль на одного сотрудника

revenues = int(input("Введите выручку компании: "))
costs = int(input("Введите издержки компании: "))
fin_result = revenues - costs

if fin_result > 0:
    staff = int(input("Введите количество сотрудников: "))
    revenues_profit = revenues / costs
    revenues_staff = fin_result / staff
    print("Поздравляем, компания работает с прибылью!")
    print('Рентабельность выручки >>> %.2f' % revenues_profit)
    print('Прибыль компании в расчете на одного сотрудника >>> %.2f' % revenues_staff)
else:
    print("Внимание, компания работает в убыток!")
