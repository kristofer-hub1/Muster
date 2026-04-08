from abc import ABC

class Creature:
    def __init__(self, attack, health):
        self.attack = attack
        self.health = health

class CardGame(ABC):
    def __init__(self, creatures):
        self.creatures = creatures

    def combat(self, c1_index, c2_index):
        c1 = self.creatures[c1_index]
        c2 = self.creatures[c2_index]

        a1 = self.hit(c1, c2)
        a2 = self.hit(c2, c1)

        if a1 == a2:
            return -1
        return c1_index if a1 else c2_index

    def hit(self, attacker, defender):
        pass

class TemporaryDamageCardGame(CardGame):
    def hit(self, attacker, defender):
        old_health = defender.health
        defender.health -= attacker.attack
        alive = defender.health > 0
        if alive:
            defender.health = old_health
        return alive

class PermanentDamageCardGame(CardGame):
    def hit(self, attacker, defender):
        defender.health -= attacker.attack
        return defender.health > 0


creatures = [Creature(1, 3), Creature(1, 3)]
game = PermanentDamageCardGame(creatures)

print(game.combat(0, 1))
print(game.combat(0, 1))