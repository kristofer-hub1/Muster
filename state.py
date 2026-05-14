class CombinationLock:
    def __init__(self, combination):
        self.combination = combination
        self.entered = []
        self.status = 'LOCKED'

    def enter_digit(self, digit):
        self.entered.append(digit)

        if self.entered != self.combination[:len(self.entered)]:
            self.status = 'ERROR'

        elif self.entered == self.combination:
            self.status = 'OPEN'

        else:
            self.status = ''.join(map(str, self.entered))


cl = CombinationLock([1, 2, 3, 4, 5])

print(cl.status)

cl.enter_digit(1)
print(cl.status)

cl.enter_digit(2)
print(cl.status)

cl.enter_digit(3)
print(cl.status)

cl.enter_digit(4)
print(cl.status)

cl.enter_digit(5)
print(cl.status)
