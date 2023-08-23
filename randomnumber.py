print("Think of a number and the computer would try to guess it correctly")
import random
a = int(input("enter the lower boundary?: "))
b = int(input("enter the upper boundary?: "))
print("enter 'h' for too high, 'l' for too low and 'c' for correct")

while True: 
    random_number = random.randint(a, b)
    feedback = input(f"is {random_number} too high, too low or correct?: ")
    if feedback == "h":
        b = random_number - 1
    elif feedback == "l":
        a = random_number + 1
    elif feedback == "c":
        print("the computer guessed the number correctly!")
        break

