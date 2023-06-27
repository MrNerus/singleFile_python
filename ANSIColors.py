COL_GREEN = '\033[38;5;46m'  # Green Text
COL_GREEN_BG = '\033[48;5;46m'  # Green Text
COL_RESET = '\033[0m'  # reset to the defaults
COL_YELLOW = '\033[38;5;226m'  # Yellow Text
COL_LIGHT_YELLOW = '\033[38;5;228m'  # Light Yellow Text
COL_CYAN = '\033[38;5;51m'  # Cyan Color
COL_RED = '\033[38;5;196m'  # Red Color
COL_BLUE = '\033[38;5;21m'  # Blue Color
COL_ORANGE = '\033[38;5;202m'  # Blue Color
COL_DARK_GREEN = '\033[38;5;22m'  # Dark Green Color

print("For text color.        COL_<NAME> = '\\033[38;5;<VALUE>m'")
print(
    f"Eg...                  {COL_CYAN}COL_GREEN {COL_BLUE}= {COL_ORANGE}'\\033[38;5;46m'  {COL_DARK_GREEN}# Green Color   {COL_LIGHT_YELLOW}--->   {COL_GREEN}abc{COL_RESET}\n")
print("For Background color.  COL_<NAME> = '\\033[48;5;<VALUE>m'")
print(
    f"Eg...                  {COL_CYAN}COL_GREEN_BG {COL_BLUE}= {COL_ORANGE}'\\033[48;5;46m'  {COL_DARK_GREEN}# Green Background Color   {COL_LIGHT_YELLOW}--->   {COL_GREEN_BG}abc{COL_RESET}\n")
print(
    f"To reset color,        {COL_CYAN}COL_RESET {COL_BLUE}={COL_ORANGE} '\\033[0m'  {COL_DARK_GREEN}  # Reset color   {COL_LIGHT_YELLOW}--->   {COL_RESET}This is your default text.\n")
print('Choose color name at your own. Use value for respective color\n')


def display(col_code):
    color = '\033[38;5;' + str(col_code) + 'm'
    # disp = f"'\\033[38;5;{str(col_code)}m'"
    return (color + f'{col_code}' + '\033[0m' + ' ')


start_number = -1


def numbers():
    global start_number
    start_number += 1
    return start_number

def printer(numberOfLines):
    for i in range(0,numberOfLines):
        print(f'{display(numbers())}{display(numbers())}{display(numbers())}{display(numbers())}{display(numbers())}{display(numbers())}')
    print('')

print('For standard colors')
print(f'{display(numbers())}{display(numbers())}{display(numbers())}{display(numbers())}{display(numbers())}{display(numbers())}{display(numbers())}{display(numbers())}')
print('')
print('For brighter standard colors')
print(f'{display(numbers())}{display(numbers())}{display(numbers())}{display(numbers())}{display(numbers())}{display(numbers())}{display(numbers())}{display(numbers())}')
print('')
print(f'For Coldest shade')
printer(6)

print(f'For 20% Warm shade')
printer(6)

print(f'For 40% Warm shade')
printer(6)

print(f'For 60% Warm shade')
printer(6)

print(f'For 80% Warm shade')
printer(6)

print('For Hottest shade')
printer(6)

print('For Gray-Scale')
printer(4)
print("")

print(
    f"USE CASE: {COL_CYAN}COL_GREEN {COL_BLUE}= {COL_ORANGE}'\\033[38;5;46m'  {COL_DARK_GREEN}# Green Color{COL_RESET}")
print(
    f"          {COL_CYAN}COL_RESET {COL_BLUE}= {COL_ORANGE}'\\033[0m'  {COL_DARK_GREEN}# Color Reset{COL_RESET}")
print(
    f"          {COL_LIGHT_YELLOW}print{COL_YELLOW}({COL_GREEN}COL_GREEN {COL_BLUE}+ {COL_ORANGE}'This is colored text.'{COL_BLUE} + {COL_GREEN}COL_RESET{COL_YELLOW}){COL_RESET}")
print(COL_RED + "Make sure to reset color after you are done using it." + COL_RESET)
