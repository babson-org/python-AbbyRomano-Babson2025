import time
def portfolio_withdraw_cash(self, amount: float):
    """TODO:
    - Reject negative
    - Reject if amount > cash
    - Otherwise subtract from self.cash
    """
    #use if else statements 
    #check for negative amount first 
    if amount < 0:
        print("You can not withdraw negative ")
    #Check to see if cash on hand is less than the amount requested 
    elif amount > self.cash:
        print(f"you only have ${self.cash:,.2f}, sell some stock first!")
    #Otherwise, subtract the amount requested from cash attribute   
    else:
        self.cash -= amount
        print(f"Your check for 4{amount:,.2f} is in the mail")

    return None
        