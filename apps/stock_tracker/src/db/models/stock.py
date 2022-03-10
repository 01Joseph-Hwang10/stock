from apps.stock_tracker.src.db.main import db

class Market:
    KOSPI = 0
    KOSDAQ = 1

    @staticmethod
    def code_of(str_code: str) -> int:
        if str_code == 'KOSPI':
            return 0
        if str_code == 'KOSDAQ':
            return 1
        return -1

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(6), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    market = db.Column(db.Integer, nullable=False)
    range_index = db.Column(db.Integer, nullable=False)
