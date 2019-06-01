from __future__ import division
from fractions import gcd


class Rational(object):
    def __init__(self, numer: int, denom: int):
        """a rational number is any number that can be expressed
        as the fraction (p/q) of a numerator and a denominator.

        We store the smallest coprime numerator and denominator.
        """
        if denom == 0:
            raise ValueError('Not a Number: invalid denominator')
        _gcd = gcd(numer, denom)  # will make denom positive
        self.numer = int(numer / _gcd)
        self.denom = int(denom / _gcd)

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return f'{self.numer}/{self.denom}'

    def __add__(self, other):
        denom_gcd = gcd(self.denom, other.denom)
        num = sum([other.denom / denom_gcd * self.numer,
                   self.denom / denom_gcd * other.numer])
        den = self.denom / denom_gcd * other.denom
        return Rational(num, den)

    def __sub__(self, other):
        negated_other = Rational(-other.numer, other.denom)
        return self + negated_other

    def __mul__(self, other):
        return Rational(
            self.numer * other.numer,
            self.denom * other.denom
        )

    def __truediv__(self, other):
        return self * other.reciprocal

    def __abs__(self):
        return Rational(
            abs(self.numer),
            abs(self.denom)
        )

    def __pow__(self, power: int):
        if power > 0:
            return Rational(
                self.numer ** power,
                self.denom ** power
            )
        elif power == 0:
            return Rational(1, 1)
        else:
            return self.reciprocal, -power

    def __rpow__(self, base):
        return base ** self.decimal

    @property
    def reciprocal(self):
        return Rational(self.denom, self.numer)

    @property
    def decimal(self):
        return float(self.numer) / self.denom
