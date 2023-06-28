from random import randint

COL_GREEN = '\033[38;5;46m'
COL_CYAN = '\033[38;5;51m'
COL_YELLOW = '\033[38;5;190m'
COL_RESET = '\033[0m'

numberOfDice = 1
numberOfSides = 6
globalCommand = ['exit']
while True:
    try:
        numberOfSides = input(f"{COL_CYAN}Enter the number of sides in dice: {COL_RESET}")
        numberOfSides = int(numberOfSides) if numberOfSides.isdigit() else numberOfSides
        if type(numberOfSides) == str and numberOfSides.lower() == 'exit':
            raise KeyboardInterrupt
        if type(numberOfSides) == str and numberOfSides.lower() not in globalCommand:
            raise ValueError
        if type(numberOfSides) == int and numberOfSides < 2:
            raise ValueError
        break
    except ValueError:
        print(f"{COL_YELLOW}Please enter valid number. {COL_RESET}")
        continue
    except KeyboardInterrupt:
        print(f"\n\n{COL_CYAN}Bye!{COL_RESET}")
        exit(0)

while True:
    try:
        numberOfDice = input(f"{COL_CYAN}Enter the number of dices: {COL_RESET}")
        numberOfDice = int(numberOfDice) if numberOfDice.isdigit() else numberOfDice
        if type(numberOfSides) == str and numberOfDice.lower() == 'exit':
            raise KeyboardInterrupt
        if type(numberOfDice) == str and numberOfDice.lower() not in globalCommand:
            raise ValueError
        if type(numberOfSides) == int and numberOfDice < 1:
            raise ValueError
        break
    except ValueError:
        print(f"{COL_YELLOW}Please enter valid number. {COL_RESET}")
        continue
    except KeyboardInterrupt:
        print(f"\n\n{COL_CYAN}Bye!{COL_RESET}")
        exit(0)

while True:
    try:
        for i in range(numberOfDice):
            print(f"{COL_GREEN}{randint(1,numberOfSides)}{COL_RESET}", end=" ")
        print("\n")
        if (input(f"{COL_CYAN}Press Enter to roll again. {COL_RESET}") == 'exit'):
            raise KeyboardInterrupt
    except KeyboardInterrupt:
        print(f"\n\n{COL_CYAN}Bye!{COL_RESET}")
        exit(0)