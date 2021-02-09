import random
secret_number = random.randint(1, 50)
guess_number = int(input("enter an integer number between 1 and 50: "))

while secret_number != "guess_number":
    if guess_number < secret_number:
        print("YOUR GUESS IS LOW!")
        guess_number = int(input("enter an integer number between 1 and 50: "))
    elif guess_number > secret_number:
        print("YOUR GUESS IS HIGH!")
        guess_number = int(input("enter an intger number between 1 and 50: "))
    else:
        print("YOU GUESSED IT!, MABROOT YA 3INAIAA :)")
        break
