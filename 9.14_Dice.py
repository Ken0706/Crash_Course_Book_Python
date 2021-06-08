from random import randint


class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_dice(self):
        print(f"Die with {self.sides} sides ")
        for i in range(10):
            x = randint(1, self.sides)
            print(f"Times : {i + 1} | Die : {x}")
        print("-" * 25)


def main():
    die6sides = Die()
    die6sides.roll_dice()
    die10sides = Die(10)
    die10sides.roll_dice()
    die20sides = Die(20)
    die20sides.roll_dice()

if __name__ == '__main__':
    main()
