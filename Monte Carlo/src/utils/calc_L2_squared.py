"""
Author: Usaid malik
Date: 05/23/2024
About: Utility function to calculate the L2 norm squared of a 
vector. Used in conjunction with the Monte Carlo simulations for the random walker
"""
import numpy as np

def calc_L2_norm_squared(vector) -> float:
    """
    Calculates the L2 norm squared of a vector
    param vector: the vector to calculate the L2 norm of 
    """
    vector = np.array(vector) # converting to numpy array if it wasn't passed in as such
    return np.sum(vector**2) # returning the sum of the squared entries which is the L2 norm squared


    