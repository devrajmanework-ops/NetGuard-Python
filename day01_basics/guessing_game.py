import random

secret = random.randint(1,10)
attempts = 0

while True:
    try:
        guess = int(input("Guess a number between 1 to 10: "))
    except ValueError:
        print("not a number")
        continue

    if guess < 1 or guess > 10:
        print("out of range")
        continue

    attempts += 1

    if guess == secret:
        print("correct")
        print("attempts", attempts)
        break
    elif guess < secret:
        print("Too low")
    else:
        print("Too high")

    
