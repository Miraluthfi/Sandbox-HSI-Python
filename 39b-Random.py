import random

names = ['Almira', 'Zaidan', 'Asni', 'Azis']

lower_limit = 0
upper_limit = len(names) - 1

random_int = random.randint(lower_limit, upper_limit)
print("Random mikir sendiri ")
winner = names[random_int]
print(winner)

# Random set forward
print("Random set forward")
winner = random.choice(names)
print(winner)