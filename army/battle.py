class Battle:
    def __init__(self, army1, army2):
        self.army1 = army1
        self.army2 = army2

    def resolve(self):
        p1 = self.army1.total_strength()
        p2 = self.army2.total_strength()

        if p1 > p2:
            winner, loser = self.army1, self.army2
        elif p2 > p1:
            winner, loser = self.army2, self.army1
        else:
            self.army1.remove_strongest_units(1)
            self.army2.remove_strongest_units(1)
            return "Tie"

        loser.remove_strongest_units(2)
        winner.gold += 100
        winner.battles.append(self)
        loser.battles.append(self)
        return f"Winner: {'Army1' if winner == self.army1 else 'Army2'}"