import random

random_number1 = random.randint(1, 10)
# Gives the random number between and inclusive of 1 and 10 (a <= random number <=10)
print(random_number1)

random_number2 = random.random()
# Gives the random number between 0 and 1 (0 < random number < 1)
print(random_number2)

random_number3 = random.uniform(1, 10)
# Gives the random float number between and inclusive of 1 and 10 (0 <= random number <= 1)
print(random_number3)

# -----------> Heads or tails

choice = random.randint(0, 1)
if choice == 0:
    print("Heads")
else:
    print("Tails")
