from typing import Any
from src.db.main import get_db


def save(instance: Any) -> None:
    db = get_db()
    db.session.add(instance)
    db.session.commit()