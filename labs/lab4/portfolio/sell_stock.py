
import time
import prices as _prices

def _find_position(self, sym):
    for p in self.positions:
        if p.get("sym") == sym:
            return p
    return None

def portfolio_sell_stock(self, sym: str, shares: float, price: float):
    """TODO:
    - Ensure symbol exists (use _find_position())
    - Ensure shares <= owned
    - Fetch last-close price via _prices.get_last_close_map([sym]) (use this price to sell shares)
    - Reduce position shares; adjust  'cost' proportionally by shares. (assumes average cost accounting)
    - Remove the position if shares drop to 0
    - Increase self.cash by proceeds
    - Hint: the amount you reduce cost is NOT the same as the amount you increase cash
    """
    
    pos = _find_position(self, sym)
    if pos is None: 
        print(f'No owned positions for {sym} found!')
        return
    
    owned = pos['shares']
    if shares > owned: 
        print(f'Cannot sell {shares}. You only own {owned}!')
        return 
    
    last_close = _prices.get_last_close_map([sym])[sym]
    proceeds = last_close * shares
    sold = shares / owned 

    cost_reduction = pos['cost'] * sold 
    pos['share'] -= shares
    pos['cost'] -= cost_reduction

    if pos['shares'] == 0:
        self.positions.remove(pos)
    
    self.cash += proceeds 
    return 
