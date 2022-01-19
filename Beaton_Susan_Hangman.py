# A  game of hangman intended for the Jhub coding scheme
# Specifications are
# Run in python 3
# Script only stops to ask for next guess or because the game has ended
# Asking the user to enter their next guess - "Please enter your next guess: "
# The hidden word must be represented by * and revealed as correct letters are guessed
# The program will end with "Congratulations you win" or "You Lose"
# The word selected much be random and from the file word_list.txt
# The user has 7 lives

import random

with open("word_list.txt", "r") as f:
    word_list = f.read().splitlines()

# Txt file is opened, read and returns a list of lines as strings.

selected_word = random.choice(word_list).lower()
# From the list of words provided a random word is selected from the it and is converted to lowercase

allowed_guesses = 7
# The number of guesses the player is allowed to make each round

incorrect_letters_guessed = []
# All incorrect letters guessed will be stored in this list, this could be printed on screen, if needed

correct_letters_guessed = []
# All correctly guessed letters will be stored in this list

count_of_letters_in_selected_word = len(set(selected_word))
# Used to calculate the count of unique letters in the selected_word

while allowed_guesses >= 0:
    for letter in selected_word:
        if letter.lower() in correct_letters_guessed:
            print(letter, end=" ")
            # end= will print the letters on 1 line and not multiple
        else:
            print("*", end=" ")
    print("")

# This while loop determines if a character in the selected_word should be unveiled or not
# If the user_input is in the word, the * changes to reveal the letter
# If the user_input is not in the word, nothing changes



    user_input = input("Please enter your next guess: ")

    # This loop uses a number of if statements and nested if statements to determining what action to take
    # and to decide if the game is won or lost
    if user_input.lower() in selected_word.lower():
        correct_letters_guessed.append(user_input.lower())
        # This if statement looks at whether the letter chosen by the user is in the selected_word
        # If it is, the letter is then stored in the corret_letters_guessed list

            # A print statement could be added to show both correct and incorrect letters guessed
            # A print statement could also show the guesses remaining


        if len(correct_letters_guessed) == count_of_letters_in_selected_word:
            print("You win")
            break
        # Once a correct letter has been stored in the correct_letters_guessed list
        # A nested if statment uses the count of unique letters in the selected_word and cound_of_correct_letters_guessed
        # to determine if the game has ben won
        # if they are not == then the break ends the loop and allows the user to choose another letter

    if user_input not in selected_word:
        # letters_guessed.append(user_input.lower()):
        incorrect_letters_guessed.append(user_input.lower())
        allowed_guesses -= 1
        # This if statement looks at whether the letter chosen by the user is in the selected_word
        # If it is not, the letter is then stored in the incorrect_letters_guessed list
            # This list is not used further but could be used to show letters already guessed by the user
                # or to inform them when they have selected a letter twice

                # A print statement could be added to show both correct and incorrect letters guessed
                # As well as guesses remaining

        if allowed_guesses == 0:
            print("You Lose")
            break

        #The nested if statement then checks if the player has any lives remaining
        # If the user has 0 lives the game is lost and the script ends
        # If the player still has lives, the break ends the loop and allows them to choose another letter
