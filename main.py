import sys
import colorama
import os
from colorama import just_fix_windows_console
just_fix_windows_console()
colorama.init()
from rich import inspect
import inquirer

def title_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    global inp

    opt = [inquirer.List('Option: ',
                         message = colorama.Style.BRIGHT + 'Select',
                         choices = [colorama.Fore.GREEN + 'Kanban', 
                                    colorama.Fore.GREEN + 'Task Manager'])]

    
    inp = inquirer.prompt(opt)
    inspect(inp)
    return inp

def options(INPUT):
    if INPUT == "KANBAN".lower() or '1':
        kanban()
    elif INPUT == "TASK MANAGER".lower() or '2':
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
