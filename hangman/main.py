import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

display = ""

is_game_over = False
while not is_game_over:
    guess = input("Make your guess: ").lower()

    for letter in chosen_word:
        if letter == guess:
            display += letter
        else:
            display += "_"

    print(display)


# TODO-2: Change the for loop so that you keep the previous correct letters in display.
