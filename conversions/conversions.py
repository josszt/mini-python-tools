def c_to_f(c):
    """
    Converts Celsius temperature to Farenheit.

    Parameters:
        celsius (float): Temperature in Celsius

    Returns:
        float: Temperature in Farenheit
    """
    return (c * 9/5) + 32

def f_to_c(f):
    """
    Converts Farenheit temperature to Celsius
    
    Parameters:
        celsius (float): Temperature in Farenheit
        
    Returns:
        float: Temperature in Celsius
    """
    return (f - 32) * 5/9

def km_to_miles(km):
    """
    Converts Kilometers to Miles

    Parameters:
        miles (float): Distance in Kilometers
    
    Returns:
        float: Distance in Miles
    """
    return km * 0.621371

def miles_to_km(mi):
    """
    Converts Miles to Kilometers

    Parameters:
        kilometers (float): Distance in Miles
    
    Returns:
        float: Distance in Kilometers
    """
    return mi * 1.609344

def L_to_gal(L):
    """
    Converts Litres to Gallons (US)

    Parameters:
        gallons (float): Volume in Gallons (US)
    
    Returns:
        float: Gallons
    """
    return L * 0.2641729

def gal_to_L(gal):
    """
    Converts Gallons (US) to Litres

    Parameters:
        litres (float): Volume in L
    
    Returns:
        float: Litres
    """
    return gal * 3.7854
