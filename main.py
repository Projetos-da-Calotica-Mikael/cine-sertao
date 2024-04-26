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
        'title': 'Gerenciar os filmes (ADM)',
        'key': '1',
        'roles': ['admin'],
        'need_auth': False
    },
    {
        'title': 'Comprar Ingressos (CLIENTE)',
        'key': '2',
        'roles': ['client'],
        'need_auth': False
    },
    {
        'title': 'Cadastrar usuário (ADM ou CLIENTE)',
        'key': '3',
        'roles': [],
        'need_auth': False
    },
    {
        'title': 'Deslogar',
        'key': '9',
        'roles': [],
        'need_auth': True
    },
    {
        'title': 'Sair',
        'key': '0',
        'roles': [],
        'need_auth': False
    }
]

user_logged = None

while True:
    print("\033c")
    print('=' * 10, 'BEM VINDO AO CINE SERTÃO', '=' * 10)

    print("\n* Menu Principal")
    for option in MAIN_MENU:
        if (option['need_auth'] == True and user_logged == None):
            continue
        print(f"[{option['key']}] - {option['title']}")

    main_menu_key = input("\nEscolha uma opção: ")
    main_menu_option = None

    for option in MAIN_MENU:
        if option['key'] == main_menu_key:
            main_menu_option = option

    if main_menu_option == None:
        print("Opção inválida.")
        continue

    if option['need_auth'] == True or len(main_menu_option['roles']):
        if (user_logged == None):
            print('\nPara acessar essa funcionalidade, por favor o faça login!')

            while True:
                while True:
                    email = input("\nDigite o email: ")
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
                    print(f'Bem vindo, {name}!')
                    break
                else:
                    print('Usuário ou senha inválidos!')

        if user_logged['type'] not in main_menu_option['roles']:
            print("Usuário não autorizado.")
            continue

    if main_menu_key == "1":
        print("\nMenu de Gerenciamento de Filmes")
        print("R5 - Realizar o cadastro do filme")
        print("R6 - Buscar filme")
        print("R7 - Atualizar dados do filme")
        print("R8 - Remover filme")
        print("R9 - Tema Livre")
        print("R10 - Tema Livre")

    elif main_menu_key == "2":
        print("\nMenu de Compra de Ingressos")
        print("R11 - Efetuar a compra do ingresso de um filme")
        print("R12 - Tema livre")

    elif main_menu_key == "3":
        name = input("\nDigite o nome: ")

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

    elif main_menu_key == "9":
        print(f"Até mais, {user_logged['name']}!")
        user_logged = None

    elif main_menu_key == "0":
        name = 'usuário anônimo' if user_logged == None else user_logged['name']
        print(f'Até mais, {name}!')
        exit()

    print("\nPressione Enter para continuar...")
    input()
