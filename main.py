import time
import random

def userChoice():
    choice = ''
    while choice not in ('rock', 'paper', 'scissors'):
        choice = input('Make your choice: ').lower()
        if choice == 'quit':
            print('End game')
            time.sleep(3)
            break
        elif choice not in ('rock', 'paper', 'scissors'):
            print('Sorry, this value is not valid')
        
    return choice

def botChoice():
    choice = random.choice(['rock', 'paper', 'scissors'])
    return choice

def mechanics(user, bot):

    if (user == 'rock' and bot == 'scissors') or (user == 'paper' and bot == 'rock') or (user == 'scissors' and bot == 'paper'):
        print('Nice you won!!')
        print(f'You chose {user}')
        print(f'Bot chose {bot}')
        print('We are the champions my friend')
        time.sleep(5)
    elif (bot == 'rock' and user == 'scissors') or (bot == 'paper' and user == 'rock') or (bot == 'scissors' and user == 'paper'):
        print('looooooser!!')
        print(f'You chose {user}')
        print(f'Bot chose {bot}')
        print('Try again...')
        time.sleep(1)
        print('in another life')
        time.sleep(4)
    else:
        print('Tie, try again')
        print(f'You chose {user}')
        print(f'Bot chose {bot}')
        time.sleep(5)

def clearScreen():
    print()

def main():
    quit = False
    while quit == False:
        user = userChoice()
        if user == 'quit':  
            break
        bot = botChoice()
        mechanics(user, bot)
        clearScreen()

main()