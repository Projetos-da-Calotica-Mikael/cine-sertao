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

def print_sales(DB, user_logged):
    print('-' * 30)
    for sale in DB['sales']:
        print(generate_sale_print(DB, user_logged, sale))

def generate_sales_file(DB, user_logged):
    filename = 'ingressos-vendidos.txt' if user_logged['type'] == 'admin' else 'ingressos-comprados.txt'

    content = '-' * 30 + '\n'
    for sale in DB['sales']:
        content += generate_sale_print(DB, user_logged, sale)

    generate_file(filename, content)
