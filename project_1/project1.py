# Dice game where players take turns to roll a dice and accumulate points. The first player to reach a score of 10 wins.
# If a player rolls a 1, they lose all points accumulated in that turn and their turn ends. And their score is reset to 0.

import random

def roll():
    min_val = 1
    max_val = 6
    random_dice_roll = random.randint(min_val, max_val)
    
    return random_dice_roll

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Invalid number of players. Please enter a number between 2 and 4.")
    else:
        print("Invalid input. Please enter a number.")

# print(players)

max_score = 10
# for loop to create a list with players scores initialized to 0. Player 1 starts at index 0. Note the use of underscore (_) as a throwaway variable.
players_scores = [0 for _ in range(players)]

# Game loop that will check if any player has reached the max score, if not it will continue the game.
while max(players_scores) < max_score:

    for player_index in range(players):
        print("\nPlayer", player_index + 1, "turn\n")
        print("Your total score is:", players_scores[player_index], "\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll the dice? (y/n): ")
            if should_roll.lower() != 'y':
                break
         
            print("\nCurrent players turn is player", player_index + 1)

            value = roll()
            if value == 1:
                print("You rolled a 1! No points this turn.")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a", value)
            
            print("Current score:", current_score, "Max score to win:", max_score)
        
    
        players_scores[player_index] += current_score
        print("Total score for Player", player_index + 1, "is now:", players_scores[player_index])

# player_scores is a list of scores for each player in the form of something like [5, 10, 3, 7] where there are 4 players and each index represents the players score. 
    # Where index 0 is player 1 (with a value of 5), index 1 is player 2 (with a value of 10), etc.
print("\nFinal Scores:", players_scores)

max_score_value = max(players_scores)
winner_index = players_scores.index(max_score_value)
print("\nPlayer", winner_index + 1, "wins with a score of", max_score_value, "!")