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

    def task_seletecion(all_tasks, operation):
        task_number = input(f"Enter the task index which you want to {operation}: ")

        valid = False
        while not valid:
            try:
                number = int(task_number)
                valid = True
            except:
                task_number = input('Please provide a valid task number: ')

        if not (0 < number <= len(all_tasks)):
            print('Task not found!')
            task_seletecion(all_tasks, operation)
        else:
            return number

    def addTask(all_tasks):

        new_task = input(colorama.Fore.GREEN + "Enter new task: ")
        all_tasks.append(new_task)
        
        taskLoop(tasks)

    def editTask(all_tasks):
        task_number = task_seletecion(tasks, 'edit')
        new_task = input('Enter new task: ')

        all_tasks[task_number - 1] = new_task

        display(tasks)
        taskLoop(tasks)

    def deleteTask(all_tasks):
        task_number = task_seletecion(tasks, 'delete') 
        all_tasks.remove(all_tasks[task_number - 1])
        
        display(tasks)
        taskLoop(tasks)

    def display(all_tasks):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(colorama.Fore.YELLOW + pyfiglet.figlet_format('Kanban\n'))

        if len(all_tasks) == 0:
            print("No tasks! BOOOOOOOOO!")
        else:
            for index, task in enumerate(all_tasks):
                print(f'{index + 1}) {task}')

    taskLoop(tasks)


if __name__ == "__main__":
    main()
