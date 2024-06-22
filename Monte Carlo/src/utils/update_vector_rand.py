"""
Author: Usaid Malik
Date: 05/23/2023
About: Used to update a vector randomly by 
incrementing one of its dimensions with a certain probability 
by a certain value with some probability distribution of values
"""
import random

def update_vector_randomly(vector, dimension_distribution, value_distribution):
    """
    updates vector randomly and returns the randomly updated vector
    vector: array of numbers
       the vector to be updated 
    dimension_distribution: Dictionary[Key: dimension index, value: probability of updating]
        this is a hashmap holding the dimension index and the probability of updating that dimension
        index, all values must sum to one 
    value_distribution: Dictionary[Key: value to update by, value: probability of updating with theat value]
        this is a hashmap holding the value to update a certain dimension index by and the corresponding 
        value is the probability of updating by that value. the values must sum to one
    """
    chosen_dimension = random.choices(list(dimension_distribution.keys()), list(dimension_distribution.values()))
    chosen_value = random.choices(list(value_distribution.keys()), list(value_distribution.values()))
    vector[chosen_dimension] += chosen_value
    return vector
