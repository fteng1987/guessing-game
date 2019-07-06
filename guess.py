from random import randint

number = randint(1, 10)
count = 0

while True:
    guess = input("Please enter a number, you have five guesses: ")
    guess = int(guess)

    count += 1
    if guess == number:
        print("You've guessed correctly.")
        break
    
    print("count=", count)
    if count > 5:
        print("You've run out of guesses.")
        break
    else:
        continue 
