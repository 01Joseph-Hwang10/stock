
"""
Naver Finance API Endpoints
"""
from typing import Tuple


class NaverEndpoint:

    @staticmethod
    def stock_detail_info(stock_code: str) -> str:
        return f'https://m.stock.naver.com/api/stock/{stock_code}/integration'

    @staticmethod
    def stock_info(stock_code: str) -> str:
        return f'https://m.stock.naver.com/api/stock/{stock_code}/basic'
    
    @staticmethod
    def stock_page(stock_code: str) -> str:
        return f'https://m.stock.naver.com/domestic/stock/{stock_code}/total'

"""
Kakao API Endpoints
"""
class KakaoEndpoint:

    """
        @param {str} content - 카카오톡 메시지. 200자 이하.
        @param {str} button_url - 카카오톡에서 메세지를 누르면 이동할 주소
        @param {str} button_title - 버튼의 타이틀
    """
    @staticmethod
    def send(content: str, button_url: str, button_title: str) -> Tuple[str, dict]:
        template_object = {
            "object_type": "text",
            "text": content,
            "link": {
                "web_url": button_url,
                "mobile_web_url": button_url,
            },
            "button_title": button_title
        }
        return 'https://kapi.kakao.com/v2/api/talk/memo/default/send', template_object