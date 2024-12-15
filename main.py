import os
import requests
from colorama import Style, Fore, init
init()
import webbrowser
import time

def watermark():
    with open('bin/watermark.txt', "r", encoding='utf-8') as f:
        for line in f.readlines():
            print(Fore.RED + line.strip() + Style.RESET_ALL)

def main():
    os.system("cls")
    watermark()
    print(Fore.RED + "Welcome to Aspect Webhook Nuker!" + Style.RESET_ALL)
    print(Fore.RED + "1) Nuke Webhook\n2) Delete Webhook\n3) Discord" + Style.RESET_ALL)
    choice = input()
    if choice == "1":
        print(Fore.RED + "Webhook? " + Style.RESET_ALL)
        webhook = input()
        print(Fore.RED + "Message? " + Style.RESET_ALL)
        msg = input()

        spammer(webhook, msg)
    elif choice == "2":
        print(Fore.RED + "Webhook? " + Style.RESET_ALL)
        webhook = input()

        delete(webhook)
    elif choice == "3":
        discord()
    else:
        print(Fore.RED + "[-] Invalid choice" + Style.RESET_ALL)
        main()

def spammer(webhook, msg):
    data = {
        'content': '@everyone' + msg,
        'username': 'aspect free nuker - https://github.com/ripcozmic/Aspect-Webhook-Nuker',
        'avatar_url': 'https://i.imgur.com/fWZlGSg.gif'
    }

    while True:
        x = requests.post(webhook, json=data)

        if x.status_code == 204:
            print(Fore.CYAN + f"[+] Successfully sent message: {msg}" + Style.RESET_ALL)
            time.sleep(0.1)
        else:
            print(Fore.RED + f"[-] Couldn't send message!" + Style.RESET_ALL)

def delete(webhook):
    x = requests.delete(webhook)

    if x.status_code == 204:
        print(Fore.CYAN + f"[+] Successfully deleted webhook!" + Style.RESET_ALL)
    else:
        print(Fore.RED + f"[-] Couldn't delete webhook!" + Style.RESET_ALL)

def discord():
    webbrowser.open("https://discord.gg/4PwxBqnXKu")

if __name__ == "__main__":
    main()