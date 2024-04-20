import random
import sys

secret_number = random.randint(1, 3)
guess_count = 0
guess_limit = 3
intro = input("Hello, my name is Bob Mactini! Welcome to the guessing game. If you guess the number I'm thinking of, you'll get a nice reward! Do you understand? (yes/no): ")

if intro.lower() == "yes":
    print("Great, now let me think of a number!")
elif intro.lower() == "no":
    print("Damn.")
    sys.exit()
else:
    print("Invalid response. Please answer with 'yes' or 'no'.")
    sys.exit()

while guess_count < guess_limit:
    try:
        guess = int(input('Now Guess!: '))
        guess_count += 1
    except ValueError:
        slightly_annoyed = input("Bro, guess")
        print("slightly_annoyed")
        guess_count -= 1
        continue

    if guess == secret_number:
        print('You won!')
        break
    else:
        print("Bro, Guess")

else:
    print('You failed!')
