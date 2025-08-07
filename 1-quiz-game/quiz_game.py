print('Welcome to the Quiz Game!')

playing = input('Do you want to play? (yes/no): ').lower()
if playing.lower() != 'yes':
    print('Maybe next time!')
    quit()

print('Great! Let\'s start the game.')
score = 0
total_questions = 0
answer = input('What does CPU stand for? ')
if answer.lower() == 'central processing unit':
    print('Correct!')
    score += 1
else:
    print('Incorrect!', answer, 'is not the correct answer. \nThe correct answer is Central Processing Unit.')
total_questions += 1

answer = input('What does GPU stand for? ')
if answer.lower() == 'graphics processing unit':
    print('Correct!')
    score += 1
else:
    print('Incorrect!', answer, 'is not the correct answer. \nThe correct answer is Graphics Processing Unit.')
total_questions += 1

print('Your final score is:', score, 'out of', total_questions)
print('Percentage:', (score / total_questions) * 100, '%')