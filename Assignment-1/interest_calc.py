"""Saved the function as a module in a different python file as given in question 7 of Assignment 1"""

def calculate_compound_interest(principal, rate, time):
    """ Solution to 7th question """

    amount = principal * (1 + (rate/100)) ** time
    compound_interest = amount - principal
    return compound_interest