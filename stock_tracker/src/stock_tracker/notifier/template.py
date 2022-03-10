from stock_tracker.src.stock_tracker.extract_stock_info import EvaluatedStockInfo
from stock_tracker.src.stock_tracker.notifier.decide_case import decide_case

def get_template():
    template = """[주가 <Price-Status> 알림]

<Item-Name> 주의 가격이 <Price-Status-Detail> 하여 <Description>
"""
    return template

PRICE_STATUS = '<Price-Status>'
ITEM_NAME = '<Item-Name>'
PRICE_STATUS_DETAIL = '<Price-Status-Detail>'
DESCRIPTION = '<Description>'

def create_template(stock_info: EvaluatedStockInfo):
    template = get_template()
    case, current_price = decide_case()
    _, met_goal = stock_info.met_goal()
    _, met_bep = stock_info.met_bep()
    if case == 0:
        template = template.replace(PRICE_STATUS, '경고')
        template = template.replace(PRICE_STATUS_DETAIL, '하강하여')
        template = template.replace(DESCRIPTION, '현재 %d원입니다. 손익분기점과 %d원 만큼 차이가 납니다.' % (current_price, met_bep - current_price))
        return template
    if case == 1:
        template = template.replace(PRICE_STATUS, 'BEP 기점')
        template = template.replace(PRICE_STATUS_DETAIL, '상승하여')
        template = template.replace(DESCRIPTION, '현재 손익분기점보다 %d원 위인 %d원입니다.' % (current_price - met_bep, current_price))
        return template
    if case == 2:
        template = template.replace(PRICE_STATUS, '하강')
        template = template.replace(PRICE_STATUS_DETAIL, '하강하여')
        template = template.replace(DESCRIPTION, '현재 %d원입니다. (목표 주가 %d원입니다.)' % (current_price, met_goal))
        return template
    if case == 3:
        template = template.replace(PRICE_STATUS, '상승')
        template = template.replace(PRICE_STATUS_DETAIL, '상승하여')
        template = template.replace(DESCRIPTION, '현재 %d원입니다. (목표 주가 %d원입니다.)' % (current_price, met_goal))
        return template
    template = template.replace(PRICE_STATUS, '유지')
    template = template.replace(PRICE_STATUS_DETAIL, '그대로 유지하여')
    template = template.replace(DESCRIPTION, '현재 %d원입니다. (목표 주가 %d원입니다.)' % (current_price, met_goal))
    return template
