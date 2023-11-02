import random

top_of_range = input("plz enter a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("plz enter a number larger than 0 next time")
else:
    print("plese enter a number next time")
    quit()


random_number = random.randint(0, top_of_range)
guesses = 0


while True:
    guesses += 1
    user_guess = input("please enter a guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("plese enter a number next time")
        continue

    if user_guess == random_number:
        print("you got it")
        break
    elif  user_guess > random_number:
        print("you were above the number")
    else:
        print("you were below the number")

print("you got in", guesses, "guesses")
    
    



