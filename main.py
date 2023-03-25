import time, sys, os
from functions import auto, get_latest_cve, osint



class colors:
    GRAY ='\033[1;30;40m'
    RED = '\033[1;31;40m'
    BLUE = '\033[1;34;40m'
    Yellow = '\033[1;33;40m'
    GREEN = '\033[1;32;40m'

def launch():

    os.system('clear')
    def sprint(str):
        for c in str + '\n':
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(1. / 90)

    print("""\
                          _,.---,---.,_
                      ,;~'             '~;,
                    ,;                     ;,
                   ;                         ; 
                  ,'                         /'
                 ,;                        /' ;,
                 ; ;      .           . <-'  ; |
                 | ;   ______       ______   ; |
                 |  '/~"     ~" . "~     "~\'  |
                 |  ~  ,-~~~^~, | ,~^~~~-,  ~  |
                 |        }:{        }:{       |
                  |   l       / | \       !   |
                  .~  (__,.--" .^. "--.,__)  ~.
                   |    ----;' / | \ `;----   |
                   \__.       \/^\/       .__/
                    V| \                 / |
                     | |T~\___!___!___/~T| |
                     | |`IIII_I_I_I_IIII'| |
                     |  \,III I I I III,/  |
                      \   `~~~~~~~~~~'    /
                        \   .       .   /
                          \.    ^    ./
                            ^~~~^~~~^


 █████╗ ██╗   ██╗████████╗ ██████╗     ██████╗ ██╗      █████╗ ██╗   ██╗██████╗  ██████╗  ██████╗ ██╗  ██╗
██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗    ██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝██╔══██╗██╔═══██╗██╔═══██╗██║ ██╔╝
███████║██║   ██║   ██║   ██║   ██║    ██████╔╝██║     ███████║ ╚████╔╝ ██████╔╝██║   ██║██║   ██║█████╔╝ 
██╔══██║██║   ██║   ██║   ██║   ██║    ██╔═══╝ ██║     ██╔══██║  ╚██╔╝  ██╔══██╗██║   ██║██║   ██║██╔═██╗ 
██║  ██║╚██████╔╝   ██║   ╚██████╔╝    ██║     ███████╗██║  ██║   ██║   ██████╔╝╚██████╔╝╚██████╔╝██║  ██╗
╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝     ╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
                                                                                                          
    """)
    time.sleep(1)
    sprint("""\
█▄▄ █▄█   █▀█ ▄▀█ █░█ █░░   █▀▀ █░█ ▄▀█ █▀█ █▀█ █ █▀▀ █▀█
█▄█ ░█░   █▀▀ █▀█ █▄█ █▄▄   █▄▄ █▀█ █▀█ █▀▄ █▀▄ █ ██▄ █▀▄

""")


def choix_input():
    print("")
    options = ["Auto (Nslookup,WhoIS,Subdomain finder & NMAP)", "OSINT - Reconnaissance passive", "Obtenir les dernières CVE"]
    print("")
    for i, option in enumerate(options):
        if i == 0:
            print(f"\033[1;34m{i+1}: {option}\033[0m")
        if i == 1:
            print(f"\033[1;33;40m{i + 1}: {option}\033[0m")
        if i == 2:
            print(f"\033[1;31;40m{i + 1}: {option}\033[0m")


    print("")
    response = input("Veuillez entrer le numéro de l'option que vous souhaitez sélectionner: ")
    response = int(response) - 1
    selected_option = options[response]
    if selected_option == "Auto (Nslookup,WhoIS,Subdomain finder & NMAP)":
        auto()
    if selected_option == "OSINT - Reconnaissance passive":
        osint()
    if selected_option == "Obtenir les dernières CVE":
        print("\n Voici les 30 dernières CVE : \n")
        get_latest_cve(30)
3
launch()
choix_input()
