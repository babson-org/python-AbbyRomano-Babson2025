from portfolio import Portfolio 
def portfolio_str(self):
    """TODO: return a readable summary string. self is a Portfolio
    Example (format is flexible):
        "Bob has 2 positions and $1,234.56"
    """
    #create variable to count number of positions by using the len() function to count items on a list
    num_pos = len(self.positions)
    #return f' string formatted to include name, number of positions and how much cash client has 
    return f'{self.name} has {num_pos} and ${self.cash:,.2f}'

 
