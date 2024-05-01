import sys
import colorama
import os
from colorama import just_fix_windows_console
just_fix_windows_console()
from rich import inspect
import inquirer
import pyfiglet
import tabulate

def main():
    tasks = []

    
    def taskLoop(all_tasks):    
        
        display(tasks)
        
        operation = input(colorama.Fore.GREEN + "'n' to make new task, 'e' to edit task, 'd' to delete task, q to exit: ")
        
        if operation == 'n':
            addTask(tasks)
        elif operation == 'e':
            editTask(tasks)
        elif operation == 'd':
            deleteTask(tasks)
        elif operation == 'q':
            return
        else:
            taskLoop(tasks)

    def addTask(all_tasks):

        new_task = input(colorama.Fore.GREEN + "Enter new task: ")
        all_tasks.append(new_task)
        
        taskLoop(tasks)

    def editTask(all_tasks):
        pass

    def deleteTask(all_tasks):
        pass


    def display(all_tasks):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(pyfiglet.figlet_format('Kanban\n'))

        if len(all_tasks) == 0:
            print("No tasks! BOOOOOOOOO!")
        else:
            for index, task in enumerate(all_tasks):
                print(f'{index + 1}) {task}')

    taskLoop(tasks)


if __name__ == "__main__":
    main()
