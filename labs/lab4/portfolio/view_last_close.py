import prices as _prices

def portfolio_view_last_close(self):
    """
    Look at the prices.py file again.  _prices.get_last_close(symbols)
    takes a list of tickers and returns a dictionay whose keys are symbols 
    and values are last close

    create a list of tickers from positions and return the dictionary
    you get back from calling _prices.last_night_close(symbols)

    the main program does the rest!
    
    """
    #create symbols list by pulling each symbol from the positions dictionary
    syms = [pos['sym'] for pos in self.positions]
    #if there isnt a symbol, return an empty dictionary
    if not syms: 
        return {}
    #get last close prices using get_last_close_map function from prices 
    last_close_price = _prices.get_last_close_map(syms)
    return last_close_price

    
