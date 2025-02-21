import random 

words = ["python", "javascript", "gaming", "github", "karate", "swift,"]
# Randomly chooses word form list
chosen_word = random.choice(words)
word_display = ['_' for _ in chosen_word]
print(word_display)
attempts = 8    # Number of allowed attempts

print("Welcome To Hangman!")

while attempts > 0 and '_' in word_display:
    print("\n" + ' '.join(word_display))
    guess = input("Guess a letter: ").lower()
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess
    else:
        print("That letter doesn't appear in the word! ")
        attempts -= 1


# Game conclusion
if '_' not in word_display:
    print("You guessed the word")
    print(' '.join(word_display))
    print("You Survived! ")
else:
    print("You ran out of attempts. The word was: " + chosen_word)
    print("You Lost! ")