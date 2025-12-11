
import time
def portfolio_add_cash(self, amount: float):
 
    """TODO:
    - Reject negative amounts
    - Otherwise add to self.cash
    - Print message showing how much cash added and what you new cash balance is
    - return not needed
    """
#If amount is less than 0, reject 'deposit'
    if amount < 0:
        print('Cannot be a negative amount!')
        return 
#Otherwise, use self to call cash attribute, add amount specified by user, and print amount added and new balance by using attributes 
    self.cash += amount
    print(f'Added ${amount:.2f} cash. New balance is ${self.cash:.2f}.')
    
    