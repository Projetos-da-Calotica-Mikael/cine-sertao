def print_film(db, film):
    print(f"ID: {film['id']}")
    print(f"Filme: {film['title']}")
    print(f"Descrição: {film['description']}")
    print(f"Duração: {film['duration']} minutos")
    print(f"Gênero: {', '.join(film['genre'])}")
    print(f"Sala: {film['room_number']}")
    print(f"Horário: {film['time']}")
    total_sales = len([sale for sale in db['sales'] if sale['film_id'] == film['id']])
    print(f"Assentos vendidos: {total_sales} de {film['capacity']}")
    print(f"Preço: R$ {film['price']:.2f}")
    print('-' * 30)

def most_sale_films(db):
    film_sales = {}

    for sale in db['sales']:
        film_id = sale['film_id']
        if film_id in film_sales:
            film_sales[film_id] += 1
        else:
            film_sales[film_id] = 1

    sorted_films = sorted(db['films'], key=lambda film: film_sales.get(film['id'], 0), reverse=True)

    return sorted_films
