import secrets
import datetime
import pyperclip

COL_GREEN = '\033[38;5;46m'
COL_CYAN = '\033[38;5;51m'
COL_YELLOW = '\033[38;5;190m'
COL_RED = '\033[38;5;196m'
COL_RESET = '\033[0m'



def getYN(x: str) -> bool:
    while True:
        try:
            userReply = input(f"{COL_CYAN}Do You want {x}? {COL_YELLOW}(Y/N){COL_CYAN}: {COL_RESET}")
            userReply = userReply.strip().lower()
            if userReply == 'y':
                return True
            if userReply == 'n':
                return False
            if userReply == 'exit':
                raise KeyboardInterrupt
            if userReply not in globalCommand:
                raise ValueError
        except KeyboardInterrupt:
            print(f"\n\n{COL_CYAN}Bye!{COL_RESET}")
            exit(0)
        except ValueError:
            print(f"{COL_YELLOW}Please enter valid value. {COL_RESET}")
            continue

def getRequirement():
    global uppercaseRequired; uppercaseRequired = getYN("UpperCase Character")
    global lowercaseRequired; lowercaseRequired = getYN("LowerCase Character")
    global numberRequired;    numberRequired = getYN("Numeric Character")
    global specCharRequired;  specCharRequired = getYN("Special Character")
    global extendedSet;       extendedSet = getYN("to use Extended CharacterSet (Recommended N)")

def getLen() -> int:
    while True:
        try:
            userReply = input(f"{COL_CYAN}Enter the number of characters in password [4-64]: {COL_RESET}")

            userReply = userReply.strip().lower()
            if userReply.isdigit() and (int(userReply) >= 4 and int(userReply) <= 64):
                return int(userReply)
            if userReply.isdigit() and (int(userReply) < 4 or int(userReply) > 64):
                raise ValueError
            if userReply == 'exit':
                raise KeyboardInterrupt
            if userReply not in globalCommand:
                raise ValueError
        except KeyboardInterrupt:
            print(f"\n\n{COL_CYAN}Bye!{COL_RESET}")
            exit(0)
        except ValueError:
            print(f"{COL_YELLOW}Please enter valid value. {COL_RESET}")
            continue

def sequenceGen(ucR: bool, lcR: bool, numR: bool, scR :bool, pLen :int) -> list:
    passwordRuleList: list(bool) = [ucR, lcR, numR, scR]
    seq = [None for i in range(0, pLen)]
    seqIndex = [i for i in range(0, pLen)]
    pRulePointer = 0

    while None in seq:
        while True:
            pRulePointer = pRulePointer + 1 if pRulePointer < len(passwordRuleList) - 1 else 0

            if passwordRuleList[pRulePointer]:
                break
        pos = secrets.choice(seqIndex)
        seq[pos] = pRuleDict[pRulePointer]
        seqIndex.remove(pos)
    
    return seq
        
def passwordGen(seq: list, charSet: list) -> str:
    pswd = ""
    for i in seq:
        pswd += secrets.choice(charSet[pRuleDictR[i]])
    return pswd

def altCode(chars):
    number = ""
    for i in chars:
        number += str(f"{ord(i)} ")

    print(f"{COL_RED}{number}{COL_RESET}")

    if getYN("to save KeyCode in file"):
        x = datetime.datetime.now()
        l = f'{x.strftime("%Y")}{x.strftime("%m")}{x.strftime("%d")}{x.strftime("%H")}{x.strftime("%M")}{x.strftime("%S")}{x.strftime("%f")}'
        f = open(f"./NerusPGEN{l}.txt", "x")
        f.write(number)
        f.close()
        print(f'''\n{COL_YELLOW}Keep This Keycode safe..
file. {COL_GREEN}NerusPGEN{l}.txt{COL_YELLOW} is saved in this working directory.{COL_RESET}''')

globalCommand = ['exit']

uppercaseRequired: bool = True
lowercaseRequired: bool = True
numberRequired: bool = True
specCharRequired: bool = True
extendedSet: bool = False

pRuleDict =  {0:"U", 1:"L", 2:"N", 3:"S"}
pRuleDictR = {"U":0, "L":1, "N":2, "S":3}

uppercaseSet: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercaseSet:str = "abcdefghijklmnopqrstuvwxtz"
numberSet: str = "1234567890"
specialCharSet: str = "'!\"#$%&()*+,-./:;<=>?@[\]^_`{|}~"

euppercaseSet: str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ'
elowercaseSet:str = 'abcdefghijklmnopqrstuvwxyzαβγδεζηθικλμνξοπρστυφχψω'
enumberSet: str = '0123456789१२३४५६७८९०'
especialCharSet: str = '!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~￦￥￡￠＄﹩﷼꠸ℳ₿₠₡₢₣₤₥₦₧₨₩₪₫€₭₮₯₰₱₲₳₴₵₶₷₸₹₺₻₼₽₾៛฿௹૱৻৳৲߿߾؋֏ कखगघङचछजझञटठडढणतथदधनपफबभमयरलवसशषहअआइईउऊएऐओऔ'

if __name__ == "__main__":
    getRequirement()
    while (uppercaseRequired == False and lowercaseRequired == False and numberRequired == False and specCharRequired == False):
        print(f"{COL_YELLOW}Atleast one of first four character sets should be Y.. {COL_RESET}")
        getRequirement()
    passwordLen = getLen()
    passwordSeq = sequenceGen(ucR=uppercaseRequired, lcR=lowercaseRequired, numR=numberRequired, scR=specCharRequired, pLen=passwordLen)
    if extendedSet:
        password = passwordGen(passwordSeq, [euppercaseSet, elowercaseSet, enumberSet, especialCharSet])
    else:
        password = passwordGen(passwordSeq, [uppercaseSet, lowercaseSet, numberSet, specialCharSet])
    print(f"{COL_CYAN}Your password is: {COL_RED}{password}{COL_RESET}")
    altCode(password)
    if extendedSet:
        print(f'''{COL_YELLOW}Remember:{COL_RESET}
=> {COL_RED}Some characters are not Supported by many websites or applications.{COL_RESET}
=> {COL_YELLOW}A as alphabate and Α as capital alpha is different. Keep note of that.
    -> Your keyboard may not have such keys to type password. So, copy-paste is one option.
       But saving password in clipboard is terrible thing to do.
    -> Alt Key code for your password shall be provided.
       Keep that safe. May be on Notepad. Consider about safety though.{COL_RESET}
=> {COL_YELLOW}I am not responsible if you messed things up.{COL_RESET}''')
    print(f'''=> {COL_YELLOW}You better use password manager like {COL_CYAN}
    >> Microsoft Authunicator
    >> 1Password,
    >> LastPass,
    >> Keeper,
    >> Dashline,
    >> Bitwarden, etc.{COL_RESET}''')
    if getYN("to copy password in clipboard"):
        pyperclip.copy(password)
