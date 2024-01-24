tickets = int(input('Введите количество билетов: '))
number_age = []

for i in range(0, tickets):
    value = int(input(f'Введите возраст участника №{i + 1}: '))
    number_age.append(value)

    def price(age):
        if age < 18:
            return 0
        elif 18 <= age < 25:
            return 990
        else:
            return 1390
    full_price = sum(map(price, number_age))

discount_price = int(full_price * 0.9)
if tickets > 3:
    print('Стоимость всех билетов со скидкой: ', discount_price, "рублей")
else:
    print('Стоимость всех билетов без скидки: ', full_price, "рублей")



