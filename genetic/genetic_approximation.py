from population import Population
from polynomial import *


class GeneticApproximation:

    def __init__(self, f, a, b, n, population_size, mutation_rate, num_terms=5, PolyClass=FifthDegreePolynomial):
        self.target_func = f
        self.population = Population(population_size, mutation_rate, a, b, n, num_terms, PolyClass)

    def update(self):
        self.population.selection(self.target_func)
        self.population.reproduction(self.target_func)

    def finalize(self):
        self.population.selection(self.target_func)