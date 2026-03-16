global money
import time
import random
import keyboard as kb
from colorama import init, Fore, Style, Back
import pickle
init(autoreset=True)
def start1():
    money = 100
    gamesotd()
def gamesotd():
    print('Press space to roll, or O to roll one die')
    kb.wait('space' or 'O' or 'o')
    bet = int(input("Choose how much to bet: "))
    y = int(input("Choose a number(1-50): "))
    if bet >= money:
        print("Can not place bet, not enough money")
    if y >= 51:
        print(Fore.RED + "Please enter a number between 1 and 50")
        restart1()
    else:
        x = random.randrange(1, 50)
        print(x)
        if x == y:
            money = money - bet
            print(f"${money}")
        else:
          money = money * 2
          print(f"${money}")
    restart1()
    
if kb.is_pressed('esc') == True:
    print("Select an option")
    print("1. Resume")
    print("2. Save")
    print("3. Load")
    print("4. Exit")
    x = int(input("Choose an option: "))
    if x == 1:
        restart1()
    if x == 2:
        with open('moneysave.dat', 'wb'):
            pickle.dump([money], f, protocol=2)
    if x == 3:
        with open('moneysave.dat', 'rb') as f:
            money = pickle.load(f)
    if x == 4:
        pass
    if x >= 5:
        print("Invalid option")

def restart1():
    startgamesotd()
def restart2():
    startgameod()
def startgameod():
    print(Fore.RED + "!!This dice only uses one digit which makes it harder to win!!")
    print("Press R to roll")
    kb.wait('R' or 'r')
    bet = int(input("Enter how much you want to bet: "))
    y = int(input("Enter a number between 1 and 9: "))
    if y >= 10:
        print(Fore.RED + "Please do not enter a number over 9.")
        restart2()
        if y <= 0:
              print(Fore.RED + "Please do not enter a number less than 1")
              restart2()
    else:
        x = random.randrange(1, 9)
        print(x)
        if x == y:
            z = money - bet
            print("You lost the bet :[")
            print(f"Current amount: ${z}")
        
        
print("Rules: Pick a 2 digit number to be the losing number, if the dice lands on that number then you lose the amount of money you bet. You can select to roll a 1 digit die but that increases your chances of losing, but instead of doubling your bet it quadruples it. (if you dont disable snake eyes and you get an 11 you lose your bet)")
print("Starting money: $100")
if input("disable snake eyes? y/n: ") == "n":
    start1()

