print('=' * 10, 'BEM VINDO AO CINE SERTÃO', '=' * 10)

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
        'title': 'R1 - Gerenciar os filmes (ADM)',
        'key': '1',
        'roles': ['admin'],
        'need_auth': False
    },
    {
        'title': 'R2 - Comprar Ingressos (CLIENTE)',
        'key': '2',
        'roles': ['client'],
        'need_auth': False
    },
    {
        'title': 'R3 - Cadastrar usuário (ADM ou CLIENTE)',
        'key': '3',
        'roles': [],
        'need_auth': False
    },
    {
        'title': 'R9 - Deslogar',
        'key': '9',
        'roles': [],
        'need_auth': True
    },
    {
        'title': 'R0 - Sair',
        'key': '0',
        'roles': [],
        'need_auth': False
    }
]

user_logged = None

while True:
    print("\nMenu Principal")

    for item in MAIN_MENU:
        if (item['need_auth'] == True and user_logged == None):
            continue
        print(item['title'])

    key_pressed = input("\nEscolha uma opção: ")
    active_option = None

    for option in MAIN_MENU:
        if option['key'] == key_pressed:
            active_option = option

    if (active_option == None):
        print("Opção inválida.")
        continue

    if (len(active_option['roles'])):
        if (user_logged == None):
            print('\nPara acessar essa funcionalidade, por favor o faça login!')

            while True:
                email = input("\nDigite o email: ")
                while True:
                    if '@' in email and '.' in email.split('@')[-1]:
                        break
                    print('Email inválido!')
                    email = input("Digite o email: ")

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

        if user_logged['type'] not in active_option['roles']:
            print("Usuário não autorizado.")
            continue

    if key_pressed == "1":
        print("\nMenu de Gerenciamento de Filmes")
        print("R5 - Realizar o cadastro do filme")
        print("R6 - Buscar filme")
        print("R7 - Atualizar dados do filme")
        print("R8 - Remover filme")
        print("R9 - Tema Livre")
        print("R10 - Tema Livre")

    if key_pressed == "2":
        print("\nMenu de Compra de Ingressos")
        print("R11 - Efetuar a compra do ingresso de um filme")
        print("R12 - Tema livre")
        continue

    if key_pressed == "3":
        name = input("\nDigite o nome: ")

        email = input("Digite o email: ")
        while True:
            if '@' in email and '.' in email.split('@')[-1]:
                break
            print('Email inválido!')
            email = input("Digite o email: ")

        password = input("Digite a senha: ")

        user_type = input("Digite o tipo (admin ou client): ")
        while True:
            if user_type in DB['user_types']:
                break
            print('Tipo inválido!')
            user_type = input("Digite o tipo (admin ou client): ")

        DB['users'].append({
            'name': name,
            'email': email,
            'password': password,
            'type': user_type
        })
        print("Usuário cadastrado com sucesso!")
        continue

    if key_pressed == "9":
        name = user_logged['name']
        print(f'Até mais, {name}!')
        user_logged = None
        continue

    if key_pressed == "0":
        name = user_logged['name'] if user_logged != None else 'usuário anônimo'
        print(f'Até mais, {name}!')
        exit()
