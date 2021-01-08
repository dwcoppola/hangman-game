from random import random
import os
capital_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
                    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
def populate_mystery_word(word):
    display_word = " "
    for v in word:
        if not v in correct_guesses:
            display_word += " _ "
        else: 
            display_word += f" {v} "
    return display_word
word_list = open("5desk.txt", "r")
lines = word_list.readlines()
word_list.close()
def get_game_word():
    new_word_list = []
    for v in lines:
        i = v[:-1]
        new_word_list.append(i)
    while True:
        game_word = new_word_list[int(random() * len(new_word_list))]
        if game_word[0] not in capital_letters and not len(game_word) < 5 and not len(game_word) > 12:
            break
        else:
            continue
    return game_word
while True:
    os.system("cls")
    print("Choose:")
    print()
    print("1. New Game")
    print("2. Load Game")
    print("3. Quit")
    print()
    answer = input()
    if answer == "1":
        game_word = get_game_word()
        correct_guesses = []
        incorrect_guesses = []
        all_guesses = []
        incorrects_remaining = 6
        while True:
            os.system("cls")
            print(f"Incorrect guesses: {incorrect_guesses}")
            print(f"Correct guesses: {correct_guesses}")
            print(f"Turns remaining: {incorrects_remaining}")
            print()
            print(populate_mystery_word(game_word))
            if not " _ " in populate_mystery_word(game_word):
                print("You win! Press 'Enter' to go back to the main menu.")
                input()
                break
            print()
            guess = input("What's your guess? (Enter 'save' at any time to save your game)")
            if guess == "":
                continue
            if guess.lower() == "save":
                while True:
                    file_name = input("Enter your save name: ")
                    if os.path.exists(f"./save_files/{file_name}.txt"):
                        answer == input("That exists already. Overwrite?")
                        if answer.lower() == "y" or answer.lower() == "yes":
                            break
                        else:
                            continue
                    else:
                        if os.path.exists("./save_files/") == False:
                            os.mkdir("./save_files/")
                        save_game = [game_word, correct_guesses, incorrect_guesses, all_guesses, incorrects_remaining]
                        save_file = open(f"./save_files/{file_name}.txt", "w")
                        for v in save_game:
                            if isinstance(v, list):
                                write = ",".join(v)
                                save_file.write(write + "\n")
                            elif isinstance(v, int):
                                save_file.write(str(v) + "\n")
                            else:
                                save_file.write(v + "\n")
                        input("You have saved your game. Press 'Enter' to go back to the menu. ")
                    break
                break
            if guess in all_guesses:
                print("You already guessed that. Press 'Enter' to continue.")
                input()
            elif guess in game_word:
                correct_guesses.append(guess)
                all_guesses.append(guess)
            else:
                incorrect_guesses.append(guess)
                all_guesses.append(guess)
                incorrects_remaining -= 1
            if incorrects_remaining == 0:
                incorrect_guesses.append(guess)           
                all_guesses.append(guess)
                incorrects_remaining -= 1       
                print(f"game over - the word was {game_word}. Press 'Enter' to go back to the main menu.")
                input()
                break
    elif answer == "2":
        if not os.path.exists("./save_files/"):
            input("You don't have any saved games to load. Press Enter to go back to the menu. ")
        print("Pick a file:")
        c = 0
        for v in os.listdir("./save_files/"):
            c += 1
            print(f"{c}. {v}")
        answer = input()
        answer = os.listdir('./save_files/')[int(answer) - 1]
        load_file = open(f"./save_files/{answer}")
        lines = load_file.readlines()
        load_file.close()
        newlines = []
        for v in lines:
            newlines.append(v[:-1])
        game_word = newlines[0]
        correct_guesses = newlines[1].split(",")
        incorrect_guesses = newlines[2].split(",")
        all_guesses = newlines[3].split(",")
        incorrects_remaining = int(newlines[4])
        while True:
            os.system("cls")
            print(f"Incorrect guesses: {incorrect_guesses}")
            print(f"Correct guesses: {correct_guesses}")
            print(f"Turns remaining: {incorrects_remaining}")
            print()
            print(populate_mystery_word(game_word))
            if not " _ " in populate_mystery_word(game_word):
                print("You win! Press 'Enter' to go back to the main menu.")
                input()
                break
            print()
            guess = input("What's your guess? (Enter 'save' at any time to save your game)")
            if guess == "":
                continue
            if guess.lower() == "save":
                while True:
                    file_name = input("Enter your save name: ")
                    if os.path.exists(f"./save_files/{file_name}.txt"):
                        answer == input("That exists already. Overwrite?")
                        if answer.lower() == "y" or answer.lower() == "yes":
                            break
                        else:
                            continue
                    else:
                        if os.path.exists("./save_files/") == False:
                            os.mkdir("./save_files/")
                        save_game = [game_word, correct_guesses, incorrect_guesses, all_guesses, incorrects_remaining]
                        save_file = open(f"./save_files/{file_name}.txt", "w")
                        for v in save_game:
                            if isinstance(v, list):
                                write = ",".join(v)
                                save_file.write(write + "\n")
                            elif isinstance(v, int):
                                save_file.write(str(v) + "\n")
                            else:
                                save_file.write(v + "\n")
                        input("You have saved your game. Press 'Enter' to go back to the menu. ")
                    break
                break
            if guess in all_guesses:
                print("You already guessed that. Press 'Enter' to continue.")
                input()
            elif guess in game_word:
                correct_guesses.append(guess)
                all_guesses.append(guess)
            else:
                incorrect_guesses.append(guess)
                all_guesses.append(guess)
                incorrects_remaining -= 1
            if incorrects_remaining == 0:
                incorrect_guesses.append(guess)           
                all_guesses.append(guess)
                incorrects_remaining -= 1       
                print(f"game over - the word was {game_word}. Press 'Enter' to go back to the main menu.")
                input()
                break
    elif answer == "3":
        os.system("cls")
        print("Thanks for playing!")
        break
    else:
        continue