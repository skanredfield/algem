import numpy as np
from sympy import *
import random

from math import floor


class DNA:

    def __init__(self, a, b, n, num_terms) -> None:
        self.a = a
        self.b = b
        self.n = n
        self.num_terms = num_terms
        self.genes = []
        self.fitness = 0
        for _ in range(num_terms*2):
            self.genes.append(random.random())

    def crossover(self, partner):
        child = DNA(self.a, self.b, self.n, self.num_terms)
        midpoint = floor(random.randrange(0, len(self.genes)))
        for i in range(len(self.genes)):
            if (i < midpoint):
                child.genes[i] = self.genes[i]
            else:
                child.genes[i] = partner.genes[i]
        return child

    def mutate(self, mutation_rate):
        for i in range(len(self.genes)):
            if (random.random() < mutation_rate):
                self.genes[i] = random.random()
    
        