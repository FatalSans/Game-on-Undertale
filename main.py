from func import *

print('Вы в Нарнии')
name_ask = input('Введи своё имя: ')
player['name'] = name_ask
current_enemy=0
while current_enemy<3:
    action = input('''Выбери действие:
        1 - В бой!  
        2 - Информация об игроке
        3 - Информация о текущем противнике  
        4 - Показать инвентарь  
        5 - Тренировка 
        6 - Магазин  
        7 - Получение денег 
        8 - Баланс 
        ''')
    if action == '1':
        if current_enemy != 2:
            current_enemy=Fight(current_enemy)
        else:
            Fight_Sans()
            current_enemy+=1
    elif action == '2':
        Stats()
    elif action == '5':
        x = input('Что вы хотите качать атаку или защиту ')
        Training(x)
    elif action == '3':
        Enemies(current_enemy)
    elif action =='7':
        Pay()
    elif action =='4':
        Inventory_1()
    elif action =='6':
        Shop()
    elif action == '8':
        Balance()
    input('Введите enter')

if player["mercy_end"]>=2:
    print('Молодец,♑︎□︎□︎♎︎ 🙰□︎♌︎')
elif player["genocide_end"]>=2:
    print('Чара:ТЕПРЬ Я ГЛАВНАЯ')
else:
    print('НЕйтрал')