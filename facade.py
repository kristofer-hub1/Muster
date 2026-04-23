import random


class Generator:
    def generate(self, count):
        return random.sample(range(1, 10), count)


class Splitter:
    def split(self, matrix):
        n = len(matrix)
        result = []

        for row in matrix:
            result.append(row)

        for col in range(n):
            result.append([matrix[row][col] for row in range(n)])

        result.append([matrix[i][i] for i in range(n)])
        result.append([matrix[i][n - 1 - i] for i in range(n)])

        return result


class Verifier:
    def verify(self, sublists):
        totals = [sum(s) for s in sublists]
        return len(set(totals)) == 1


class MagicSquareGenerator:
    def __init__(self):
        self._generator = Generator()
        self._splitter = Splitter()
        self._verifier = Verifier()

    def generate(self, size):
        while True:
            numbers = self._generator.generate(size * size)
            matrix = [numbers[i * size:(i + 1) * size] for i in range(size)]
            sublists = self._splitter.split(matrix)
            if self._verifier.verify(sublists):
                return matrix


if __name__ == "__main__":
    gen = MagicSquareGenerator()
    square = gen.generate(3)

    for row in square:
        print(row)
