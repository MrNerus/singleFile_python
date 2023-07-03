# pip install qrcode
# pip install Pillow

import qrcode

COL_GREEN = '\033[38;5;46m'
COL_CYAN = '\033[38;5;51m'
COL_YELLOW = '\033[38;5;190m'
COL_RESET = '\033[0m'

def inputText(x: str, notNull = True, options = []) -> str:
    while True:
        try:
            if bool(options):
                print(f"{COL_CYAN}Choices:{COL_RESET}", end=" ")
                for i in options:
                    print(f"{COL_YELLOW}{i}{COL_RESET}", end=" | ")
                print("")
            a = input(f'{COL_CYAN}Enter {x}: {COL_RESET}')
            if notNull and a == "":
                raise ValueError
            if bool(options) and a not in options:
                raise ValueError
            return a
        except KeyboardInterrupt:
            print(f"\n\n{COL_CYAN}Bye!{COL_RESET}")
            exit(0)
        except ValueError:
            print(f"{COL_YELLOW}Please enter proper text.{COL_RESET}")
            continue
          


class myQR:
    def __init__(self, size: int, padding: int):
        self.qr = qrcode.QRCode(box_size=size, border=padding)
    
    def createQR(self, text: str, fileName: str, fg: str, bg: str):
        self.qr.add_data(data = text)
        qrImage = self.qr.make_image(fill_color=fg, back_color=bg)
        qrImage.save(fileName)
        print(f"{COL_GREEN}QR Saved!{COL_RESET}")

globalCommand = ['exit']

def textGenNormal() -> str:
    return inputText("your text")

def textGenWifi() -> str:
    #  img = pyqrcode.create(f"WIFI:S:{data1};T:{data2};P:{data3};;")
    # WEP, WPA/WPA2, FREE
    ssid = inputText("your Network Name")
    security = inputText("encryption type of wifi", options=["None", "WPA/WPA2", "WEP"])
    password = inputText("your password", notNull=False)
    return f"WIFI:S:{ssid};T:{security};P:{password};;"

def textGenURL() -> str:
    url = inputText("a link")
    return f"URLTO:{url}"

def textGenEmail() -> str:
    email = inputText("your email")
    cc = inputText("cc")
    bcc = inputText("bcc")
    subject = inputText("subject")
    body = inputText("body")
    return f"mailto:{email}?cc={cc}&bcc={bcc}&subject={subject}&body={body}"

def textGenTel() -> str:
    phNo = inputText("your phone number")
    return f"tel:{phNo}"
def textGenSMS() -> str:
    phNo = inputText("a receiver's phone number")
    message = inputText("your message")
    return f"SMSTO:{phNo}:{message}"
def textGenGeo() -> str:
    latitude = inputText("latitude")
    longitude = inputText("longitude")
    altitude = inputText("altitude")
    return f"geo:{latitude},{longitude},{altitude}"

def textGenContact() -> str: ...
#     return '''BEGIN:VCARD
# VERSION:3.0
# N:{lname};{fname}
# FN:{fname} {lname}
# TITLE:{title}
# ORG:{org}
# URL:{url}
# EMAIL;TYPE=INTERNET:{email}
# TEL;TYPE=voice,work,pref:{phw}
# TEL;TYPE=voice,home,pref:{phh}
# TEL;TYPE=voice,cell,pref:{mob}
# TEL;TYPE=fax,work,pref:{fxw}
# TEL;TYPE=fax,home,pref:{fxh}
# ADR:;;{street};{city};{state};{postal};{country}
# END:VCARD'''
# # Not implemented due to my limited knowledge



def main():
    modes = {"1":"Normal text", "2":"Wifi", "3":"URL", "4":"Email", "5":"Telephone", "6": "SMS", "7": "Geo"}
    for i in modes:
        print(f"{COL_YELLOW}{i}{COL_RESET} = {COL_CYAN}{modes[i]}{COL_RESET}")
    choice = inputText("your choice", options=list(modes.keys()))
    text = ""
    match choice:
        case "1":
            text = textGenNormal()
        case "2":
            text = textGenWifi()
        case "3":
            text = textGenURL()
        case "4":
            text = textGenEmail()
        case "5":
            text = textGenTel()
        case "6":
            text = textGenSMS()
        case "7":
            text = textGenGeo()
        case default:
            print(f"{COL_YELLOW}This should not happen.{COL_RESET}")
    filename = inputText("save file name")
    myqr = myQR(size=30, padding=2)
    myqr.createQR(text=text, fileName=filename, fg="#000000", bg="#ffffff")

if __name__ == "__main__":
    main()