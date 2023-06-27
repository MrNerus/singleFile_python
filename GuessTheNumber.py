from random import randint

COL_GREEN = '\033[38;5;46m' 
COL_AQUA = '\033[38;5;51m'
COL_YELLOW = '\033[38;5;190m'
COL_RESET = '\033[0m'

lowerLimit = 0
upperLimit = 0

counter = 0
guessLimit = 0

# Take input for lower limit
while True:
    try:
        lowerLimit = int(input(f"{COL_AQUA}Enter a lower number: {COL_RESET}"))
        break
    
    except ValueError:
        print(f"{COL_YELLOW}Please Enter valid number. {COL_RESET}")
        continue
    
    except KeyboardInterrupt:
        print(f"{COL_AQUA}Game Terminated. {COL_RESET}")
        exit(0)

# Take input for upper limit
while True:
    try:
        upperLimit = int(input(f"{COL_AQUA}Enter a upper number: {COL_RESET}"))
        if upperLimit <= lowerLimit:
            raise ValueError
        break

    except ValueError:
        print(f"{COL_YELLOW}Please Enter valid number. {COL_RESET}")
        continue
    
    except KeyboardInterrupt:
        print(f"{COL_AQUA}Game Terminated. {COL_RESET}")
        exit(0)

# Take input for guess limit
while True:
    try:
        guessLimit = int(input(f"{COL_AQUA}Enter a number of guess allowed [0 for unmimited]: {COL_RESET}"))
        break

    except ValueError:
        print(f"{COL_YELLOW}Please Enter valid number. {COL_RESET}")
        continue
    
    except KeyboardInterrupt:
        print(f"{COL_AQUA}Game Terminated. {COL_RESET}")
        exit(0)

limitedGuess = bool(guessLimit)

while True:
    computerGuess = randint(lowerLimit, upperLimit)
    myGuess = 0
    
    # InGame Logics
    while True:
        if counter == guessLimit:
            print(f"{COL_YELLOW}Attempt over! The number was {computerGuess}.{COL_RESET}")
            print(f"{COL_AQUA}\n\nNew Game {COL_RESET}")
            counter = 0
            break
        try:
            myGuess = int(input(f"{COL_AQUA}Enter your guess [Attempt No.: {counter + 1}]: {COL_RESET}"))
            if (myGuess < lowerLimit or myGuess > upperLimit):
                raise ValueError
            counter += 1
            if (myGuess < computerGuess):
                print(f"{COL_YELLOW}More than that. {COL_RESET}")
                continue
            if (myGuess > computerGuess):
                print(f"{COL_YELLOW}Less than that. {COL_RESET}")
                continue
            print(f"{COL_GREEN}Bingo! you took {counter} guesses. {COL_RESET}")
            print(f"{COL_AQUA}\n\nNew Game {COL_RESET}")
            counter = 0
            break

        except ValueError:
            print(f"{COL_YELLOW}Please Enter valid number. {COL_RESET}")
            continue

        except KeyboardInterrupt:
            print(f"{COL_AQUA}Game Terminated. {COL_RESET}")
            exit(0) 
    
        
    
            

      


