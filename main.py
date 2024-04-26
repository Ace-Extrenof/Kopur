import sys
import colorama
import os
from colorama import just_fix_windows_console
just_fix_windows_console()
colorama.init()

def title_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

    print(colorama.Fore.BLUE + "##### STOODY HELPER ######\n\n-----1) KANBAN-----\n-----2) TASK MANAGER")
    global inp 
    inp = input("\uf061 ")
    return inp

def options(INPUT):
    if INPUT == "KANBAN".lower() or '1' or '1)':
        kanban()
    elif INPUT == "TASK MANAGER" or '2' or '2)':
        task_manager()
    else:
        print("err... \nNOT AN OPTION")

def kanban():
    print("kanban ;)")

def task_manager():
    print("task manager")

if __name__ == "__main__":
    title_screen()
    options(inp)
