from aiohttp import web
from gino.ext.aiohttp import Gino
from sqlalchemy.dialects import postgresql


async def handle(request):
    headers = str(dict(request.headers))

    body = (await request.read()).decode("utf-8") if request.body_exists else None
    ip = request.remote
    request_db = await Request.create(body=body, headers=headers, ip=ip)
    return web.Response(text=f'Request {request_db.id} created')


db = Gino()
app = web.Application(middlewares=[db])
app.add_routes([
    web.post('/', handle),
])

app['config'] = {'gino': {'dsn': 'postgresql://k0t3n@localhost/fbk_task'}}
db.init_app(app)


class Request(db.Model):
    __tablename__ = 'requests'

    id = db.Column(db.Integer(), primary_key=True)
    headers = db.Column(db.Unicode())
    body = db.Column(db.Unicode())
    ip = db.Column(postgresql.INET())


async def setup_tables(app) -> None:
    await db.gino.create_all()


app.on_startup.append(setup_tables)

if __name__ == '__main__':
    web.run_app(app)
