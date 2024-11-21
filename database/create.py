from database.models import active_models
from database.db_init import db


def create_tables() -> None:
    """Database models to tables"""
    with db:
        db.create_tables(active_models)
