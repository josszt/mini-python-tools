def shout(text):
    """
    Capitlize all letters, as if shouting

    Parameters: 
        text (float): any letters
    
    Returns:
        float: All letters capitlized
    """
    return text.upper()

def reverse(text):
    """
    Write the text backwards
    
    Parameters:
        text (float): all letters and words
    
     Returns:
        float: All text written in reverse
    """
    return text[::-1]

def count_words(text):
    """
    Count the words in the statement
    
    Parameters:
        text.split() (float): all words in statement
    
    Returns:
        float: The number of words in the statement is
    """
    return len(text.split())