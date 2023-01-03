import random as Ran
from colorama import Fore
import art as Art # tuto knihovnu je nutné mít nainstalovanou

def porada(): # funkce jednoduchého poradce
    
    answersOnQuestion = ["Určitě.", "Nespoléhal bych na to.",
                         "Možná.", "To rozhodně ne."] # seznam primitivních odpovědí na otázku
    
    welcome = Art.text2art("PORADCE")
    print(Fore.MAGENTA + welcome)
    
    # funkční část
    while True:

        question = input(Fore.LIGHTGREEN_EX + "Zadej tvůj dotaz: ")
    
        if question.endswith("?"):
            choice = Ran.choice(answersOnQuestion)
            print(choice)
            print("")
            
            while True:
            
                repChoice = input("Restartovat? [A/N]" 
                                + "\n" + "Menu[1]: ")
                if repChoice == "A":
                    break
                elif repChoice == "N":
                    quit()
                elif repChoice == "1":
                    main()
                else:
                    print("Nerozumím - znovu: ")
                    break
        else:
            print(Fore.RED + "To nebyla otázka, znovu prosím: ")  
            break         
        
def zpoved(): # funkce zpovědnice
    
    ok = """ ___________                  
            < JE TO OK. >
             ----------- 
                    \   ^__^
                     \  (oo)\_______
                        (__)\       )\/
                            ||----w |
                            ||     ||
                                       """
        
    notok = """ ___________ 
              < NENÍ TO OK. >
                ----------- 
                    \   ^__^
                     \  (oo)\_______
                        (__)\       )\/
                            ||----w |
                            ||     ||
                                        """
    
    welcome = Art.text2art("ZPOVEDNICE")
    print(Fore.CYAN + welcome)
    
    # databáze slov, které určují špatnou situaci 
    # může být libovolně upravována, nebo doplňována
    badwords = ["ukradl", "Ukradl", "ukradla", "Ukradla", "ublížil",
                "Ublížil", "ublížila", "Ulbížila", "ublížilo",
                "Ublížilo", "ublížili", "Ublížili", "ublížily",
                "Ublížily", "ukradli", "Ukradli", "ukradlo",
                "Ukradlo", "ukradly", "Ukradly", "odcizily",
                "Odcizily", "odZený", "Uhozený", "praštil",
                "Praštil", "praštila", "Praštila", "praštili",
                "Praštili", "praštily", "Praštily", "přaštěn",
                "Praštěn", "praštěni", "Praštěni", "praštění",
                "Praštění", "krev", "Krev", "krvácel", "Krvácel",
                "krvácela", "Krvácela", "rána", "Rána"
                "napadl", "napadla", "Napadl", "Napadla",
                "uhodil", "Uhodil", "uhodila", "Uhodila",
                "ukrást", "Ukrást", "ublížit", "Ublížit",
                "odcizit", "Odcizit", "uhodit", "Uhodit",
                "praštit", "Praštit", "krvácet", "Krvácet",
                "Krvácí", "krvácí", "napadat", "Napadat",
                "ukraden", "Ukraden", "ukradena", "Ukradena",
                "okrást", "Okrást", "okraden", "Okraden",
                "Okradena", "Vystřelil", "vystřelil", "vystřelila,"
                "Vystřelila", "vystřelilo", "Vystřelilo", "vystřelily",
                "Vystřelily", "vystřelili", "Vystřelili", "zavraždil"
                "Zavraždil", "zavraždili", "Zavraždili", "zavraždila",
                "Zavraždila", "zavraždily", "Zavraždily", "zabil", 
                "Zabil", "zabili", "Zabili", "zabily", "Zabily"]
    
    # funkční část
    while True:
        
        message = input(Fore.LIGHTRED_EX + "Copak ti leží na srdci? ")
        
        if any(word in message for word in badwords):
            print(Fore.RED + notok)
            print("")
            print("Tak tohle není dobrý, musíš situaci vyřešit správně a spravedlivě.")
            print("Důležitá je chladná hlava, ale jednej, protože to je třeba vyřešit.")
            
            while True:
            
                repChoice = input("Restartovat? [A/N]" 
                                + "\n" + "Menu[1]")
                if repChoice == "A":
                    break
                elif repChoice == "N":
                    quit()
                elif repChoice == "1":
                    main()
                else:
                    print("Nerozumím - znovu: ")
                    break
        
        else:
            print(Fore.LIGHTGREEN_EX + ok)
            print("")
            print("Je to v pořádku.")
            print("Pokud s tím nejsi spokojen, zachovej chladnou hlavu, zhodnoť stav situace a jednej v klidu.")
            print("Pokud jsi spokojen, není co řešit :).")
            
            while True:
            
                repChoice = input("Restartovat? [A/N]" 
                                + "\n" + "Menu[1]")
                if repChoice == "A":
                    break
                elif repChoice == "N":
                    quit()
                elif repChoice == "1":
                    main()
                else:
                    print("Nerozumím - znovu: ")
                    break

# úvodní funkce volící pracovní režim
def main():
    
    print("Vítej v programu.")
    print("Chceš mluvit s poradcem, nebo se zpovědníkem?")
    print("Poradce = 0,")

    mainChoice = int(input("zpovědnice = 1: "))
    
    while True:
        
        if mainChoice == 0:
            porada()
        elif mainChoice == 1:
            zpoved()
        else:
            print("Nerozumím - ještě jednou: ")

main()
