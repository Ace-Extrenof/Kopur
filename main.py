import sys
import colorama
import os
from colorama import just_fix_windows_console
just_fix_windows_console()
colorama.init()
from rich import inspect
import inquirer



def main():
    def title_screen():
        os.system('cls' if os.name == 'nt' else 'clear')
        global inp

        opt = [inquirer.List('choice',
                             message = colorama.Style.BRIGHT + 'Select',
                             choices = [colorama.Fore.GREEN + 'Kanban', 
                                        colorama.Fore.GREEN + 'Task Manager'])]

        
        ans = inquirer.prompt(opt)
        global INPUT
        INPUT = ans['choice']

    def options():
        if INPUT == "Task Manager".lower() or '1':
            task_manager()
        elif INPUT == "Knban".lower() or INPUT == '2':
            kanban()
        else:
            print("err... \nNOT AN OPTION")

    def kanban():
        print("kanban ;)")

    def task_manager():
        print("task manager")

    title_screen()
    options()


if __name__ == "__main__":
    main()
