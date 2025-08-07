with open("story.txt", "r") as f:
    # Read the entire content of the file into the variable 'story'.
    story = f.read()
# print(story)

# Using a set to store unique words found between < and >
words = set()
start_of_word = -1
target_start = "<"
target_end = ">"

# Enumerate over each character in the story to find words between < and >
for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i

    if char == target_end and start_of_word != -1:
    # if char == target_end:
        word = story[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1

print(sorted(words))

words = sorted(words)
answers = {}

for word in words:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer

print(answers)

for word in words:
    story = story.replace(word, answers[word])
print(story)