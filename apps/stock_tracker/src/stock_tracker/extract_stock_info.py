import requests
from typing import List, Tuple
from apps.shared.hooks.use_config import use_config, Config
from apps.shared.hooks.use_safe_request import use_safe_request
from apps.stock_tracker.src.stock_tracker.endpoints import NaverEndpoint

class EvaluatedStockInfo:
    current_price: int
    goal: List[int]
    bep: int
    code: str
    name: str
    market: str

    def __init__(self, source: dict) -> None:
        self.current_price = source['current_price']
        self.goal = source['goal']
        self.bep = source['bep']
        self.code = source['code']
        self.name = source['name']
        self.market = source['market']
    
    def met_goal(self) -> Tuple[bool, int]:
        self.goal.sort()
        reached_price = self.goal[0]
        if self.current_price < reached_price:
            return False, reached_price
        for goal in self.goal:
            if self.current_price < goal:
                break
        return True, reached_price
    
    def met_bep(self) -> Tuple[bool, int]:
        if self.current_price < self.bep:
            return False, self.bep
        return True, self.bep
    

def extract_stock_info() -> List[EvaluatedStockInfo]:
    config: Config = use_config()
    result: List[EvaluatedStockInfo] = []
    for target in config['target']:
        response = use_safe_request(requests.get(NaverEndpoint.stock_info(target['code'])))
        price = response['closePrice']
        result.append(EvaluatedStockInfo({
            'current_price': price,
            'goal': target['goal'],
            'bep': target['bep'],
            'code': target['code'],
            'name': target['name'],
            'market': target['market'],
        }))
    return result