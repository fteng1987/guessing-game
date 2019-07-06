from random import randint

number = randint(1,10)


while True:
    guess = input("Please enter a number: ")
    guess = int(guess)
    if guess == number:
        print("You've guessed correctly.")
        break
    else:
        continue 
