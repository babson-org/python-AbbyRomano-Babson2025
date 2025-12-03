
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
    #Again use find position to see if symbol exists in clients portfolio
    pos = _find_position(self, sym)
    #if it doesnt, print error message 
    if pos is None: 
        print(f'No owned positions for {sym} found!')
        return
    #create a variable for owned shares by calling pos dictionary and using 'shares' key 
    owned = pos['shares']
    #if owner doesnt have enough shares to sell, print error message 
    if shares > owned: 
        print(f'Cannot sell {shares}. You only own {owned}!')
        return
    
    #create variable to get last close price from sample prices file 
    last_close = _prices.get_last_close_map([sym])[sym]
    #calculate how much money the client will get from selling shares by using last close price times shares 
    proceeds = last_close * shares
    #See how many shares are being sold by dividing shares variable by owned variable 
    sold = shares / owned 
    #use pos dictionary and 'cost' key and multiply by sold variable created to get cost reduction amount
    cost_reduction = pos['cost'] * sold 
    #update pos dictionary according to keys with new values after sale, so subtract shares and cost 
    pos['share'] -= shares
    pos['cost'] -= cost_reduction
    #use an if statement to see if shares are 0, if so append pos dictionary and remove the postion
    if pos['shares'] == 0:
        self.positions.remove(pos)
    #add proceeds from the sale to cash attribute 
    self.cash += proceeds 
    return 
