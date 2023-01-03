import random as Ran
from colorama import Fore
import art as Art # this library has to be installed

def advise(): # the basic adviser function
    
    answersOnQuestion = ["Sure.", "I wouldn't rely on that.",
                         "Maybe.", "That? Definitely not."]
    
    welcome = Art.text2art("ADVISER")
    print(Fore.MAGENTA + welcome)
    
    # functional part 
    while True:

        question = input(Fore.LIGHTGREEN_EX + "Enter your question: ")
    
        if question.endswith("?"):
            choice = Ran.choice(answersOnQuestion)
            print(choice)
            print("")
            
            while True:
            
                repChoice = input("Restart? [Y/N]" 
                                + "\n" + "Menu[1]")
                if repChoice == "Y":
                    break
                elif repChoice == "N":
                    quit()
                elif repChoice == "1":
                    main()
                else:
                    print("Didn't understand - again: ")
                    break
        else:
            print(Fore.RED + "That wasn't a question - again: ")   
            break        
        
def confession(): # the confessing function
    
    ok = """ ___________                  
            < IT'S OK. >
             ----------- 
                    \   ^__^
                     \  (oo)\_______
                        (__)\       )\/
                            ||----w |
                            ||     ||
                                        """
        
    notok = """ ___________ 
              < IT'S NOT OK. >
                ----------- 
                    \   ^__^
                     \  (oo)\_______
                        (__)\       )\/
                            ||----w |
                            ||     ||
                                        """
    
    welcome = Art.text2art("CONFESSOR")
    print(Fore.CYAN + welcome)
    
    # this is a database of all bad words significating a bad situation
    # it can be customized or updated any time
    badwords = ["stole", "steal", "stolen",
                "hurt", "robbered", "robbery",
                "robber", "hit", "punched",
                "punch", "blood", "bleed", "bleeded",
                "bleedy", "bleeding", "bloody",
                "wound", "attack", "attacked"]
    
    # functional part
    while True:
        
        message = input(Fore.LIGHTRED_EX + "What's on your heart? ")
        
        if any(word in message for word in badwords):
            print(Fore.RED + notok)
            print("")
            print("Well, that's not good at all. Solve it as fairly as it has to be.")
            print("Having cold and calmed brain is most important.")
            
            while True:
            
                repChoice = input("Restart? [Y/N]" 
                                + "\n" + "Menu[1]")
                if repChoice == "Y":
                    break
                elif repChoice == "N":
                    quit()
                elif repChoice == "1":
                    main()
                else:
                    print("Didn't understand - again: ")
                    break
                
        else:
            print(Fore.LIGHTGREEN_EX + ok)
            print("")
            print("It's ok.")
            print("If you're not happy about how it is, keep your head calmed, determine the situation and solve it calmly.")
            print("If you're happy with it, there's no reason for solving anything :).")
       
            while True:
            
                repChoice = input("Restart? [Y/N]" 
                                + "\n" + "Menu[1]")
                if repChoice == "Y":
                    break
                elif repChoice == "N":
                    quit()
                elif repChoice == "1":
                    main()
                else:
                    print("Didn't understand - again: ")
                    break

# welcomming function choosing the working mode
def main():
    
    print("Welcome in the program.")
    print("Do you want to talk with adviser, or with confessor?")
    print("Adviser = 0,")

    mainChoice = int(input("confessor = 1: "))
    
    while True:
        
        if mainChoice == 0:
            advise()
        elif mainChoice == 1:
            confession()
        else:
            print("Didn't understand - again: ")

main()
