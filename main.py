from colorama import Fore, Back, Style
from os import system

# default = "email:password:token"
system("title " + "Discord Token Formatter - https://github.com/Corteizlx3")
count = 0
default = []
logo = Fore.RED + '''

  █████▒ ▒█████   ██▀███   ███▄ ▄███▓ ▄▄▄      ▄▄▄█████▓▄▄▄█████▓▓█████  ██▀███  
▓██   ▒ ▒██▒  ██▒▓██ ▒ ██▒▓██▒▀█▀ ██▒▒████▄    ▓  ██▒ ▓▒▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒
▒████ ░ ▒██░  ██▒▓██ ░▄█ ▒▓██    ▓██░▒██  ▀█▄  ▒ ▓██░ ▒░▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒
░▓█▒  ░ ▒██   ██░▒██▀▀█▄  ▒██    ▒██ ░██▄▄▄▄██ ░ ▓██▓ ░ ░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄  
░▒█░    ░ ████▓▒░░██▓ ▒██▒▒██▒   ░██▒ ▓█   ▓██▒  ▒██▒ ░   ▒██▒ ░ ░▒████▒░██▓ ▒██▒
 ▒ ░    ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒░   ░  ░ ▒▒   ▓▒█░  ▒ ░░     ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░
 ░        ░ ▒ ▒░   ░▒ ░ ▒░░  ░      ░  ▒   ▒▒ ░    ░        ░     ░ ░  ░  ░▒ ░ ▒░
 ░ ░    ░ ░ ░ ▒    ░░   ░ ░      ░     ░   ▒     ░        ░         ░     ░░   ░ 
            ░ ░     ░            ░         ░  ░                     ░  ░   ░     
'''
def totoken():
    f = open('tokens.txt', 'r')
    Lines = f.readlines()
    for lines in Lines:
        global token
        global count
        count += 1
        default = lines
        split = default.split(":")
        # print(split)
        token = split[2]
        # print(token)
        f = open('results/token.txt','a')
        f.writelines(token)

def emailtopass():
    f = open('tokens.txt', 'r')
    Lines = f.readlines()
    for lines in Lines:
        global token
        global count
        count += 1
        default = lines
        split = default.split(":")
        # print(split)
        token = split[0] +":"+ split[1] + "\n"
        # print(token)
        f = open('results/emailpassword.txt','a')
        f.writelines(token)
print(logo)
print(Fore.WHITE+Style.BRIGHT+"                            https://github.com/Corteizlx3\n\n")
print(Fore.CYAN+"[1] email:password:token --> token")
print(Fore.CYAN+"[2] email:password:token --> email:pass")
print(Fore.CYAN+"[3] EXIT\n")
choice = input(Fore.BLUE + "User: " + Fore.MAGENTA)
if choice == "1":
    totoken()
    print("\n "+Fore.GREEN+"[+]"+Fore.MAGENTA+" Converted email:password:token "+Fore.GREEN+"--->"+Fore.MAGENTA+" token Successfully.")
    print("        "+Fore.RED+"[>]"+Fore.MAGENTA+" If You Have Any Suggestions Contact Me On Github")
elif choice == "2":
    emailtopass()
    print("\n "+Fore.GREEN+"[+]"+Fore.MAGENTA+" Converted email:password:token "+Fore.GREEN+"--->"+Fore.MAGENTA+" email:password Successfully.")
    print("        "+Fore.RED+"[>]"+Fore.MAGENTA+" If You Have Any Suggestions Contact Me On Github")
elif choice == "3":
    print(Fore.RED+"        [>]"+Fore.MAGENTA+" Exiting...")



