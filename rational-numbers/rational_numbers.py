from __future__ import division
from math import isclose


class Rational(object):
    def __init__(self, numer, denom):
        """Rationals are defined as """
        if numer is None:
            raise ValueError('Not a Number: invalid numerator')
        if denom is None or float(denom) == 0:
            raise ValueError('Not a Number: invalid denominator')
        self.numer = float(numer)
        self.denom = float(denom)

    def convert_fraction_to_integers(numer: float, denom: float):
        """Return a fraction of integers equivalent to input of decimals.
        """
        while not isclose(numer, int(numer)) and not isclose(denom, int(denom)):
            numer, denom = numer * 10, denom * 10

        return int(numer), int(denom)

    def euclidiean_algo(a: int, b: int):
        """an efficient method for computing the greatest common divisor (GCD)
        of two numbers the largest number that divides both of them without leaving a remainder.
        https://en.wikipedia.org/wiki/Euclidean_algorithm

        Returns: the GCD
        """
        pass

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return f'{self.numer}/{self.denom}'

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __truediv__(self, other):
        pass

    def __abs__(self):
        pass

    def __pow__(self, power):
        pass

    def __rpow__(self, base):
        pass
