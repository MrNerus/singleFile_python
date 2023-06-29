# https://random-word-api.herokuapp.com/word
# https://github.com/RazorSh4rk/random-word-api
# https://github.com/RazorSh4rk

import requests

COL_GREEN = '\033[38;5;46m'
COL_CYAN = '\033[38;5;51m'
COL_YELLOW = '\033[38;5;190m'
COL_RED = '\033[38;5;196m'
COL_RED_DARK = '\033[38;5;88m'
COL_RESET = '\033[0m'

globalCommand = ['exit']

while True:
    word = []
    usedWord = []
    discoveredWord = []
    numberOfLives = 3
    try:
        response = requests.get("https://random-word-api.herokuapp.com/word")
        if (response.status_code == 200):
            word = list(response.text)[2:-2]
        else:
            print(f"{COL_YELLOW}Something went wrong getting word from web!{COL_RESET}")
            print(f"{COL_CYAN}Status Code: {COL_YELLOW}{response.status_code}{COL_RESET}")
            print(f"{COL_CYAN}Please check your connection and try again later..{COL_RESET}")
            raise KeyboardInterrupt
    except KeyboardInterrupt:
        print(f"\n\n{COL_CYAN}Bye!{COL_RESET}")
        exit(0)
    except requests.exceptions.ConnectionError:
        print(f"{COL_YELLOW}Something went wrong connecting to the internet!{COL_RESET}")
        print(f"{COL_CYAN}Please check your connection and try again later..{COL_RESET}")
        print(f"\n\n{COL_CYAN}Bye!{COL_RESET}")
        exit(0)

    discoveredWord = [None for i in word]
    while True:
        try:
            numberOfLives = input(f"{COL_CYAN}Enter the number of lives you have: {COL_RESET}")
            numberOfLives = int(numberOfLives) if numberOfLives.isdigit() else numberOfLives
            if type(numberOfLives) == str and numberOfLives.lower() == 'exit':
                raise KeyboardInterrupt
            if type(numberOfLives) == str and numberOfLives.lower() not in globalCommand:
                raise ValueError
            if type(numberOfLives) == int and (numberOfLives < 1 or numberOfLives > 10):
                raise ValueError
            break
        except ValueError:
            print(f"{COL_YELLOW}Please enter valid number. {COL_RESET}")
            continue
        except KeyboardInterrupt:
            print(f"\n\n{COL_CYAN}Bye!{COL_RESET}")
            exit(0)

    remainingLife = numberOfLives

    while True:
        if None not in discoveredWord:
            print(f"{COL_GREEN}You Won! {COL_CYAN}The word was: {COL_RESET}", end="")
            for i in word:
                print(f"{COL_YELLOW}{i}{COL_RESET}", end="")
            print ("\n")
            try:
                playAgain = input(f"{COL_CYAN}Press Enter to play again. {COL_RESET}")
                if playAgain == "":
                    break
                if playAgain.lower() == 'exit':
                    raise KeyboardInterrupt
                if playAgain not in globalCommand:
                    raise ValueError
            except KeyboardInterrupt:
                print(f"\n\n{COL_CYAN}Bye!{COL_RESET}")
                exit(0)
            except ValueError:
                print(f"{COL_YELLOW}Please enter valid command. {COL_RESET}")
                continue
        if remainingLife < 0:
            print(f"{COL_RED}You lost! {COL_CYAN}The word was: {COL_RESET}", end="")
            for i in word:
                print(f"{COL_YELLOW}{i}{COL_RESET}", end="")
            print ("\n")
            try:
                playAgain = input(f"{COL_CYAN}Press Enter to play again. {COL_RESET}")
                if playAgain == "":
                    break
                if playAgain.lower() == 'exit':
                    raise KeyboardInterrupt
                if playAgain not in globalCommand:
                    raise ValueError
            except KeyboardInterrupt:
                print(f"\n\n{COL_CYAN}Bye!{COL_RESET}")
                exit(0)
            except ValueError:
                print(f"{COL_YELLOW}Please enter valid command. {COL_RESET}")
                continue
        char = ""

        print(f"{COL_CYAN}Used Characters: {COL_RESET}", end="")
        for i in usedWord:
            print(f"{COL_YELLOW}{i}{COL_RESET}", end=" ")
        print("")

        for i in range(remainingLife):
            print(f"❤︀",end="")
        for i in range(numberOfLives - remainingLife):
            print(f"💔", end="")
        print("")

        print(f"{COL_CYAN}Discovered Word: {COL_RESET}", end="")
        for i in discoveredWord:
            if i != None:
                print(f"{COL_YELLOW}{i}{COL_RESET}", end=" ")
            else:
                print(f"{COL_YELLOW}_{COL_RESET}", end=" ")
        print("")

        try:
            while True:
                char = input(f"{COL_CYAN}Enter your Character: {COL_RESET}")
                if len(char) == 1:
                    break
                if char.lower() == 'exit':
                    raise KeyboardInterrupt
                if char.lower() not in globalCommand:
                    print(f"{COL_YELLOW}Please enter valid character. {COL_RESET}")
                    raise ValueError
                if char in usedWord:
                    print(f"{COL_YELLOW}Already choosen. {COL_RESET}")
                    continue
        except KeyboardInterrupt:
            print(f"\n\n{COL_CYAN}Bye!{COL_RESET}")
            exit(0)
        except ValueError:
            print(f"{COL_YELLOW}Please enter valid character. {COL_RESET}")
            continue
        
        if char in word:
            print(f"{COL_GREEN}Yes!{COL_RESET}")
            for i,j in enumerate(word):
                if j == char:
                    discoveredWord[i] = char
        else:
            print(f"{COL_RED}Nope!{COL_RESET}")
            remainingLife -= 1
        
        usedWord.append(char)
