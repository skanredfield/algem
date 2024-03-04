import numpy as np
import matplotlib.pyplot as plt
from sympy import *
from rich.progress import track

from polynomial import *
from genetic_approximation import GeneticApproximation


def target_func(x):
    # return 2*x**3-0.5*x**2+0.1*x-0.5
    return 2*x**3
    # return 2*x**2
    # return np.sin(x)
    # return x


a = -10.0
b = 10.0
n = 50
population_size = 64
mutation_rate = 0.05
num_terms = 5
gen_approx = GeneticApproximation(
    target_func, 
    a, b, n, 
    population_size, 
    mutation_rate, 
    num_terms, 
    RandomPolynomial
)

fitness_result = []

for _ in track(range(5000), description="Iterating"):
    gen_approx.update()
    
    fitness_result.append(gen_approx.population.get_max_fitness()[0])

gen_approx.finalize()
gen_approx.population.polynomials.sort(key=lambda x: x.fitness, reverse=True)

x = np.arange(a, b, 0.1)
y = target_func(x)

fig, ax = plt.subplots()
ax.plot(fitness_result, "C0", label="Best solution")
ax.legend()
ax.set_title("Fitness")
ax.set_xlabel("Iteration #")
plt.show()

plt.xlim(-10, 10)
plt.ylim(-1, 1)
plt.plot(x, y, label="Target function")

# for i in range(5):
#     print("Final poly #", i, ": ", gen_approx.population.polynomials[i].to_symbolic())
#     print("Final fitness #", i, ": ", gen_approx.population.polynomials[i].fitness)
#     y_approx = gen_approx.population.polynomials[i].eval_polynomial(x)
#     plt.plot(x, y_approx)

y_approx = gen_approx.population.polynomials[0].eval_polynomial(x)
plt.plot(x, y_approx)

plt.show()