import numpy as np
from sympy import *

class Polynomial:

    def to_symbolic(self):
        x = Symbol('x')
        return self.eval_polynomial(x)
    
    def calculate_fitness(self, target_func):
        self.fitness = 0
        step = (self.dna.b - self.dna.a) / self.dna.n
        x = self.dna.a
        for _ in range(self.dna.n):
            diff = target_func(x) - self.eval_polynomial(x)
            try:
                self.fitness += 1/(diff**2 + 1.0)
            except ZeroDivisionError:
                self.fitness += 1000000
            x += step


class FifthDegreePolynomial(Polynomial):

    def __init__(self, dna) -> None:
        self.dna = dna
        self.fitness = 0

        self.t0_factor = round(np.interp(self.dna.genes[0], [0.0, 1.0], [-10.0, 10.0]), 5)
        self.t1_factor = round(np.interp(self.dna.genes[2], [0.0, 1.0], [-10.0, 10.0]), 5)
        self.t2_factor = round(np.interp(self.dna.genes[4], [0.0, 1.0], [-10.0, 10.0]), 5)
        self.t3_factor = round(np.interp(self.dna.genes[6], [0.0, 1.0], [-10.0, 10.0]), 5)
        self.t4_factor = round(np.interp(self.dna.genes[8], [0.0, 1.0], [-10.0, 10.0]), 5)

        self.t0_power = 1
        self.t1_power = 2
        self.t2_power = 3
        self.t3_power = 4
        self.t4_power = 5

    def eval_polynomial(self, x):
        result = (self.t0_factor * x**self.t0_power)
        result += (self.t1_factor * x**self.t1_power)
        result += (self.t2_factor * x**self.t2_power)
        result += (self.t3_factor * x**self.t3_power)
        result += (self.t4_factor * x**self.t4_power)
        return result
    

class RandomFiveTermPolynomial(Polynomial):

    def __init__(self, dna) -> None:
        self.dna = dna
        self.fitness = 0

        self.t0_factor = round(np.interp(self.dna.genes[0], [0.0, 1.0], [-10.0, 10.0]), 5)
        self.t1_factor = round(np.interp(self.dna.genes[2], [0.0, 1.0], [-10.0, 10.0]), 5)
        self.t2_factor = round(np.interp(self.dna.genes[4], [0.0, 1.0], [-10.0, 10.0]), 5)
        self.t3_factor = round(np.interp(self.dna.genes[6], [0.0, 1.0], [-10.0, 10.0]), 5)
        self.t4_factor = round(np.interp(self.dna.genes[8], [0.0, 1.0], [-10.0, 10.0]), 5)

        self.t0_power = int(np.interp(self.dna.genes[1], [0.0, 1.0], [1, 10]))
        self.t1_power = int(np.interp(self.dna.genes[3], [0.0, 1.0], [1, 10]))
        self.t2_power = int(np.interp(self.dna.genes[5], [0.0, 1.0], [1, 10]))
        self.t3_power = int(np.interp(self.dna.genes[7], [0.0, 1.0], [1, 10]))
        self.t4_power = int(np.interp(self.dna.genes[9], [0.0, 1.0], [1, 10]))

    def eval_polynomial(self, x):
        result = (self.t0_factor * x**self.t0_power)
        result += (self.t1_factor * x**self.t1_power)
        result += (self.t2_factor * x**self.t2_power)
        result += (self.t3_factor * x**self.t3_power)
        result += (self.t4_factor * x**self.t4_power)
        return result
    

class RandomPolynomial(Polynomial):

    def __init__(self, dna) -> None:
        if len(dna.genes) < 2:
            raise("Random polynomials should be provided with more than two genes.")

        if len(dna.genes) % 2 != 0:
            raise("Random polynomials should be constructed around an even number of genes.")
        
        self.dna = dna
        self.fitness = 0

        self.factors = []
        self.powers = []

        for i in range(len(self.dna.genes)-1):
            self.factors.append(round(np.interp(self.dna.genes[i], [0.0, 1.0], [-10.0, 10.0]), 5))
            self.powers.append(int(np.interp(self.dna.genes[i+1], [0.0, 1.0], [1, 10])))

    def eval_polynomial(self, x):
        result = 0
        for i in range(len(self.factors)):
            result += (self.factors[i] * x**self.powers[i])
        return result
    
    