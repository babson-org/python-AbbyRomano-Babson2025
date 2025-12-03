
class Stock:
    def __init__(self, sym, name, shares = 0.0, cost = 0.0):
        #Define attributes for each stock object to use in other portfolio files 
        self.sym = sym
        self.name = name
        self.shares = shares
        self.cost = cost        
        
    def __str__(self):
        """TODO: include symbol, shares, and cost (format flexible)."""
        return f"{self.shares} shares of {self.sym} at ${self.cost:,.2f}"
  
        