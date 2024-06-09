#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from getpass import getpass
from utils import clear
import users
import menus
import films
import sales

DB = {
    'user_types': ['admin', 'client'],
    'users': [
        {
            'id': '1',
            'name': 'Admin',
            'email': 'admin@admin.com',
            'password': 'admin',
            'type': 'admin'
        },
        {
            'id': '2',
            'name': 'Cliente',
            'email': 'client@client.com',
            'password': 'client',
            'type': 'client'
        },
        {
            'id': '3',
            'name': 'Cliente 2',
            'email': 'client2@client.com',
            'password': 'client',
            'type': 'client'
        }
    ],
    'films': [
        {
            'id': '2',
            'title': 'Filme B',
            'description': 'Descrição do filme 2',
            'duration': '120', # in minutes
            'genre': ['Ação', 'Aventura'],
            'room_number': '1',
            'time': 'manhã', # 'manhã', 'tarde', 'noite'
            'capacity': 100,
            'price': 20.00,
        },
        {
            'id': '1',
            'title': 'Filme A',
            'description': 'Descrição do filme 1',
            'duration': '120', # in minutes
            'genre': ['Ação', 'Aventura'],
            'room_number': '1',
            'time': 'manhã', # 'manhã', 'tarde', 'noite'
            'capacity': 100,
            'price': 20.00,
        }
    ],
    'sales': [
        {
            'id': '1',
            'film_id': '1',
            'user_id': '2'
        },
        {
            'id': '2',
            'film_id': '2',
            'user_id': '3'
        }
    ],
}

previous_menu = menus.MAIN_MENU
active_menu = menus.MAIN_MENU

user_logged = DB['users'][1]

while True:
    clear()
    print('=' * 15, 'BEM VINDO AO CINE SERTÃO', '=' * 15)

    if (user_logged):
        print(f"\nOlá, {user_logged['name']}!")

    print(f"\n* {active_menu['title']}")

    valid_menu_options = []

    for option in active_menu['options']:
        if user_logged == None:
            if (option['need_auth'] or len(option['roles'])):
                continue
        else:
            if (option['need_no_auth'] or (len(option['roles']) and user_logged['type'] not in option['roles'])):
                continue
        valid_menu_options.append(option)
        print(f"{len(valid_menu_options)}. {option['title']}")

    menu_index = input("\nEscolha uma opção: ")

    if (not menu_index.isdigit() or
        int(menu_index) < 1 or
        int(menu_index) > len(valid_menu_options)
    ):
        getpass("Opção inválida.\n\nPressione Enter para continuar...")
        continue

    menu_option = valid_menu_options[int(menu_index) - 1]

    print('')

    if menu_option['code'] == 'films_menu':
        active_menu = menus.FILM_MENU
        continue

    elif menu_option['code'] == 'users_menu':
        active_menu = menus.USER_MENU
        continue

    elif menu_option['code'] == 'store_sale':
        sales.store_sale(DB, user_logged)

    elif menu_option['code'] == 'index_available_film':
        films.index_available_film(DB)

    elif menu_option['code'] == 'index_film':
        films.index_film(DB)

    elif menu_option['code'] == 'index_popular_film':
        films.index_popular_film(DB)

    elif menu_option['code'] == 'store_film':
        films.store_film(DB)

    elif menu_option['code'] == 'update_film':
        films.update_film(DB)

    elif menu_option['code'] == 'destroy_film':
        films.destroy_film(DB)

    elif menu_option['code'] == 'index_sale':
        sales.print_sales(DB, user_logged)

    elif menu_option['code'] == 'generate_sale_file':
        sales.generate_sales_file(DB, user_logged)

    elif menu_option['code'] == 'index_user':
        users.index_user(DB)

    elif menu_option['code'] == 'store_user':
        users.store_user(DB, user_logged)

    elif menu_option['code'] == 'update_user':
        users.update_user(DB)

    elif menu_option['code'] == 'destroy_user':
        users.destroy_user(DB)

    elif menu_option['code'] == 'login':
       user_logged = users.login(DB)

    elif menu_option['code'] == 'logout':
        print(f"Até mais, {user_logged['name']}!")
        user_logged = None

    elif menu_option['code'] == 'back':
        active_menu = previous_menu
        continue

    elif menu_option['code'] == 'exit':
        name = 'usuário anônimo' if user_logged == None else user_logged['name']
        print(f'Até mais, {name}!')
        exit()

    getpass("\nPressione Enter para continuar...")
