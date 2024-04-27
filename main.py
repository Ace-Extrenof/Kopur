import sys
import colorama
import os
from colorama import just_fix_windows_console
just_fix_windows_console()
from rich import inspect
import inquirer

def main():
    def title_screen():
        os.system('cls' if os.name == 'nt' else 'clear')
        global inp

        opt = [inquirer.List('choice',
                             message = colorama.Style.DIM + 'PROJECT MANAGER(SHIT)',                              
                             choices = ['Kanban', 
                                        'Task Manager'])]

        
        ans = inquirer.prompt(opt)
        global INPUT
        if ans is not None:
           INPUT = ans['choice']

    def options():
        global INPUT
        if INPUT.lower() == 'kanban' or INPUT == '0':
            kanban()
        elif INPUT.lower() == "task manager" or INPUT == '1':
            task_manager()

        else:
            print('DAMN ERROR')
    def kanban():
        print("kanban ;)")

    def task_manager():
        print("task manager")
    
    title_screen()
    options()


if __name__ == "__main__":
    main()
