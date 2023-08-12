

 # (taking definitions from a package "random" into the my scope

import random
secret_n = random.randint(1, 20)
print("Welcome to my Guess Game")

for attempts in range(1,6):
    print(f"Attempts nr {attempts}")
    guess = int(input("Take a guess"))
    if guess == secret_n:
        print("Congrats! You have guessed correctly!")
        break
    elif guess > secret_n:
        print("Too high!")
    else:
        print("Too low!")
if guess != secret_n:
    print(f"Game Over! My number was{secret_n}")
    