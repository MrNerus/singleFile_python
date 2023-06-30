from random import choice

COL_GREEN = '\033[38;5;46m'
COL_RED = '\033[38;5;196m'
COL_CYAN = '\033[38;5;51m'
COL_YELLOW = '\033[38;5;190m'
COL_RESET = '\033[0m'

playCommand = {
    'rock' :('scissors','paper'),
    'paper':('rock','scissors'), 
    'scissors':('paper','rock')
    }
globalCommand = ['exit']

counter = [0,0,0]

while True:
    playerChoice = ""
    computerChoice = choice(tuple(playCommand.keys()))
    while True:
        try:
            print(f"{COL_CYAN}[{COL_RESET}", end=" ")
            for i in playCommand:
                print(f"{COL_YELLOW}{i}{COL_RESET}", end=" ")
            print(f"{COL_CYAN}]{COL_RESET}")
            playerChoice = input(f"{COL_CYAN}Enter your choice: {COL_RESET}").strip().lower()
            if playerChoice in playCommand:
                break
            if playerChoice == 'exit':
                raise KeyboardInterrupt
            if playerChoice not in globalCommand:
                raise ValueError
        except KeyboardInterrupt:
            print(f"\n\n{COL_CYAN}Bye!{COL_RESET}")
            exit(0)
        except ValueError:
            print(f"{COL_YELLOW}Please enter valid input!{COL_RESET}")
            continue

    print(f"{COL_GREEN}Computer Choosed: {COL_YELLOW}{computerChoice}{COL_RESET}")
    if computerChoice == playCommand[playerChoice][1]:
        print(f"{COL_RED}You Lost!{COL_RESET}")
        counter[0] += 1
    elif computerChoice == playCommand[playerChoice][0]:
        print(f"{COL_GREEN}You Won!{COL_RESET}")
        counter[2] += 1
    elif computerChoice == playerChoice:
        print(f"{COL_YELLOW}It is tie!{COL_RESET}")
        counter[1] += 1
    print(f"{COL_CYAN}Computer: {COL_YELLOW}{counter[0]}{COL_RESET}\n{COL_CYAN}Tie: {COL_YELLOW}{counter[1]}{COL_RESET}\n{COL_CYAN}You: {COL_YELLOW}{counter[2]}{COL_RESET}\n")

    
    
    
            


