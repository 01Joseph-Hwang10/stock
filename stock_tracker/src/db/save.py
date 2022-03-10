from typing import Any
from stock_tracker.src.db.main import get_db


def save(instance: Any) -> None:
    db = get_db()
    db.session.add(instance)
    db.session.commit()