import random

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
            'user_id': '1'
        },
          {
            'id': '2',
            'film_id': '1',
            'user_id': '2'
        }
    ],
}

MAIN_MENU = [
    {
        'title': 'Gerenciar usuários',
        'code': 'users_menu',
        'roles': ['admin'],
        'need_auth': True,
        'need_no_auth': False
    },
    {
        'title': 'Gerenciar filmes',
        'code': 'films_menu',
        'roles': ['admin'],
        'need_auth': True,
        'need_no_auth': False
    },
    {
        'title': 'Comprar ingresso',
        'code': 'store_sale',
        'roles': ['client'],
        'need_auth': True,
        'need_no_auth': False
    },
    {
        'title': 'Listar ingressos comprados',
        'code': 'index_sales',
        'roles': ['client'],
        'need_auth': True,
        'need_no_auth': False
    },
    {
        'title': 'Listar ingressos vendidos',
        'code': 'index_sales',
        'roles': ['admin'],
        'need_auth': True,
        'need_no_auth': False
    },
    {
        'title': 'Criar conta',
        'code': 'register_user',
        'roles': [],
        'need_auth': False,
        'need_no_auth': True
    },
    {
        'title': 'Login',
        'code': 'login',
        'roles': [],
        'need_auth': False,
        'need_no_auth': True
    },
    {
        'title': 'Deslogar',
        'code': 'logout',
        'roles': [],
        'need_auth': True,
        'need_no_auth': False
    },
    {
        'title': 'Sair',
        'code': 'exit',
        'roles': [],
        'need_auth': False,
        'need_no_auth': False
    }
]

USER_MENU = [
    {
        'title': 'Listar usuários',
        'code': 'index_user',
        'roles': ['admin'],
        'need_auth': True,
        'need_no_auth': False
    },
    {
        'title': 'Cadastrar usuário',
        'code': 'store_user',
        'roles': ['admin'],
        'need_auth': True,
        'need_no_auth': False
    },
    {
        'title': 'Editar usuário',
        'code': 'update_user',
        'roles': ['admin'],
        'need_auth': True,
        'need_no_auth': False
    },
    {
        'title': 'Apagar usuário',
        'code': 'destroy_user',
        'roles': ['admin'],
        'need_auth': True,
        'need_no_auth': False
    },
    {
        'title': 'Voltar',
        'code': 'back',
        'roles': [],
        'need_auth': False,
        'need_no_auth': False
    }
]

FILM_MENU = [
    {
        'title': 'Listar filmes',
        'code': 'index_film',
        'roles': ['admin'],
        'need_auth': True,
        'need_no_auth': False
    },
    {
        'title': 'Cadastrar filme',
        'code': 'store_film',
        'roles': ['admin'],
        'need_auth': True,
        'need_no_auth': False
    },
    {
        'title': 'Editar filme',
        'code': 'update_filme',
        'roles': ['admin'],
        'need_auth': True,
        'need_no_auth': False
    },
    {
        'title': 'Apagar filme',
        'code': 'destroy_film',
        'roles': ['admin'],
        'need_auth': True,
        'need_no_auth': False
    },
    {
        'title': 'Voltar',
        'code': 'back',
        'roles': [],
        'need_auth': False,
        'need_no_auth': False
    }
]

user_logged = None

while True:
    print('\033c========== BEM VINDO AO CINE SERTÃO ==========')

    if (user_logged):
        print(f"\nOlá, {user_logged['name']}!")

    print("\n* Menu Principal")

    main_menu_valid_options = []

    for option in MAIN_MENU:
        if user_logged == None:
            if (option['need_auth'] == True or len(option['roles'])):
                continue
        else:
            if (option['need_no_auth'] == True or (len(option['roles']) and user_logged['type'] not in option['roles'])):
                continue
        main_menu_valid_options.append(option)
        print(f"{len(main_menu_valid_options)}. {option['title']}")

    main_menu_index = input("\nEscolha uma opção: ")

    if (not main_menu_index.isdigit() or
        int(main_menu_index) < 1 or
        int(main_menu_index) > len(main_menu_valid_options)
    ):
        input("Opção inválida.\n\nPressione Enter para continuar...")
        continue

    main_menu_option = main_menu_valid_options[int(main_menu_index) - 1]

    print('')

    if main_menu_option['code'] == 'films_menu':
        print("* Menu de Gerenciamento de Filmes")
        print(FILM_MENU)

    elif main_menu_option['code'] == 'users_menu':
        print("* Menu de Gerenciamento de Usuários")
        print(USER_MENU)

    elif main_menu_option['code'] == 'store_sale':
        print("TODO: Listar filmes e permitir a compra de ingressos")

    elif main_menu_option['code'] == 'index_sales':
        print('-' * 20)
        for sale in DB['sales']:
            film = next((film for film in DB['films'] if film['id'] == sale['film_id']), None)
            if (user_logged['type'] == 'admin'):
                user = next((user for user in DB['users'] if user['id'] == sale['user_id']), None)
                print(f"Venda: {sale['id']}")
                print(f"Usuário: {user['name']}")
            else:
                if user_logged['id'] != sale['user_id']:
                    continue
            print(f"Filme: {film['title']}")
            print(f"Descrição: {film['description']}")
            print(f"Duração: {film['duration']} minutos")
            print(f"Gênero: {', '.join(film['genre'])}")
            print(f"Sala: {film['room_number']}")
            print(f"Horário: {film['time']}")
            total_sales = len([sale for sale in DB['sales'] if sale['film_id'] == film['id']])
            print(f"Assentos vendidos: {total_sales} de {film['capacity']}")
            print(f"Preço: R$ {film['price']:.2f}")
            print('-' * 20)

    elif main_menu_option['code'] == 'register_user':
        name = input("Digite o nome: ")

        while True:
            email = input("Digite o email: ")

            if '@' not in email or '.' not in email.split('@')[-1]:
                print('Email inválido!')
            elif any(user['email'] == email for user in DB['users']):
                print('Email já cadastrado!')
            else:
                break

        password = input("Digite a senha: ")

        user_type = 'client'

        if user_logged and user_logged['type'] == 'admin':
            while True:
                user_type = input("Digite o tipo (admin ou client): ")
                if user_type in DB['user_types']:
                    break
                print('Tipo inválido!')

        DB['users'].append({
            'id': str(random.random()),
            'name': name,
            'email': email,
            'password': password,
            'type': user_type
        })

        print('Usuário cadastrado com sucesso!')

    elif main_menu_option['code'] == 'login':
        while True:
            while True:
                email = input("Digite o email: ")
                if '@' in email and '.' in email.split('@')[-1]:
                    break
                print('Email inválido!')

            password = input("Digite a senha: ")

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

    elif main_menu_option['code'] == 'logout':
        print(f"Até mais, {user_logged['name']}!")
        user_logged = None

    elif main_menu_option['code'] == 'exit':
        name = 'usuário anônimo' if user_logged == None else user_logged['name']
        print(f'Até mais, {name}!')
        exit()

    input("\nPressione Enter para continuar...")
