print("guessing game")
import random
random_number = random.randint(1, 10)
guess = 0
while True:
    guess += 1
    guesses = int(input("Guess the number?: "))
    if guesses == random_number:
        print("You guessed the number correctly in ", guess, "guesses")
        break
    elif guesses > random_number:
        print("Try again, too high.")
    elif guesses < random_number:
        print("Try again, too low.")



