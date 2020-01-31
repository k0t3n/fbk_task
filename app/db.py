from gino.ext.aiohttp import Gino

db = Gino()


async def setup_tables(*args, **kwargs) -> None:
    """
    Initializes database tables from models
    """
    await db.gino.create_all()


def init_db(app):
    """
    Initializes Gino
    """
    db.init_app(app)
