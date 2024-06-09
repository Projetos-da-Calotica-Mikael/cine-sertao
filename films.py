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
