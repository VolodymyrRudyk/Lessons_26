print('%(qty)d more %(food)s' % {'qty': 1, 'food': 'spam'})

#шаблон з ціллю підстановки
reply = """                                 
Greetings...
Hello %(name)s!
Your age is %(age)s
"""
values = {'name': 'Bob', 'age': 40}         #створення значення для підстановки
print(reply % values)                       #виконання підстановки

food = 'spam'
qty = 10
print(vars())
print('%(qty)d more %(food)s' % vars())     #змінні є ключами в vars()
