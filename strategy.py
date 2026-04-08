import cmath

class DiscriminantStrategy:
    def calculate_discriminant(self, a, b, c):
        pass


class OrdinaryDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        return b * b - 4 * a * c


class RealDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        d = b * b - 4 * a * c
        if d < 0:
            return float('nan')
        return d


class QuadraticEquationSolver:
    def __init__(self, strategy):
        self.strategy = strategy

    def solve(self, a, b, c):
        d = self.strategy.calculate_discriminant(a, b, c)

        if isinstance(d, float) and cmath.isnan(d):
            return (complex(float('nan'), float('nan')),
                    complex(float('nan'), float('nan')))

        sqrt_d = cmath.sqrt(d)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)

        return (x1, x2)


# Näited
solver1 = QuadraticEquationSolver(OrdinaryDiscriminantStrategy())
print(solver1.solve(1, 10, 16))

solver2 = QuadraticEquationSolver(RealDiscriminantStrategy())
print(solver2.solve(1, 4, 5))

solver3 = QuadraticEquationSolver(OrdinaryDiscriminantStrategy())
print(solver3.solve(1, 4, 5))