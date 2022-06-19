guests = int(input())

if guests < 20:
    print('Дом')
if guests >= 20 and guests <= 50:
    print('Кафе')
if guests > 50:
    print('Ресторан')
