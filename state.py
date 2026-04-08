class CombinationLock:
    def __init__(self, combination):
        self.combination = combination          # õige kombinatsioon
        self.entered = []                       # seni sisestatud numbrid
        self.status = 'LOCKED'                  # algolek

    def enter_digit(self, digit):
        # Kui juba OPEN või ERROR, ei tee enam midagi
        if self.status in ('OPEN', 'ERROR'):
            return

        # Lisa uus number
        self.entered.append(digit)

        # Kontrolli, kas sisestus vastab kombinatsiooni algusele
        for i in range(len(self.entered)):
            if self.entered[i] != self.combination[i]:
                self.status = 'ERROR'
                return

        # Kui kogu kombinatsioon on sisestatud õigesti
        if len(self.entered) == len(self.combination):
            self.status = 'OPEN'
        else:
            # Näita sisestatud numbreid stringina
            self.status = ''.join(map(str, self.entered))