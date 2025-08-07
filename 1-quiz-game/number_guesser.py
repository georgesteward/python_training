import random

random_number_range = random.randrange(0, 5)  # prints a random odd number between 1 and 100
random_number_int = random.randint(0, 5)  # prints a random integer between 1 and 100 (inclusive)

# top_of_range = input("Type a number: ")
# if top_of_range.isdigit():
#     top_of_range = int(top_of_range)

#     if top_of_range <= 0:
#         print("Please type a number larger than 0 next time.")
#         quit()
# else:
#     print('Please type a number between 1 and', random_number_range.__rand__)

guesses = 0

while True:
    
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
        print('You guessed:', user_guess)

        # if user_guess <= 0:
        #     print("Please type a number larger than 0 next time.")
        #     quit()
        guesses += 1
    else:
        print('Please type a number between 1 and', random_number_range)
        continue

    if user_guess == random_number_int:
        print('You win! You guessed the correct number in', guesses, 'guess(es), great job!')
        break
    elif user_guess < random_number_int:
        print('You were below the number! Guess higher next time.')
    else:
        print('You were above the number! Guess lower next time.')
    
    print('You have guessed', guesses, 'times out of a total of 3 guesses.')

    if guesses == 3:
        print("Game over! You've guessed 3 times. \nThe number was:", random_number_int)
        break