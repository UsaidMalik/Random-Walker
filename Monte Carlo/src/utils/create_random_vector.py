"""
Author: Usaid malik
Date: 06/23/2024
About: Creates a random vector demonstrated after T time
steps with dimension d
"""
import numpy as np
from .update_vector_rand import update_vector_randomly

def random_vector_T_steps(dimension_distribution, update_distribution, T, d):
    vector = np.zeros(d) # numpy vector of 0's indicating the origin with dimensions d
    for _ in range(T):
        vector = update_vector_randomly(vector, dimension_distribution, update_distribution)
    return vector

