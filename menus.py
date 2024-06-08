MAIN_MENU = {
    'title': 'Menu Principal',
    'options': [
        {
            'title': 'Gerenciar filmes',
            'code': 'films_menu',
            'roles': ['admin'],
            'need_auth': True,
            'need_no_auth': False
        },
        {
            'title': 'Gerenciar usuários',
            'code': 'users_menu',
            'roles': ['admin'],
            'need_auth': True,
            'need_no_auth': False
        },
        {
            'title': 'Listar filmes disponíveis',
            'code': 'index_available_film',
            'roles': ['client'],
            'need_auth': True,
            'need_no_auth': False
        },
        {
            'title': 'Comprar ingresso',
            'code': 'store_sale',
            'roles': ['client'],
            'need_auth': True,
            'need_no_auth': False
        },
        {
            'title': 'Listar ingressos comprados',
            'code': 'index_sale',
            'roles': ['client'],
            'need_auth': True,
            'need_no_auth': False
        },
        {
            'title': 'Listar ingressos vendidos',
            'code': 'index_sale',
            'roles': ['admin'],
            'need_auth': True,
            'need_no_auth': False
        },
        {
            'title': 'Login',
            'code': 'login',
            'roles': [],
            'need_auth': False,
            'need_no_auth': True
        },
        {
            'title': 'Criar conta',
            'code': 'store_user',
            'roles': [],
            'need_auth': False,
            'need_no_auth': True
        },
        {
            'title': 'Deslogar',
            'code': 'logout',
            'roles': [],
            'need_auth': True,
            'need_no_auth': False
        },
        {
            'title': 'Sair',
            'code': 'exit',
            'roles': [],
            'need_auth': False,
            'need_no_auth': False
        }
    ]
}

USER_MENU = {
    'title': 'Menu de Gerenciamento de Usuários',
    'options': [
        {
            'title': 'Listar usuários',
            'code': 'index_user',
            'roles': ['admin'],
            'need_auth': True,
            'need_no_auth': False
        },
        {
            'title': 'Cadastrar usuário',
            'code': 'store_user',
            'roles': ['admin'],
            'need_auth': True,
            'need_no_auth': False
        },
        {
            'title': 'Editar usuário',
            'code': 'update_user',
            'roles': ['admin'],
            'need_auth': True,
            'need_no_auth': False
        },
        {
            'title': 'Apagar usuário',
            'code': 'destroy_user',
            'roles': ['admin'],
            'need_auth': True,
            'need_no_auth': False
        },
        {
            'title': 'Voltar',
            'code': 'back',
            'roles': [],
            'need_auth': False,
            'need_no_auth': False
        }
    ]
}

FILM_MENU = {
    'title': 'Menu de Gerenciamento de Filmes',
    'options': [
        {
            'title': 'Listar filmes',
            'code': 'index_film',
            'roles': ['admin'],
            'need_auth': True,
            'need_no_auth': False
        },
        {
            'title': 'Listar os filmes mais vistos',
            'code': 'index_popular_film',
            'roles': ['admin'],
            'need_auth': True,
            'need_no_auth': False
        },
        {
            'title': 'Cadastrar filme',
            'code': 'store_film',
            'roles': ['admin'],
            'need_auth': True,
            'need_no_auth': False
        },
        {
            'title': 'Editar filme',
            'code': 'update_film',
            'roles': ['admin'],
            'need_auth': True,
            'need_no_auth': False
        },
        {
            'title': 'Apagar filme',
            'code': 'destroy_film',
            'roles': ['admin'],
            'need_auth': True,
            'need_no_auth': False
        },
        {
            'title': 'Voltar',
            'code': 'back',
            'roles': [],
            'need_auth': False,
            'need_no_auth': False
        }
    ]
}
