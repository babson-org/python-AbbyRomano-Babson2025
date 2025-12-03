from portfolio import Portfolio 
def portfolio_str(self):
    """TODO: return a readable summary string. self is a Portfolio
    Example (format is flexible):
        "Bob has 2 positions and $1,234.56"
    """

    num_pos = len(self.positions)
    return f'{self.name} has {num_pos} and ${self.cash:,.2f}'

 
