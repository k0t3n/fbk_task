from aiohttp import web

from app.models.request import Request


async def request_handler(request) -> web.Response:
    """
    Saves request data to db
    """
    headers = str(dict(request.headers))
    body = (await request.read()).decode("utf-8") if request.body_exists else None
    ip = request.remote
    request_db = await Request.create(body=body, headers=headers, ip=ip)

    return web.Response(text=f'Request {request_db.id} created')
