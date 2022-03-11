from flask_testing import TestCase
from stock_tracker.src.app import init_app_dev
from stock_tracker.src.db.main import get_db
from stock_tracker.src.stock_tracker.notifier.main import _notify
from stock_tracker.src.stock_tracker.extract_stock_info import extract_stock_info

class Notify(TestCase):

    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True

    def create_app(self):

        app = init_app_dev()
        app.config['TESTING'] = True
        self.db = get_db()
        return app

    def test_notify(self):
        stock_infos = extract_stock_info()
        for stock_info in stock_infos:
            _notify(stock_info)

    def setUp(self):

        self.db.create_all()

    def tearDown(self):

        self.db.session.remove()
        self.db.drop_all()
