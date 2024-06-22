import matplotlib.pyplot as plt
import numpy as np
from utils.calc_L2_squared import calc_L2_norm_squared
from utils.update_vector_rand import update_vector_randomly
from utils.stastical_functions import *
from scipy import stats
from scipy import optimize

def random_vector_T_steps(T, d):
    vector = np.zeros(d) # numpy vector of 0's indicating the origin with dimensions d
    for _ in range(T):
        vector = update_vector_randomly(vector, dimension_distribution, update_distribution)
    return vector

# Initialize a dictionary to store L2 norms for each (T, d) pair
L2_norms_dict = {}
inside_values_dict = {}

T_values = [2, 10, 30, 50]
d_values = [2]

for T in T_values:
    for d in d_values:
        dimension_distribution = {i: 1/d for i in range(d)}
        update_distribution = {-1: 1/2, 1: 1/2}
        
        inside_values = []
        L2_norms = []
        for i in range(1000):
            random_vec = random_vector_T_steps(T=T, d=d)
            inside_values.extend(random_vec)
            L2_norms.append(calc_L2_norm_squared(random_vec))
        
        # Store the L2 norms in the dictionary
        L2_norms_dict[(T, d)] = L2_norms
        inside_values_dict[(T, d)] = inside_values
        print("finsihed d value iter")
    print("finsihed T value iter")

# Plot the L2 Norm values for each (T, d) pair

for (T, d), L2_norms in L2_norms_dict.items():
    plt.hist(L2_norms, alpha=0.5, label=f'T={T}, d={d}')

plt.xlabel("L2 Norm values with 10000 Iterations")
plt.ylabel("Frequency")
plt.legend(loc='upper right')
plt.show()


def test_func(x, a, b):
    return stats.norm.pdf(x, a, b)


# Plot the inside values of the vectors (not squared) for each (T, d) pair
for (T, d), inside_values in inside_values_dict.items():
    # Calculate the histogram
    hist, bins = np.histogram(inside_values, bins=15)
    bin_centers = (bins[:-1] + bins[1:]) / 2

    # Plot the dots at the top of each bar
    plt.scatter(bin_centers, hist, label=f'T={T}, d={d}')

    normalization_factor = np.trapz(hist, bin_centers)  # area under the curve
    params, pcov = optimize.curve_fit(test_func, bin_centers, hist / normalization_factor)

    x_detailed = np.linspace(bin_centers.min() - 3, bin_centers.max() + 3, 200)
    plt.plot(x_detailed, test_func(x_detailed, params[0], params[1]) * normalization_factor,label=f'Line of best fit T={T}, d={d}')

    # Calculate and plot the line of best fit
    coefficients = np.polyfit(bin_centers, hist, 1)
    poly = np.poly1d(coefficients)
   # plt.plot(bin_centers, poly(bin_centers), label=f'Best fit: T={T}, d={d}')


plt.xlabel("Vector Entry values with 1000 Iterations")
plt.ylabel("Frequency")
plt.legend(loc='upper right')
plt.show()
