#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import random
from getpass import getpass
from utils import is_valid_email
from menus import MAIN_MENU, USER_MENU, FILM_MENU
from films import print_film, most_sale_films

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
        }
    ],
    'films': [
        {
            'id': '2',
            'title': 'Filme 2',
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
            'title': 'Filme 1',
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
            'film_id': '1',
            'user_id': '2'
        }
    ],
}

previous_menu = MAIN_MENU
active_menu = MAIN_MENU

user_logged = DB['users'][0]

while True:
    print('\033c')
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
        input("Opção inválida.\n\nPressione Enter para continuar...")
        continue

    menu_option = valid_menu_options[int(menu_index) - 1]

    print('')

    if menu_option['code'] == 'films_menu':
        active_menu = FILM_MENU
        continue

    elif menu_option['code'] == 'users_menu':
        active_menu = USER_MENU
        continue

    elif menu_option['code'] == 'store_sale':
        print('-' * 30)
        filmes_disponiveis = False
        for film in DB['films']:
            total_sales = len([sale for sale in DB['sales'] if sale['film_id'] == film['id']])
            available_seats = film['capacity'] - total_sales
            if available_seats > 0:
                filmes_disponiveis = True
                print(f"ID: {film['id']}")
                print(f"Filme: {film['title']}")
                print(f"Descrição: {film['description']}")
                print(f"Duração: {film['duration']} minutos")
                print(f"Gênero: {', '.join(film['genre'])}")
                print(f"Sala: {film['room_number']}")
                print(f"Horário: {film['time']}")
                print(f"Assentos disponíveis: {available_seats} de {film['capacity']}")
                print(f"Preço: R$ {film['price']:.2f}")
                print('-' * 30)
        if filmes_disponiveis:
            film_id = input("Digite o ID do filme que deseja comprar: ")
            film = next((film for film in DB['films'] if film['id'] == film_id), None)
            if film:
                new_sale = {
                    'id': str(random.random()).split('.')[1],
                    'film_id': film_id,
                    'user_id': user_logged['id']
                }
                DB['sales'].append(new_sale)
                print('Ingresso comprado com sucesso!')
            else:
                print('Filme não encontrado!')
        else:
            print("Desculpe, não há filmes disponíveis para venda no momento.")

    elif menu_option['code'] == 'index_film':
        print('-' * 30)
        films = DB['films']
        for film in films:
            print_film(DB, film)

    elif menu_option['code'] == 'index_popular_film':
        print('-' * 30)
        films = most_sale_films(DB)
        for film in films:
            print_film(DB, film)

    elif menu_option['code'] == 'store_film':
        new_film = {
            'id': str(random.random()).split('.')[1]
        }
        new_film['title'] = input("Digite o título: ")
        new_film['description'] = input("Digite a descrição: ")

        while True:
            new_film['duration'] = input("Digite a duração (em minutos): ")
            if new_film['duration'].isdigit():
                new_film['duration'] = int(new_film['duration'])
                break
            print('Duração inválida!')

        new_film['genre'] = input("Digite o gênero (separado por vírgula): ").split(',')

        while True:
            new_film['room_number'] = input("Digite o número da sala: ")
            if new_film['room_number'].isdigit():
                new_film['room_number'] = int(new_film['room_number'])
                break
            print('Número inválido!')

        while True:
            new_film['time'] = input("Digite o horário (manhã, tarde ou noite): ")
            if new_film['time'] in ['manhã', 'tarde', 'noite']:
                break
            print('Horário inválido!')

        while True:
            new_film['capacity'] = input("Digite a capacidade da sala: ")
            if new_film['capacity'].isdigit():
                new_film['capacity'] = int(new_film['capacity'])
                break
            print('Capacidade inválida!')

        while True:
            new_film['price'] = input("Digite o preço: ")
            if new_film['price'].replace('.', '', 1).isdigit():
                new_film['price'] = float(new_film['price'])
                break
            print('Preço inválido!')

        DB['films'].append(new_film)

        print('Filme cadastrado com sucesso!')

    elif menu_option['code'] == 'update_film':
        film_id = input("Digite o ID do filme: ")

        update_film = next((film for film in DB['films'] if film['id'] == film_id), None)

        if update_film == None:
            print('Filme não encontrado!')
            input("\nPressione Enter para continuar...")
            continue

        update_film['title'] = input(f"Digite o título ({update_film['title']}): ")
        update_film['description'] = input(f"Digite a descrição ({update_film['description']}): ")

        duration_prompt = f"Digite a duração (em minutos) ({update_film['duration']}): "
        while True:
            update_film['duration'] = input(duration_prompt)
            if update_film['duration'].isdigit():
                update_film['duration'] = int(update_film['duration'])
                break
            print('Duração inválida!')

        update_film['genre'] = input(f"Digite o gênero (separado por vírgula) ({', '.join(update_film['genre'])}): ").split(',')

        room_prompt = f"Digite o número da sala ({update_film['room_number']}): "
        while True:
            update_film['room_number'] = input(room_prompt)
            if update_film['room_number'].isdigit():
                update_film['room_number'] = int(update_film['room_number'])
                break
            print('Número inválido!')

        time_prompt = f"Digite o horário (manhã, tarde ou noite) ({update_film['time']}): "
        while True:
            update_film['time'] = input(time_prompt)
            if update_film['time'] in ['manhã', 'tarde', 'noite']:
                break
            print('Horário inválido!')

        capacity_prompt = f"Digite a capacidade da sala ({update_film['capacity']}): "
        while True:
            update_film['capacity'] = input(capacity_prompt)
            if update_film['capacity'].isdigit():
                update_film['capacity'] = int(update_film['capacity'])
                break
            print('Capacidade inválida!')

        price_prompt = f"Digite o preço (R$ {update_film['price']:.2f}): "
        while True:
            update_film['price'] = input(price_prompt)
            if update_film['price'].replace('.', '', 1).isdigit():
                update_film['price'] = float(update_film['price'])
                break
            print('Preço inválido!')

        print('Filme atualizado com sucesso!')

    elif menu_option['code'] == 'destroy_film':
        film_id = input("Digite o ID do filme: ")
        if any(film['id'] == film_id for film in DB['films']):
            DB['films'] = [film for film in DB['films'] if film['id'] != film_id]
            print('Filme apagado com sucesso!')
        else:
            print('Filme não encontrado!')

    elif menu_option['code'] == 'index_sale':
        print('-' * 30)
        for sale in DB['sales']:
            film = next((film for film in DB['films'] if film['id'] == sale['film_id']), None)
            if (user_logged['type'] == 'admin'):
                user = next((user for user in DB['users'] if user['id'] == sale['user_id']), None)
                print(f"Venda ID: {sale['id']}")
                print(f"Usuário ID: {sale['user_id']}")
                if user:
                    print(f"Usuário: {user['name']}")
                else:
                    print("Usuário não encontrado")
                print(f"Filme ID: {sale['film_id']}")
            else:
                if user_logged['id'] != sale['user_id']:
                    continue
            if film:
                print(f"Filme: {film['title']}")
                print(f"Descrição: {film['description']}")
                print(f"Duração: {film['duration']} minutos")
                print(f"Gênero: {', '.join(film['genre'])}")
                print(f"Sala: {film['room_number']}")
                print(f"Horário: {film['time']}")
                total_sales = len([sale for sale in DB['sales'] if sale['film_id'] == film['id']])
                print(f"Assentos vendidos: {total_sales} de {film['capacity']}")
                print(f"Preço: R$ {film['price']:.2f}")
            else:
                print("Filme não encontrado")
            print('-' * 30)

    elif menu_option['code'] == 'index_user':
        print('-' * 30)
        for user in DB['users']:
            print(f"ID: {user['id']}")
            print(f"Nome: {user['name']}")
            print(f"Email: {user['email']}")
            print(f"Tipo: {user['type']}")
            print('-' * 30)

    elif menu_option['code'] == 'store_user':
        new_user = {
            'id': str(random.random()).split('.')[1],
            'type': 'client'
        }
        new_user['name'] = input("Digite o nome: ")

        while True:
            new_user['email'] = input("Digite o email: ")

            if not is_valid_email(new_user['email']):
                print('Email inválido!')
            elif any(user['email'] == new_user['email'] for user in DB['users']):
                print('Email já cadastrado!')
            else:
                break

        new_user['password'] = getpass("Digite a senha: ")

        if user_logged and user_logged['type'] == 'admin':
            while True:
                new_user['type'] = input("Digite o tipo (admin ou client): ")
                if new_user['type'] in DB['user_types']:
                    break
                print('Tipo inválido!')

        DB['users'].append(new_user)

        print('Usuário cadastrado com sucesso!')

    elif menu_option['code'] == 'update_user':
        user_id = input("Digite o ID do usuário: ")

        update_user = next((user for user in DB['users'] if user['id'] == user_id), None)

        if update_user == None:
            print('Usuário não encontrado!')
            input("\nPressione Enter para continuar...")
            continue

        update_user['name'] = input(f"Digite o nome ({update_user['name']}): ")

        email_prompt = f"Digite o email ({update_user['email']}): "
        while True:
            update_user['email'] = input(email_prompt)

            if not is_valid_email(update_user['email']):
                print('Email inválido!')
            elif any(user['email'] == update_user['email'] and user['id'] != update_user['id'] for user in DB['users']):
                print('Email já cadastrado!')
            else:
                break

        update_user['password'] = getpass(f"Digite a senha ({update_user['password']}): ")

        if user_logged['type'] == 'admin':
            type_prompt = f"Digite o tipo (admin ou client) ({update_user['type']}): "
            while True:
                update_user['type'] = input(type_prompt)
                if update_user['type'] in DB['user_types']:
                    break
                print('Tipo inválido!')

        print('Usuário atualizado com sucesso!')

    elif menu_option['code'] == 'destroy_user':
        user_id = input("Digite o ID do usuário: ")
        if any(user['id'] == user_id for user in DB['users']):
            DB['users'] = [user for user in DB['users'] if user['id'] != user_id]
            print('Usuário apagado com sucesso!')
        else:
            print('Usuário não encontrado!')

    elif menu_option['code'] == 'login':
        while True:
            while True:
                email = input("Digite o email: ")
                if is_valid_email(email):
                    break
                print('Email inválido!')

            password = getpass("Digite a senha: ")

            for user in DB['users']:
                if user['email'] == email and user['password'] == password:
                    user_logged = user
                    break

            if user_logged:
                name = user_logged['name']
                print(f'\nBem vindo, {name}!')
                break
            else:
                print('Email ou senha inválidos!')

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

    input("\nPressione Enter para continuar...")
