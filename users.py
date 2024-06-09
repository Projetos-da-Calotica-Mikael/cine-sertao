from getpass import getpass
from utils import is_valid_email, generate_id

def login(DB):
    user_logged = None
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

    return user_logged

def index_user(DB):
    print('-' * 30)
    for users in DB['users']:
        print(f"ID: {users['id']}")
        print(f"Nome: {users['name']}")
        print(f"Email: {users['email']}")
        print(f"Tipo: {users['type']}")
        print('-' * 30)

def store_user(DB, user_logged):
    new_user = {
        'id': generate_id(),
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

def update_user(DB, user_logged):
    user_id = input("Digite o ID do usuário: ")

    update_user = next((user for user in DB['users'] if user['id'] == user_id), None)

    if update_user == None:
        print('Usuário não encontrado!')
        getpass("\nPressione Enter para continuar...")
        return

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

def destroy_user(DB):
    user_id = input("Digite o ID do usuário: ")
    if any(user['id'] == user_id for user in DB['users']):
        DB['users'] = [user for user in DB['users'] if user['id'] != user_id]
        print('Usuário apagado com sucesso!')
    else:
        print('Usuário não encontrado!')
