import os

from aiohttp import web

from .db import init_db, setup_tables
from .views import request_handler

app = web.Application()

app['config'] = {
    'gino': {
        'host': os.getenv('POSTGRES_HOST', 'localhost'),
        'user': os.getenv('POSTGRES_USER', 'postgres'),
        'password': os.getenv('POSTGRES_PASSWORD'),
        'database': os.getenv('POSTGRES_DB', 'fbk_task'),
    }
}

init_db(app)

app.add_routes([
    # only POST requests are allowed, see deploy/nginx/nginx.conf:13
    web.post('/', request_handler),
])

app.on_startup.append(setup_tables)

if __name__ == '__main__':
    web.run_app(app)
