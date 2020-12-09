# q22

import time
import requests
import sys
import socket
from colorama import Fore

def __requests__():
    print(Fore.RED + "\n[!] - The 3 Sec Clear All Text ;)")
    time.sleep(3)
    os.system("clear")
    try:
        time.sleep(2)
        print(Fore.YELLOW + "Hello Welcome ;) ")
        time.sleep(2)
        target = input(Fore.BLUE +"\n[" + Fore.RED + "*" + Fore.BLUE + "]" + Fore.RED + " ~ " + Fore.YELLOW + "Enter Your Address Target" + Fore.GREEN + " ==>  ")
        if target == "" or None:
            try:
                time.sleep(2)
                print(Fore.BLUE + "\n[" + Fore.YELLOW + "!" + Fore.BLUE + "]" + Fore.YELLOW + " ~ " + Fore.RED + "Error" + Fore.BLUE  + " : " + Fore.RED + "Your Target Is Not Found ;(")
                time.sleep(2)
                sys.exit()
            except:
                pass
        time.sleep(2)
        socket = socket.gethostbyname(target)
        print(Fore.BLUE + "\n[" + Fore.RED + "+" + Fore.BLUE + "]" + Fore.RED + " ~ " + Fore.GREEN + "Your Ip Target : " + socket)
        time.sleep(2)
        r = requests.git("https://who.is/whois-ip/ip-address/" + socket)
        try:
            print("<pre>")
        except:
            pass
    except:
        pass
__requests__()    
