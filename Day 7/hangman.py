import random
import hangman_words
import hangman_ASCII

chosen_word = random.choice(hangman_words.word_list)

guessedWord = ['_'] * len(chosen_word) # generate list of the same character [value or element] * length_of_list
## can't be a list cause strings are immutable can't be changed once created

life_counter = 6

print(hangman_ASCII.logo)

while ('_' in guessedWord) and (life_counter > 0):
    guessedLetter = input("Guess a letter: ").lower()

    if (guessedLetter in guessedWord):
        print("\nYou've already guessed that letter!")
    print(" ".join(guessedWord))

    for i in range(len(chosen_word)):
        if chosen_word[i] == guessedLetter:
            guessedWord[i] = guessedLetter
    if guessedLetter not in chosen_word:
        life_counter -= 1

    print(hangman_ASCII.stages[life_counter])


if life_counter > 0:
    print("You won !")
else:
    print(f"The word was {chosen_word}")
    print("You lost !")
