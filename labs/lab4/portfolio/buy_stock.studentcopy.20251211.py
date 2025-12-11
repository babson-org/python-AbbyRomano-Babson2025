

import prices as _prices
import time

def _find_position(self, sym):
    for p in self.positions:
        if p.get("sym") == sym:
            return p
    return None

def portfolio_buy_stock(self, sym: str, shares: float, price: float):
    """TODO:    
    - Validate sym in DOW30
         In the lab4 folder is a file prices.py.  Look at the file and find out what DOW30 is
         You can access DOW30 with _prices.DOW30 (see how we import prices above)
    - Validate shares > 0
    - Fetch last-close price via _prices.get_last_close_map([sym]) (use this price to buy shares)
    - Make sure the client has enough cash to make the purchase (price * shares)

    - IMPORTANT: in self.positions there should only be one dictionary per symbol

    - Add the purchase to an existing position or create a new position in self.positions 
    - Be sure to decrease the client cash attribute
    NOTE: UI prompts are handled in main.py: this method only prints for invalid ticker and insufficient funds. The rest are handled in main.py
    """
    #Make sure symbol is within stocks specified in dow30 file, otherwise reject request and return error
    if sym not in _prices.DOW30: 
        print(f'{sym} is not in the DOW30')
        return
    #If there are no shares, again reject request and return error 
    if shares <= 0: 
        print('There are no shares!')
        return
    #call last close price from price file and set it equal to a 'last close' variable
    last_close = _prices.get_last_close_map([sym])[sym]
    #now find the total cost by using the last cost variable above multiplied by number of shares requested 
    total_cost = last_close * shares
    #Make sure that client has enough cash to make purchase by comparing total cost variable to self.cash attribute
    if total_cost > self.cash: 
        print(f'Insufficient funds! You have ${self.cash}, but need ${total_cost}.')
        return 
    #call find position and set it equal to a variable pos to check if the positon in the client portfolio exists
    pos = _find_position(self, sym)
    #use an if else statement to see if position exists, if it doesnt, append new 'pos' dictionary to self.positions list
    if pos is None: 
        pos = {
            'sym': sym,
            'shares': shares,
            'cost': total_cost
        }
        self.positions.append(pos)
    #otherwise, if the position is already in clients portfolio just update the shares and cost values 
    else: 
        pos['shares'] += shares
        pos['cost'] += total_cost

    #Make sure to attribute for the cost of the purchase by deducting total cost from cash attribute 
    self.cash -= total_cost 
    
    return



