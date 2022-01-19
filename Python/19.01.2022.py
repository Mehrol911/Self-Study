import random

for i in range(3):
    print(random.randint(10, 20))


members = ['John', 'Mary', 'Bob', 'Mosh']
leader = random.choice(members)
print(leader)


dice1 = [1, 2, 3, 4, 5, 6]
dice2 = [1, 2, 3, 4, 5, 6]
for i in range(1):
    res1 = [random.choice(dice1)]
    res2 = [random.choice(dice2)]
    result = res1 + res2
    print(result)


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second

dice = Dice()
print(dice.roll())


from pathlib import Path
#Absolute path
#c:\Program Files\Microsoft
# /usr/local/bin
#Relative path
#path = Path("ecommerce")
#print(path.exists()) #mkdir - create
#print(path.rmdir()) #delete

path = Path()
for file in path.glob('*.py'):
    print(file)