from typing import Tuple
from stock_tracker.src.stock_tracker.extract_stock_info import EvaluatedStockInfo
from stock_tracker.src.db.models.stock import Stock, Market
from stock_tracker.src.db.save import save

"""
Example:
[ 'a' , 'b' , 'c' , 'd' ]
 0    1     2     3    4
"""
def compute_range_index(stock_info: EvaluatedStockInfo) -> int:
    current_price = stock_info.current_price
    goals = stock_info.goal
    len_goals = range(len(goals))
    for i in len_goals:
        goal = goals[i]
        if current_price < goal:
            return i
    return len_goals + 1

"""
Returns [case, price]
Cases :
0: under_bep (Bearish)
1: over_bep (Bullish)
2: met_goal (Bearish)
3: met_goal (Bullish)
4: No change to notify
"""
def decide_case(stock_info: EvaluatedStockInfo) -> Tuple[int, int]:
    instance = Stock.query.filter_by(code=stock_info.code, market=Market.code_of(stock_info.market)).first()
    range_index = compute_range_index(stock_info)
    met_bep, _ = stock_info.met_bep()
    current_price = stock_info.current_price
    # Case 0 : Under BEP (Bearish)
    if current_price < met_bep and instance.range_index != -1:
        instance.range_index = -1
        save(instance)
        return 0, current_price
    # Case 1 : Over BEP (Bullish)
    if current_price >= met_bep and instance.range_index == -1:
        instance.range_index = range_index
        save(instance)
        return 1, current_price
    met_goal, _ = stock_info.met_goal()
    # Case 2 : Met Goal (Bearish)
    if met_goal and range_index < instance.range_index:
        instance.range_index = range_index
        save(instance)
        return 2, current_price
    # Case 3 : Met Goal (Bullish)
    if met_goal and range_index > instance.range_index:
        instance.range_index = range_index
        save(instance)
        return 3, current_price
    # Case 4 : No change to notify
    return 4, current_price
