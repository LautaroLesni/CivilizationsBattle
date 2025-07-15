class Army:
    def __init__(self, civilization):
        self.gold = 1000
        self.units = []
        self.battles = []
        self.init_units(civilization)

    def init_units(self, civ):
        table = {
            'Chinese': (2, 25, 2),
            'English': (10, 10, 10),
            'Byzantine': (5, 8, 15)
        }
        p, a, k = table[civ]
        self.units += [Pikeman() for _ in range(p)]
        self.units += [Archer() for _ in range(a)]
        self.units += [Knight() for _ in range(k)]

    def total_strength(self):
        return sum(u.strength for u in self.units)

    def train_unit(self, unit_index):
        unit = self.units[unit_index]
        cost = unit.train()
        if self.gold >= cost:
            self.gold -= cost

    def transform_unit(self, unit_index):
        new_unit, cost = self.units[unit_index].transform()
        if new_unit and self.gold >= cost:
            self.gold -= cost
            self.units[unit_index] = new_unit

    def remove_strongest_units(self, count=2):
        self.units.sort(key=lambda u: u.strength, reverse=True)
        del self.units[:count]