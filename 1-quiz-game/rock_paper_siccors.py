import random

user_wins = 0
computer_wins = 0
redo = 0
options = ['rock', 'paper', 'sissors']

while True:
    user_input = input("Type Rock/Paper/Sissors or Q to quit: ").lower()
    if user_input == 'q':
        quit()

    if user_input not in ['rock', 'paper', 'sissors']:
        print('Invalid response, please type in Rock, Paper, Sissors or Q to quit.')
        continue

    random_number = random.randint(0, 2)
    # 0 = rock, 1 = paper, 2 = sissors
    computer_pick = options[random_number]

    if user_input == 'rock' and computer_pick == 'sissors':
        print('You picked', user_input, 'and the computer picked', computer_pick + '. You win!')
        user_wins += 1
    elif user_input == 'paper' and computer_pick == 'rock':
        print('You picked', user_input, 'and the computer picked', computer_pick + '. You win!')
        user_wins += 1
    elif user_input == 'sissors' and computer_pick == 'paper':
        print('You picked', user_input, 'and the computer picked', computer_pick + '. You win!')
        user_wins += 1
    elif user_input == computer_pick:
        print('You picked', user_input, 'and the computer picked', computer_pick + '. It\'s a tie!')
        redo += 1
    else:
        print('You picked', user_input, 'and the computer picked', computer_pick + '. You lose!')
        computer_wins += 1
    
    print('You have', user_wins, 'wins(s) and the computer has', computer_wins, 'win(s). And you\'ve tied', redo, 'time(s).')
    continue
