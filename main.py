DB = {
    'user_types': ['admin', 'client'],
    'users': [
        {
            'name': 'Admin',
            'email': 'admin@admin.com',
            'password': 'admin',
            'type': 'admin'
        },
        {
            'name': 'Cliente',
            'email': 'client@client.com',
            'password': 'client',
            'type': 'client'
        }
    ],
    'films': [],
}

MAIN_MENU = [
    {
        'title': 'Gerenciar os filmes',
        'code': 'manage_films',
        'roles': ['admin'],
        'need_auth': True,
        'need_no_auth': False
    },
    {
        'title': 'Comprar Ingressos',
        'code': 'buy_tickets',
        'roles': ['client'],
        'need_auth': True,
        'need_no_auth': False
    },
    {
        'title': 'Cadastrar usuário',
        'code': 'register_user',
        'roles': ['admin', 'client'],
        'need_auth': False,
        'need_no_auth': False
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

user_logged = None

while True:
    print('\033c')

    print('=' * 10, f'BEM VINDO AO CINE SERTÃO', '=' * 10)

    if (user_logged):
        print(f"\nOlá {user_logged['name']}!")

    print("\n* Menu Principal")

    main_menu_valid_options = []

    for option in MAIN_MENU:
        if user_logged == None:
            if (option['need_auth'] == True or len(option['roles'])):
                continue
        else:
            if option['need_no_auth'] == True:
                continue
            if (len(option['roles']) and user_logged['type'] not in option['roles']):
                continue

        main_menu_valid_options.append(option)
        print(f"{len(main_menu_valid_options)}. {option['title']}")

    main_menu_index = input("\nEscolha uma opção: ")

    if (not main_menu_index.isdigit()):
        print("Opção inválida.")
        input("\nPressione Enter para continuar...")
        continue

    if (int(main_menu_index) < 1 or int(main_menu_index) > len(main_menu_valid_options)):
        print("Opção inválida.")
        input("\nPressione Enter para continuar...")
        continue

    main_menu_option = main_menu_valid_options[int(main_menu_index) - 1]

    print('')

    if main_menu_option['code'] == 'manage_films':
        print("Menu de Gerenciamento de Filmes")
        print("R5 - Realizar o cadastro do filme")
        print("R6 - Buscar filme")
        print("R7 - Atualizar dados do filme")
        print("R8 - Remover filme")
        print("R9 - Tema Livre")
        print("R10 - Tema Livre")

    elif main_menu_option['code'] == 'buy_tickets':
        print("Menu de Compra de Ingressos")
        print("R11 - Efetuar a compra do ingresso de um filme")
        print("R12 - Tema livre")

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
                print('Usuário ou senha inválidos!')

    elif main_menu_option['code'] == 'logout':
        print(f"Até mais, {user_logged['name']}!")
        user_logged = None

    elif main_menu_option['code'] == 'exit':
        name = 'usuário anônimo' if user_logged == None else user_logged['name']
        print(f'Até mais, {name}!')
        exit()

    input("\nPressione Enter para continuar...")
