import requests
from stock_tracker.src.stock_tracker.extract_stock_info import EvaluatedStockInfo
from stock_tracker.src.stock_tracker.notifier.template import create_template
from stock_tracker.src.stock_tracker.extract_stock_info import extract_stock_info
from stock_tracker.src.stock_tracker.endpoints import KakaoEndpoint, NaverEndpoint
from stock_tracker.src.hooks.use_config import use_config, Config
from stock_tracker.src.hooks.use_safe_request import use_safe_request

def notify(stock_info: EvaluatedStockInfo) -> None:
    template = create_template(stock_info)
    config: Config = use_config()
    headers = {
        'Authorization': config['credentials']['kakaoAuthorization'],
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    use_safe_request(requests.get(KakaoEndpoint.send(template, NaverEndpoint.stock_page(stock_info.code), '주가 정보 확인'), headers=headers))
    

def notify_all() -> None:
    stock_infos = extract_stock_info()
    for stock_info in stock_infos:
        notify(stock_info)
