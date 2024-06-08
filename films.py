def print_film(DB, film):
    print(f"ID: {film['id']}")
    print(f"Título: {film['title']}")
    print(f"Descrição: {film['description']}")
    print(f"Duração: {film['duration']} minutos")
    print(f"Gênero: {', '.join(film['genre'])}")
    print(f"Sala: {film['room_number']}")
    print(f"Horário: {film['time']}")
    total_sales = len([sale for sale in DB['sales'] if sale['film_id'] == film['id']])
    print(f"Assentos vendidos: {total_sales} de {film['capacity']}")
    print(f"Preço: R$ {film['price']:.2f}")
    print('-' * 30)

def filter_films_by_name(films, name):
    return [film for film in films if name.lower() in film['title'].lower()]

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
