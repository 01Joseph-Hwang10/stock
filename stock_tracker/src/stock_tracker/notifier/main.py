import requests
from stock_tracker.src.stock_tracker.extract_stock_info import EvaluatedStockInfo
from stock_tracker.src.stock_tracker.notifier.template import create_template, decide_case
from stock_tracker.src.stock_tracker.extract_stock_info import extract_stock_info
from stock_tracker.src.stock_tracker.endpoints import KakaoEndpoint, NaverEndpoint
from shared.hooks.use_config import use_config
from shared.hooks.use_safe_request import use_safe_request

def _notify(stock_info: EvaluatedStockInfo) -> None:
    template = create_template(stock_info)
    config = use_config()
    headers = {
        'Authorization': config['credentials']['kakaoAuthorization'],
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    url, template_object = KakaoEndpoint.send(template, NaverEndpoint.stock_page(stock_info.code), '주가 정보 확인')
    response = use_safe_request(requests.post(url, data=template_object, headers=headers))
    print('Message sent with status code : %s' % response.status_code)    

def notify(stock_info: EvaluatedStockInfo) -> None:
    case, _ = decide_case(stock_info)
    if case == 4: # No change to notify
        return
    _notify(stock_info)
    

def notify_all() -> None:
    stock_infos = extract_stock_info()
    for stock_info in stock_infos:
        notify(stock_info)
