import random
from hangman_words import word_list
from hangman_art import stages, logo
print(logo)
lives = 6
chosen_word = random.choice(word_list)

correct_letters = []
guessed_letters = []

is_game_over = False
while not is_game_over:
    guess = input("Make your guess: ").lower()
    display = ""

    if guess in guessed_letters:
        print(f"You have guessed {guess} before!")

    guessed_letters.append(guess)

    if guess not in chosen_word:
        lives -= 1
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    if lives == 0:
        is_game_over = True
        print("You lose!")

    print(stages[::-1][lives])
    print(display)
    print(f"################### You have {lives} left! ############################")

# TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
#  e.g. You guessed d, that's not in the word. You lose a life.
