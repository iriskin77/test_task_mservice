from piccolo.conf.apps import AppRegistry
from piccolo.engine.postgres import PostgresEngine
from core.settings import POSTGRES_HOST, POSTGRES_DB, POSTGRES_PASSWORD, POSTGRES_PORT, POSTGRES_USER


DB = PostgresEngine(
    config={
        "database": POSTGRES_DB,
        "user": POSTGRES_USER,
        "password": POSTGRES_PASSWORD,
        "host": POSTGRES_HOST,
        "port": POSTGRES_PORT,
    }
)

APP_REGISTRY = AppRegistry(
    apps=[
        "models.piccolo_app",
    ]
)
