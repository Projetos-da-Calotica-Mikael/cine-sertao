from utils import clear
from file import generate_file

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
    content += '-' * 30 + '\n'
    return content

def find_sales_by_film_title(DB, film_title):
    film_id = None

    for film in DB['films']:
        if film['title'] == film_title:
            film_id = film['id']
            break

    if film_id is None:
        print("Nenhum filme encontrado com o título fornecido:", film_title)
        return []

    sales_for_film = []
    for sale in DB['sales']:
        if sale['film_id'] == film_id:
            sales_for_film.append(sale)

    if len(sales_for_film) == 0:
        print("Nenhuma venda encontrada com o título fornecido:", film_title)

    return sales_for_film

def print_sales(DB, user_logged):
    title = ''
    while True:
        print('-' * 30)
        sales = find_sales_by_film_title(DB, title) if title else DB['sales']
        for sale in sales:
            print(generate_sale_print(DB, user_logged, sale))
        title = input('\nDigite o título do filme que deseja buscar (pressione Enter para sair): ')
        if title == '':
            break
        clear()

def generate_sales_file(DB, user_logged):
    filename = 'ingressos-vendidos.txt' if user_logged['type'] == 'admin' else 'ingressos-comprados.txt'

    content = '-' * 30 + '\n'
    for sale in DB['sales']:
        content += generate_sale_print(DB, user_logged, sale)

    generate_file(filename, content)
