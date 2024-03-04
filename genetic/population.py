from sympy import *
import random

from dna import DNA
from polynomial import *


class Population:

    def __init__(self, size, mutationRate, a, b, n, num_terms, PolyClass):
        self.mutationRate = mutationRate
        self.polynomials = []
        self.matingPool = []
        self.generations = 0
        self.PolyClass = PolyClass
        for _ in range(size):
            self.polynomials.append(PolyClass(DNA(a, b, n, num_terms)))

    def weighted_selection(self):
        index = 0
        start = random.random()
        while (start > 0):
            start -= self.polynomials[index].fitness
            index += 1
        index -= 1
        return self.polynomials[index]

    # normalize the fitness values
    def selection(self, f):
        totalFitness = 0
        for i in range(len(self.polynomials)):
            self.polynomials[i].calculate_fitness(f)
            totalFitness += self.polynomials[i].fitness
        for i in range(len(self.polynomials)):
            self.polynomials[i].fitness /= totalFitness

    def reproduction(self, f):
        nextPolynomials = []
        for _ in range(len(self.polynomials)):
            parentA = self.weighted_selection()
            parentB = self.weighted_selection()
            child = parentA.dna.crossover(parentB.dna)
            child.mutate(self.mutationRate)
            poly = self.PolyClass(child)
            poly.calculate_fitness(f)
            nextPolynomials.append(poly)
        self.polynomials = nextPolynomials
        self.generations += 1

    def get_max_fitness(self):
        max_fitness = -1
        index = -1
        for i in range(len(self.polynomials)):
            if self.polynomials[i].fitness > max_fitness:
                max_fitness = self.polynomials[i].fitness
                index = i
        return (max_fitness, index)