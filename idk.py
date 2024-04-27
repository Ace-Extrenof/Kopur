import inquirer

def main():
    # Define the list of options
    options = [
        inquirer.List('choice',
                      message='Select an option:',
                      choices=['Kanban', 'Task Manager'])
    ]

    # Prompt the user for their choice
    answers = inquirer.prompt(options)

    # Get the user's selected choice
    user_choice = answers['choice']

    # Print the corresponding output
    if user_choice == 'Task Manager':
        print('taskmna')
    elif user_choice == 'Kanban':
        print('kanban')
    else:
        print('Invalid choice. Please select either "Kanban" or "Task Manager".')

if __name__ == '__main__':
    main()
