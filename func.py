import time

from data import *

import random


def Subjects():
    def Spell_luck():
        if player["Inventory"]["Зелье удачи"] > 0:
            player["Inventory"]["Зелье удачи"] -= 1
            player["luck"] += 5
            print(
                f'Вы выпили зельку(у вас осталось {player["Inventory"]["Зелье удачи"]} зелек) ваша удача == {player["luck"]}%')
        else:
            print('Нет зелек')

    def Food():
        x = input('Выбери что будешь есть ирисковый пирог или мета бургер ')
        x = x.capitalize()
        if x == "Пирог":
            if player["Inventory"]["Ирисковый пирог"] > 0:
                player["HP"] += foods[0]["health"]
                print('Ваше здоровье было вылечено на 80')
                player["Inventory"]["Ирисковый пирог"] -= 1
            else:
                print('нет ирисковых ВАЛАУДЖИ')
        if x == "Бургер":
            if player["Inventory"]["МетаБургер"] > 0:
                player["HP"] += foods[1]["health"]
                print('Ваше здоровье было вылечено на 40')
                player["Inventory"]["МетаБургер"] -= 1
            else:
                print('нет Мета бургеров,ееее....')

    x = input('Выбери что ты будешь делать есть еду или Выпить зелье ')
    x = x.capitalize()
    if x == "Есть еду":
        Food()
    if x == 'Выпить зелье':
        Spell_luck()


def Stats():
    print(f'Игрок - {player["name"]}')
    print(
        f'Величина атаки - {player["attack"]}. Шанс критического урона ({player["attack"] * 3}ед.) равен {player["luck"]}%')
    print(f'Броня поглощает {int((player["resistance"]) * 100)}% урона')
    print()


def Training(type_training):
    def event():
        x = int(input('На сколько хочешь повысить вес штанги от 5 до 25 кг '))
        if random.randint(0, 100) <= 80 - (x - 5) * 3.5:
            print('Успех')
            return x
        else:
            print('Неуспех')
            return 0

    Flag = True
    for i in range(6):
        if random.randint(0, 100) > 80 and Flag:

            Flag = False
            force = event()


        else:
            print(f'Тренировка завершена на {i * 20}%')
            time.sleep(0.1)

    if Flag:
        force = 5
    if type_training == '1':
        player['attack'] += force
    else:
        player['resistance'] += force / 1000 * 3


def Enemies(type_enemy):
    enemy = enemes[type_enemy]
    print(f'Противник - {enemy["name"]}')
    print(f'Величина атаки - {enemy["attack"]}. Шанс критического урона ({enemy["attack"] * 3}ед.) ')
    print(f'Кол-во HP {enemy["hp"]}')
    print(f'Броня поглощает {int((enemy["resistance"]) * 100)}% урона')
    print(f'Для пощады требуется: {enemy["for_mercy"]}')
    print()


def Fight(current_enemy):
    def Atack():
        player["HP"] -= enemy["attack"] * (1 - player["resistance"])
        print(f'Ваше здоровье = {player["HP"]} , ', end='')
        if random.randint(0, 100) <= player["luck"]:
            enemy["hp"] -= player["attack"] * 3
            print(f'Вы нанесли:{player["attack"] * 3}')
        else:
            enemy["hp"] -= player["attack"]
            print(f'Вы нанесли:{player["attack"]}')

        print(f'Здоровье врага = {enemy["hp"]},'
              f'Ваш противник нанёс:{enemy["attack"] * (1 - player["resistance"])}')

    def Block():

        player["HP"] -= enemy["attack"] * (1 - (player["resistance"] + player["block"]))
        print(f'Ваше здоровье = {player["HP"]},'
              f'Ваш противник нанёс:{enemy["attack"] * (1 - (player["resistance"] + player["block"]))}')

    def Mercy():
        enemy["mercy"] += 1
        enemy["attack"] *= 0.8
        print('Атака противника уменьшена')
        player["HP"] -= enemy["attack"] * (1 - (player["resistance"]))
        print(f'Ваше здоровье = {player["HP"]},'
              f'Ваш противник нанёс:{enemy["attack"] * (1 - (player["resistance"]))}')
        print(f'Вы сказала {enemy["name"]}у что он хороший')

    enemy = enemes[current_enemy]
    print(enemy["script"])
    while enemy["hp"] >= 0 and player["HP"] >= 0 and enemy["mercy"] < enemy["for_mercy"]:
        x = input('Выберите действие: Атака, Блок, Пощада,Выбрать предмет ')
        x = x.capitalize()

        if x == 'Атака':
            Atack()
        if x == 'Блок':
            Block()
        if x == 'Пощада':
            Mercy()
        if x == 'Выбрать предмет':
            Subjects()

        print()
        time.sleep(1)

    if enemy["hp"] <= 0:
        player["genocide_end"] += 1
        enemes[2]["attack"] += current_enemy * 20 + 10
        print(enemy["genocide_win"])
    if player["HP"] <= 0:
        print(enemy["loss"])
    if enemy["mercy"] == enemy["for_mercy"]:
        player["mercy_end"] += 1
        print(enemy["mercy_win"])
    current_enemy += 1
    return current_enemy


def Fight_Sans():
    def Attack():
        print('Вы атковали но оказалось не все монстры стоят на месте')
        player["HP"] -= enemes[2]["attack"] * (1 - player["resistance"])
        enemes[2]["mises"]-=1
        print(f'Ваше здоровье = {player["HP"]} , Санс нанёс:{enemes[2]["attack"] * (1 - player["resistance"])}')

    if player["genocide_end"] == 2:
        print(enemes[2]["script"])
        while player["HP"] > 0 and enemes[2]["mises"] > 0:
            x = input('Выберите действие: Атака, Выбрать еду ')
            x = x.capitalize()

            if x == 'Атака':
                Attack()
            if x == "Выбрать еду":
                Subjects()
            print()
            time.sleep(1)
        if enemes[2]["mises"] <= 0:
            player["genocide_end"] += 1
            print(enemes[2]["genocide_win"])
        if player["HP"] <= 0:
            print(enemes[2]["loss"])
    else:
        print(enemes[2]["mercy_win"])


def Pay():
    print('Ты работаешь на Фриск есть шанс зароботать (но сколько?).')
    if random.randint(1, 100) <= player["luck_for_money"]:
        player["money"] += 500
        print("Вы заработали 500 G(Грабелей)")
    else:
        print('Все твои деньги забрал Фриск из Реалистичного Андэртэйла')


def Shop():
    x = input(
        'Выбирите что будете покупать :Пирог который хилит 80 хп,Бургер который хилит 40 хп или купить Зелье удачи ')
    x = x.capitalize()
    if x == 'Пирог':
        print(f'Стоимость покупки пирога = {foods[0]["cost"]}')
        y = input('Хотите купить? ')
        y = y.capitalize()
        if y == 'Да' and player["money"] >= foods[0]["cost"]:
            player["money"] -= foods[0]["cost"]
            player["Inventory"]["Ирисковый пирог"] += 1
            print('Вы купили пирог')
        else:
            print('У вас нехватает денег либо вы просто скипнули')
    if x == 'Бургер':
        print(f'Стоимость покупки бургера = {foods[1]["cost"]}')
        y = input('Хотите купить? ')
        y = y.capitalize()
        if y == 'Да' and player["money"] >= foods[1]["cost"]:
            player["money"] -= foods[1]["cost"]
            player["Inventory"]["МетаБургер"] += 1
            print('Вы купили МетаБургер')
        else:
            print('У вас нехватает денег либо вы просто скипнули')
    if x == 'Зелье удачи':
        print(f'Стоимость покупки зельки = {potions[0]["cost"]}')
        y = input('Хотите купить? ')
        y = y.capitalize()
        if y == 'Да' and player["money"] >= potions[0]["cost"]:
            player["money"] -= potions[0]["cost"]
            player["Inventory"]["Зелье удачи"] += 1
            print('Вы купили Зелье удачи')
        else:
            print('У вас нехватает денег либо вы просто скипнули')


def Inventory_1():
    inventory_keys = list(player['Inventory'].keys())
    for i in range(3):
        print(f'{inventory_keys[i]}: {player["Inventory"][inventory_keys[i]]}')


def Balance():
    print(f'У вас: {player["money"]}G')
