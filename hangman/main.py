import random
from hangman_words import word_list
from hangman_art import stages, logo

print(logo)
lives = 6
chosen_word = random.choice(word_list)
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

correct_letters = []
guessed_letters = []

is_game_over = False
while not is_game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Make your guess: ").lower()
    if guess in guessed_letters:
        print(f"You have guessed {guess} before!")
    guessed_letters.append(guess)

    display = ""

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print("Word to guess: " + display)

    if lives == 0:
        is_game_over = True
        print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")

    if "_" not in display:
        is_game_over = True
        print("****************************YOU WIN****************************")

    print(stages[::-1][lives])