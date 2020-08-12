# import libraries needed
import random
import time

# create the lists needed - the word list, the guess list
wordlist = ["tree", "monkey", "chair", "laptop", "photo"]
letter_list = []
word_list = []
starting_lives = 5
lives = starting_lives
alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "x",
    "y",
    "z",
]
result_letter = ""
result_word = ""

# define the functions needed


def welcome():
    print(
        "Welcome to hangman! The aim of the game is to guess letters that our mystery word is made up of!\n"
    )
    time.sleep(1)
    print("Let's see what our mystery word generator comes up with!\n")
    time.sleep(1)


def choose_words(wordlist):
    hangman_word = random.choice(wordlist)
    return list(hangman_word)


def display_word(hangman_word):
    word_display = ["*" for letter in hangman_word]
    return word_display


def clear_game(letter_list, word_list, lives):
    letter_list = []
    word_list = []
    lives = starting_lives
    return letter_list, word_list, lives


def validate_user_choice(choice):
    if choice[0] == "w":
        return "word"
    else:
        return "letter"


def user_guess():
    guess = input("What's your guess?\n")
    return guess


def is_choice_valid(choice, guess, letter_list, word_list, alphabet):
    if choice[0].lower() == "w":
        if guess in word_list:
            print("You have already guessed that.")
        elif [character in alphabet for character in list(guess)]:
            word_list.append(guess)
        else:
            print("This is not a valid guess.")
    else:
        if guess in letter_list:
            print("You have already guess that.")
        elif guess in alphabet:
            letter_list.append(guess)


def lose_a_life(lives):
    lives -= 1
    return lives


def check_letter_guess(guess, hangman_word):
    if guess in hangman_word:
        print("Great guess, that letter is in the mystery word!\nLet's see where!")
        time.sleep(2)
        guess_indexes = [
            index for index, character in enumerate(hangman_word) if guess == character
        ]
        for index in guess_indexes:
            hangman_display[index] = guess
        print("".join(hangman_display))
    else:
        print("That letter is not in the mystery word!")
        time.sleep(2)
        # call lose lives func
        print("Let's try again!")
    time.sleep(2)
    print("Here is what you have guessed so far:")
    time.sleep(1)
    print("Letters: ")
    print(letter_list)
    print("Words: ")
    print(word_list)


def check_word_guess(guess, hangman_word):
    if guess == "".join(hangman_word):
        print("You guessed the right word!")
        time.sleep(1)
        print("You won!")
        done = True
        return done
    else:
        print("You guessed the wrong word!")
        time.sleep(2)
        print("Here is what you have guessed so far:")
        time.sleep(1)
        print("Letters: ")
        print(letter_list)
        print("Words: ")
        print(word_list)


def is_word_hidden(display_word):
    if "*" not in display_word:
        print("You won!")
        return True
    else:
        return False


def remaining_lives(lives):
    if lives != 0:
        print("Your remaining lives:")
        print(lives)
        done = False
        return done
    else:
        print("You have no more remaining lives")
        time.sleep(1)
        print("GAME OVER")
        done = True
        return done


def game_ended(result_word, result_letter, lives, is_word_hidden):
    if result_word == True:
        print("You won!")
        return True
    elif result_letter == True:
        return is_word_hidden(display_word)
    elif lives == 0:
        "Sorry that's the end of your lives. Better luck next time."
        return True


def play_again():
    again = input("Would you like to play again? Y/N:")
    print(again)


## GAME PLAY

# welcome player
welcome()

# initial display of word
hangman_word = choose_words(wordlist)
time.sleep(2)
print("Here is your mystery word...\n")
time.sleep(2)
hangman_display = display_word(hangman_word)
print("".join(hangman_display))

# game play
done = False
while not done:

    while True:
        choice = input("Would you like to guess a word or letter? w/l")
        if choice.lower() not in ("w", "l", "word", "letter"):
            print("Please select w or l.")
        else:
            break

    guess = user_guess()

    is_choice_valid(choice, guess, letter_list, word_list, alphabet)

    lives = lose_a_life(lives)

    if choice[0].lower() == "w":
        result_word = check_word_guess(guess, hangman_word)
    else:
        result_letter = check_letter_guess(guess, hangman_word)
    print("Your remaining lives are:")
    print(lives)

    done = game_ended(result_word, result_letter, lives, is_word_hidden)
    if done:
        x = "".join(hangman_word)
        print(f"The word was {x}.")

# end game
print("That's the end of the game!")
time.sleep(1)
letter_list, word_list, lives = clear_game(letter_list, word_list, lives)
again = play_again()
