name = input("What is your name? ")
print("Hello", name, "and welcome to the choose your own adventure game!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? (left/right) ").lower()
if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across? (walk/swim) ").lower()
    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print("Not a valid option. You lose.")
elif answer == "right":
    answer = input("You come to a mountain, you can climb it or go around it? (climb/around) ").lower()
    if answer == "climb":
        print("You climbed the mountain and found a treasure chest!")
    elif answer == "around":
        print("You went around the mountain and got lost.")
    else:
        print("Not a valid option. You lose.")
quit()