import itertools


COL_GREEN = '\033[38;5;46m'
COL_CYAN = '\033[38;5;51m'
COL_RED = '\033[38;5;196m'
COL_YELLOW = '\033[38;5;190m'
COL_RESET = '\033[0m'


password = "ard"

def fileImport():
    while True:
        try: 
            filePath = input(f"{COL_CYAN}Enter a file path: {COL_RESET}")
            if filePath == "":
                raise ValueError
            file = open(filePath, 'r')
            return file
        except ValueError:
            print(f"{COL_YELLOW}Please enter a file path..{COL_RESET}")
        except FileNotFoundError:
            print(f"{COL_YELLOW}That file couldnot be located..{COL_RESET}")
        except KeyboardInterrupt:
            print(f"\n\n{COL_CYAN}Bye!{COL_RESET}")
            exit(0)

def fileRead():
    try:
        words: list(str) = fileImport().read().splitlines()
        for i,j in enumerate(words):
            print(COL_YELLOW, i, j, COL_RESET, end="\t")
            if password == j:
                print(f"{COL_GREEN}Password Matched!{COL_RESET}")
                exit(0)
            else:
                print(f"{COL_RED}Not Match!{COL_RESET}")
    except KeyboardInterrupt:
        print(f"\n\n{COL_CYAN}Bye!{COL_RESET}")
        exit(0)

def bruteforce():
    charLen = 4
    while True:
        try:
            charLen = int(input(f"{COL_CYAN}Enter the number of character in passowrd: {COL_RESET}"))
            if charLen <= 0:
                raise ValueError
            break
        except ValueError:
            print(f"{COL_YELLOW}Please enter a valid number..{COL_RESET}")
        except KeyboardInterrupt:
            print(f"\n\n{COL_CYAN}Bye!{COL_RESET}")
            exit(0)
    chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    buffer = ["0" for i in range(charLen)]
    final = ["z" for i in range(charLen)]
    attemptCounter = 1

    for i in itertools.product(chars, repeat = charLen):
        print(f"{COL_YELLOW}{attemptCounter} {''.join(i)}{COL_RESET}", end="\t")
        if ''.join(i) == password:
            print(f"{COL_GREEN}Password Matched!{COL_RESET}")
            break
        attemptCounter += 1
        print(f"{COL_RED}Not Match!{COL_RESET}")

def makeChoice():
    choices = {"1": 'Wordlist', "2":"Bruteforce"}
    while True:
        try:
            print(f"{COL_CYAN}Choices: {COL_RESET}", end="")
            for i in choices:
                print(f"{COL_YELLOW}{i}{COL_CYAN} for {choices[i]}", end = "\t")
            print("")
            choice = input(f"{COL_CYAN}Enter your choice: {COL_RESET}")
            if len(choice) == 0:
                raise ValueError
            if choice not in choices:
                raise ValueError
            if choice == "1":
                fileRead()
            if choice == '2':
                bruteforce()
        except ValueError:
            print(f"{COL_YELLOW}Please enter a valid number..{COL_RESET}")
        except KeyboardInterrupt:
            print(f"\n\n{COL_CYAN}Bye!{COL_RESET}")
            exit(0)

if __name__=="__main__":
    makeChoice()