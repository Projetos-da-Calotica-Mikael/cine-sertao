from getpass import getpass
from utils import clear, generate_id

def print_film(DB, film):
    print(f"ID: {film['id']}")
    print(f"Título: {film['title']}")
    print(f"Descrição: {film['description']}")
    print(f"Duração: {film['duration']} minutos")
    print(f"Gênero: {', '.join(film['genre'])}")
    print(f"Sala: {film['room_number']}")
    print(f"Horário: {film['time']}")
    print(f"Assentos disponíveis: {film['capacity']}")
    total_sales = len([sale for sale in DB['sales'] if sale['film_id'] == film['id']])
    print(f"Assentos vendidos: {total_sales} de {film['capacity']}")
    print(f"Preço: R$ {film['price']:.2f}")
    print('-' * 30)

def filter_films_by_title(films, title):
    films = [film for film in films if title.lower() in film['title'].lower()]
    if len(films) == 0:
        print("Nenhum filme encontrado com o título fornecido:", title)
    return films

def most_sale_films(DB):
    film_sales = {}

    for sale in DB['sales']:
        film_id = sale['film_id']
        if film_id in film_sales:
            film_sales[film_id] += 1
        else:
            film_sales[film_id] = 1

    sorted_films = sorted(DB['films'], key=lambda film: film_sales.get(film['id'], 0), reverse=True)

    return sorted_films

def filter_films_available(DB):
    available_films_list = []
    for film in DB['films']:
        total_sales = len([sale for sale in DB['sales'] if sale['film_id'] == film['id']])
        available_seats = film['capacity'] - total_sales
        if available_seats > 0:
            available_films_list.append(film)
    return available_films_list

def index_film(DB):
    title = ''
    while True:
        print('-' * 30)
        films = filter_films_by_title(DB['films'], title)
        for film in films:
            print_film(DB, film)
        title = input('\nDigite o título do filme que deseja buscar (pressione Enter para sair): ')
        if title == '':
            break
        clear()

def index_popular_film(DB):
    title = ''
    while True:
        print('-' * 30)
        films = filter_films_by_title(most_sale_films(DB), title)
        for film in films:
            print_film(DB, film)
        title = input('\nDigite o título do filme que deseja buscar (pressione Enter para sair): ')
        if title == '':
            break
        clear()

def store_film(DB):
    new_film = {
        'id': generate_id()
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

def index_available_film(DB):
    title = ''
    while True:
        print('-' * 30)
        films = filter_films_by_title(filter_films_available(DB), title)
        for film in films:
            print_film(DB, film)
        title = input('\nDigite o título do filme que deseja buscar (pressione Enter para sair): ')
        if title == '':
            break
        clear()

def destroy_film(DB):
    film_id = input("Digite o ID do filme: ")
    if any(film['id'] == film_id for film in DB['films']):
        DB['films'] = [film for film in DB['films'] if film['id'] != film_id]
        print('Filme apagado com sucesso!')
    else:
        print('Filme não encontrado!')

def update_film(DB):
    film_id = input("Digite o ID do filme: ")

    update_film = next((film for film in DB['films'] if film['id'] == film_id), None)

    if update_film == None:
        print('Filme não encontrado!')
        getpass("\nPressione Enter para continuar...")
        return

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
