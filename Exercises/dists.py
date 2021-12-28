import math
import random

class Distribution:
    def __init__(self, pdf, cdf):
        self.pdf = pdf
        self.cdf = cdf

    def __mul__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            def newpdf(x):
                return self.pdf(x) * other
            def newcdf(x):
                return self.cdf(x) * other
            return Distribution(newpdf, newcdf)
        else:
            return NotImplemented

    def __add__(self, other):
        def newpdf(x):
            return self.pdf(x) + other.pdf(x)
        def newcdf(x):
            return self.cdf(x) + other.cdf(x)
        return Distribution(newpdf, newcdf)
    
class Normal(Distribution):
    def __init__(self, mean, stdev):
        self.mean = mean
        self.stdev = stdev

    def pdf(self, x):
        return (1.0 / math.sqrt(2 * math.pi * self.stdev ** 2)) * math.exp(-0.5 * (x - self.mean) ** 2 / self.stdev ** 2)

    def cdf(self, x):
        return (1 + math.erf((x - self.mean) / math.sqrt(2) / self.stdev)) / 2

    def sample(self):
        return self.mean + self.stdev * math.sqrt(2) * math.cos(2 * math.pi * random.random())

