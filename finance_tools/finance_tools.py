def add_tax(amount, rate):
    """
    Adds tax to subtotal amount

    Parameters:
    amount (float): subtotal of bill
    rate (float): tax rate applied

    Returns:
        float: Total Amount with Tax
    """
    return amount * (1 + rate)

def tip(amount, rate=0.15):
    """
    Adds tip to final bill
    
    Parameters:
        amount (float): amount of bill
        rate (float): 15% tip
        
    Return:
        float: Total with Tax and Tip
    """
    return amount * rate

def split_bill(amount, people):
    """
    Splits bill among all people
    
    Parameters:
        amount (float): amount of bill
        people (float): number of people to split
        
    Returns:
        float: Amount to pay, per person
    """
    return amount / people

def monthly_payment(principal, rate, months):
    """
    Total monthly payment

    Parameters:
        principal (float): Principal amount of bill
        rate (float): Amount added monthly via interest
        months (float): How many months to pay in full
    
    Return:
        float: Total monthly payment
    """
    return (principal * rate) / (1 - (1 + rate)**(-months))