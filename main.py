import time
import random
import os
from colorama import Fore, init
init(autoreset=True)

def menu():
    print(f'#############################################################')
    print(f'#                    Welcome to {Fore.LIGHTRED_EX}Jokenpo{Fore.WHITE}                     #')
    print(f'# Stone wins Scissors, Scissors wins Paper, Paper wins Rock #')
    print(f'#                    Write quit to close                    #')
    print(f'#############################################################')

def userChoice():
    choice = ''
    while choice not in ('rock', 'paper', 'scissors'):
        choice = input('Make your choice(Rock, Paper or Scissors): ').lower()
        if choice == 'quit':
            print('End game')
            time.sleep(2)
            break
        elif choice not in ('rock', 'paper', 'scissors'):
            print('Sorry, this value is not valid')
        
    return choice

def botChoice():
    choice = random.choice(['rock', 'paper', 'scissors'])
    return choice

def mechanics(user, bot):

    if (user == 'rock' and bot == 'scissors') or (user == 'paper' and bot == 'rock') or (user == 'scissors' and bot == 'paper'):
        print(f'You chose {Fore.CYAN}{user}')
        time.sleep(1)
        print(f'Bot chose {Fore.LIGHTBLUE_EX}{bot}')
        time.sleep(1)
        print(f'{Fore.GREEN}Nice you won!!')
        print('We are the champions my friend')
        time.sleep(2)
    elif (bot == 'rock' and user == 'scissors') or (bot == 'paper' and user == 'rock') or (bot == 'scissors' and user == 'paper'):
        print(f'You chose {Fore.CYAN}{user}')
        time.sleep(1)
        print(f'Bot chose {Fore.LIGHTBLUE_EX}{bot}')
        time.sleep(1)
        print(f'{Fore.RED}looooooser!!')
        print('Try again...')
        time.sleep(2)
    else:
        print(f'You chose {Fore.CYAN}{user}')
        time.sleep(1)
        print(f'Bot chose {Fore.LIGHTBLUE_EX}{bot}')
        time.sleep(1)
        print(f'{Fore.YELLOW}Tie, try again')
        time.sleep(2)

def clearScreen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def main():
    quit = False
    while quit == False:
        clearScreen()
        menu()
        user = userChoice()
        if user == 'quit':  
            break
        bot = botChoice()
        mechanics(user, bot)

main()