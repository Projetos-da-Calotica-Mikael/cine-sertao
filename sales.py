from utils import clear, generate_id
from file import generate_file
from films import filter_films_available, print_film

def generate_sale_print(DB, user_logged, sale):
    content = ""
    film = next((film for film in DB['films'] if film['id'] == sale['film_id']), None)
    if (user_logged['type'] == 'admin'):
        user = next((user for user in DB['users'] if user['id'] == sale['user_id']), None)
        content = f"Venda ID: {sale['id']}\n"
        content += f"Usuário ID: {sale['user_id']}\n"
        if user:
            content += f"Usuário: {user['name']}\n"
        else:
            content += "Usuário não encontrado\n"
        content += f"Filme ID: {sale['film_id']}\n"
    else:
        if user_logged['id'] != sale['user_id']:
            return ''
    if film:
        content += f"Filme: {film['title']}\n"
        content += f"Descrição: {film['description']}\n"
        content += f"Duração: {film['duration']} minutos\n"
        content += f"Gênero: {', '.join(film['genre'])}\n"
        content += f"Sala: {film['room_number']}\n"
        content += f"Horário: {film['time']}\n"
        total_sales = len([sale for sale in DB['sales'] if sale['film_id'] == film['id']])
        content += f"Assentos vendidos: {total_sales} de {film['capacity']}\n"
        content += f"Preço: R$ {film['price']:.2f}\n"
    else:
        content += "Filme não encontrado\n"
    content += '-' * 30
    return content

def find_sales_by_film_identifier(DB, identifier):
    sales_for_film = []

    for film in DB['films']:
        if film['id'] == identifier:
            film_id = identifier
            break
    else:
        for film in DB['films']:
            if film['title'].lower() == identifier.lower():
                film_id = film['id']
                break
        else:
            print("Nenhum filme encontrado com o título ou ID fornecido:", identifier)
            return []

    for sale in DB['sales']:
        if sale['film_id'] == film_id:
            sales_for_film.append(sale)

    if len(sales_for_film) == 0:
        print("Nenhuma venda encontrada para o filme com título ou ID:", identifier)

    return sales_for_film

def print_sales(DB, user_logged):
    title = ''
    while True:
        print('-' * 30)
        sales = find_sales_by_film_identifier(DB, title) if title else DB['sales']
        for sale in sales:
            print(generate_sale_print(DB, user_logged, sale))
        title = input('\nDigite o título ou id do filme que deseja buscar (pressione Enter para sair): ')
        if title == '':
            break
        clear()

def generate_sales_file(DB, user_logged):
    filename = 'ingressos-vendidos.txt' if user_logged['type'] == 'admin' else 'ingressos-comprados.txt'

    film_id = input('Digite o título ou ID do filme que deseja buscar (pressione Enter para todos): ')

    content = '-' * 30 + '\n'
    sales = find_sales_by_film_identifier(DB, film_id) if film_id else DB['sales']
    for sale in sales:
        content += generate_sale_print(DB, user_logged, sale)

    generate_file(filename, content)

def store_sale(DB, user_logged):
    print('-' * 30)

    available_films = filter_films_available(DB)

    for film in available_films:
        print_film(DB, film)

    if len(available_films) > 0:
        film_id = input("\nDigite o ID do filme que deseja comprar: ")
        film = next((film for film in DB['films'] if film['id'] == film_id), None)
        if film:
            new_sale = {
                'id': generate_id(),
                'film_id': film_id,
                'user_id': user_logged['id']
            }
            DB['sales'].append(new_sale)
            print('Ingresso comprado com sucesso!')
        else:
            print('Filme não encontrado!')
    else:
        print("Desculpe, não há filmes disponíveis para venda no momento.")
