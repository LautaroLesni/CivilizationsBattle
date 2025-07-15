class Unit:
    def __init__(self, age=0):
        self.age = age
        self.strength = self.base_strength()

    def base_strength(self):
        raise NotImplementedError()

    def train(self):
        raise NotImplementedError()

    def transform(self):
        raise NotImplementedError()


class Pikeman(Unit):
    def base_strength(self):
        return 5

    def train(self):
        self.strength += 3
        return 10  # cost in gold

    def transform(self):
        return Archer(self.age), 30


class Archer(Unit):
    def base_strength(self):
        return 10

    def train(self):
        self.strength += 7
        return 20

    def transform(self):
        return Knight(self.age), 40


class Knight(Unit):
    def base_strength(self):
        return 20

    def train(self):
        self.strength += 10
        return 30

    def transform(self):
        return None, None  # Cannot transform