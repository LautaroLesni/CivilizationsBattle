from army.army import Army
from army.battle import Battle

def main():
    army1 = Army("Chinese")
    army2 = Army("English")

    print("Army 1 strength:", army1.total_strength())
    print("Army 2 strength:", army2.total_strength())

    battle = Battle(army1, army2)
    result = battle.resolve()
    print(result)
    print("Army 1 gold:", army1.gold)
    print("Army 2 gold:", army2.gold)

if __name__ == "__main__":
    main()