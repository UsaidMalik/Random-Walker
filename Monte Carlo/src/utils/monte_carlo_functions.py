"""
Author: Usaid Malik
Date: 06/23/24
About: functions that do a monte carlo simulation 
and return the results for each trial
"""
import numpy as np
from utils.calc_L2_squared import calc_L2_norm_squared
from utils.update_vector_rand import update_vector_randomly
from utils.stastical_functions import *
from scipy import stats
from scipy import optimize


def monte_carlo_vector_entries(dimension_distribution, update_distribution, T=40, d=3, num_iterations=1000):
    vector_entries = []
    for i in range(num_iterations):
        random_vec = random_vector_T_steps(dimension_distribution, update_distribution, T=T, d=d)
        vector_entries.extend(random_vec)
    return vector_entries
    
def monte_carlo_L2_norms(dimension_distribution, update_distribution, T=40, d=3, num_iterations=1000):
    # Initialize a dictionary to store L2 norms for each (T, d) pair
    L2_norms = []
    for i in range(num_iterations):
        random_vec = random_vector_T_steps(dimension_distribution, update_distribution, T=T, d=d)
        L2_norms.append(calc_L2_norm_squared(random_vec))
    
    return L2_norms
