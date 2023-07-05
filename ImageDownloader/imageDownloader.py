import requests
from os.path import exists

COL_GREEN = '\033[38;5;46m'
COL_CYAN = '\033[38;5;51m'
COL_YELLOW = '\033[38;5;190m'
COL_RED = '\033[38;5;196m'
COL_RESET = '\033[0m'


def textInput(x, options=[]):
    while True:
        try:
            if bool(options):
                print(f"{COL_CYAN}Choices: {COL_RESET}", end="")
                for i in options:
                    print(f"{COL_YELLOW}{i}{COL_RESET}", end=" | ")
                print("\b\b")
            userInput = input(f"{COL_CYAN}Enter {x}: {COL_RESET}")
            if userInput == "":
                raise ValueError
            if bool(options) and userInput.lower() not in options:
                raise ValueError
            return userInput
        except ValueError:
            print(f"{COL_YELLOW}Please enter proper value..{COL_RESET}")
        except KeyboardInterrupt:
            print(f"\n\n{COL_CYAN}Bye!{COL_RESET}")
            exit(0)


def download(url: str) -> bool:
    response = requests.get(url)
    if response.status_code == 200:
        img = response.content
        
        supportedExtensions = [".png", ".jpg", ".svg", ".jpeg", ".webp"]
        extension = ""
        for i in supportedExtensions:
            if i in url:
                extension = i
                break
        while True:
            imageName = textInput("name of image")    
            if not bool(extension):
                extension = textInput("image extension", supportedExtensions)
            if exists(f"./Image/{imageName}{extension}"):
                print(f"{COL_YELLOW}That name already exist. {COL_RESET}")
                continue
            break
        file = open(f"./Image/{imageName}{extension}", 'xb')
        file.write(img)
        file.close()
        return True
    return False

if __name__ == "__main__":
    while not download(textInput('url of image')):
        print(f"{COL_YELLOW}There was a problem downloading image.{COL_RESET}")
    else:
        print(f"{COL_GREEN}Image downloaded successfully.{COL_RESET}")
    
