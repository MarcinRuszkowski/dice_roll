from random import randint

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}
'''
diceRolls = []

amountOfRolls = int(input('How many rolls? '))
for dice in range(amountOfRolls):
    diceRolls.append(randint(1, 6))

for num in diceRolls:
    for line in dice_art.get(num):
        print(line)

rolledValues = 0
for num in diceRolls:
    rolledValues += num

print(f'Rolled values: {rolledValues}')
'''
# func

def roll_dice(amountOfRoll):
    diceRolls = []
    for dice in range(amountOfRoll):
        diceRolls.append(randint(1, 6))

    return diceRolls

def count_rolled_values(diceRolls):
    rolledValues = 0
    for value in diceRolls:
        rolledValues += value
    print(rolledValues)


def show_rolled_dice(diceRolls):
    for num in diceRolls:
        for line in dice_art.get(num):
            print(line)


diceRolls = roll_dice(3)
show_rolled_dice(diceRolls)
count_rolled_values(diceRolls)
