Sum_tickets=0  #значение стоимости билетов
Ticket_quantity=int(input("Укажите количество билетов для покупки:"))  #ввод количества покупаемых на конференцию билетов
age = int(input("Укажите свой возраст:")) #ввод возраста покупателя (участника конференции)
for Sum_tickets in range (Ticket_quantity):
    if  age<18:
        Sum_tickets = 0
    elif 18<=age<25:
        Sum_tickets = 990*Ticket_quantity
    elif age>=25:
        Sum_tickets = 1390*Ticket_quantity
print("Стоимость билетов составляет:",Sum_tickets)
if Ticket_quantity>3:
        DiscountPrice=int(Sum_tickets-(Sum_tickets*0.1))   # в случае, если участник конференции покупает более трех билетов - скидка 10%
else:
    DiscountPrice = Sum_tickets
print("Стоимость билетов составляет c учетом скидки (если более 3-х участников):", DiscountPrice)
