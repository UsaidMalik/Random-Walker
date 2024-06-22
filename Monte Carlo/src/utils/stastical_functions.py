"""
Author: Usaid Malik
Date: 05/23/24
About: These are the expectation and variance
functions for this problem as well as the expected
distribution for this specific problem, derived
from the problem statement, it should be noted for now
these are only for the case where equal probability
is assumed
"""


def calc_expectation_L2_squared_norm(T: int, d:int = 0) -> int:
    return T


def calc_variance_L2_squared_norm(d:int, T:int) -> float:
    return T + (T**2 - 3*T)/(2*d) + (T**2*(d**2 - 3*d)/(2*d**2)) - T**2


def calc_expectation_vector_entry_squared(d:int, T:int) -> float:
    return T/d


def calc_variance_vector_entry_squared(d:int, T:int) -> float:
    return T/d + (T(T-1)/2 - T)/(d**2) - (T/d)**2


def calc_expectation_vector_entry(d:int = 0, T:int = 0) -> float:
    return 0 # this will be zero because of the values chosen and the equal probability


def calc_variance_vector_entry(T:int, d:int = 0) -> int:
    return T # this is the variance of a single entry
