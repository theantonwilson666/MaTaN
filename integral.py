import numpy as np
import math

class integral():
    def __init__(self, expr, a, b, FNumb):
        self.expr = self.replaceFuncs(expr)
        self.N = 50
        self.Foureie_Numb = int(FNumb)
        self.a = self.replaceInterval(a)
        self.b = self.replaceInterval(b)
        self.h = (self.b - self.a) / self.N

    def replaceFuncs(self, expr):
        buf = expr
        buf = buf.replace('sin', 'math.sin')
        buf = buf.replace('cos', 'math.cos')
        buf = buf.replace('tan', 'math.tan')
        buf = buf.replace('e', 'math.e')
        buf = buf.replace('pi', 'math.pi')
        return buf

    def replaceInterval(self, a):
        a = a.replace('pi', str(math.pi))
        a = a.replace('e', str(math.e))
        return float(a)

    def f(self, x):
        return eval(self.expr)

    def Foureie_f(self, x):
        f = 0
        a0 = (1 / math.pi) * self.Simpsons_formule("1", -math.pi, math.pi)
        for i in np.arange(1, self.Foureie_Numb):
            n = i
            cos_nx = "math.cos(%d*x)" %n
            sin_nx = "math.sin(%d*x)" %n
            f += (1 / math.pi) * self.Simpsons_formule(cos_nx, -math.pi, math.pi) * eval(cos_nx) + (1 / math.pi) * self.Simpsons_formule(sin_nx, -math.pi, math.pi) * eval(sin_nx)
        f += a0 / 2
        return f

    def sum_funcs_odd(self, expr):
        sum = 0
        for i in np.arange(self.a + self.h, self.b, 2 * self.h):
            x = i
            sum += self.f(x) * eval(expr)
        return sum

    def sum_funcs_even(self, expr):
        sum = 0
        for i in np.arange(self.a + 2 * self.h, self.b, 2 * self.h):
            x = i
            sum += self.f(x) * eval(expr)
        return sum

    def Simpsons_formule(self, expr, a, b):
        S = (self.h / 3) * (self.f(a) + 4*self.sum_funcs_odd(expr) + 2*self.sum_funcs_even(expr) + self.f(b))
        return S
