# Paramters functions reusable and self-contained. A function that grabs a global variable is locked to that one variable forever
# A function that recieves a parameter can work with any data you pass it 

import json
def save_tasks(tasks):
    with open('level1/04 Todo CLI/tasks.json', 'w') as f:
      json.dump(tasks, f)

def load_tasks():
    try:
        with open('level1/04 Todo CLI/tasks.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def add_task(tasks):
    task = input('Add a task: ')
    while True:
        priority = input('Priority (high/medium/low): ')
        if priority.lower() in ('high', 'medium', 'low'):
            break
        print('Choose between high, medium, low.')
    tasks.append({
        'name': task,
        'priority': priority,
        'status': 'pending'
        })
    save_tasks(tasks)

def view_tasks(tasks):
    for i, task in enumerate(tasks, 1):
            print(f"{i}. [{task['status']}] {task['name']} ({task['priority']})")

def remove_task(tasks):
    number = int(input('Remove a task: '))
    if 1 <= number <= len(tasks):  
        tasks.pop(number - 1)
        save_tasks(tasks)
    else :
        print('Invalid task number')

def mark_done(tasks):
    number = int(input('Mark a task as done: '))
    if 1 <= number <= len(tasks):
        tasks[number -1]['status'] = 'done'
        save_tasks(tasks)
    else:
        print('Invalid task number.')

def show_pending(tasks):
    for i, task in enumerate(tasks, 1):
        if task['status'] == 'pending':
            print(f"{i}. [{task['status']}] {task['name']} ({task['priority']})")

def main():
    tasks = load_tasks()
    while True:
        try:
            print('\n=== Todo CLI ===')
            print('1. Add task')
            print('2. View tasks')
            print('3. Remove task')
            print('4. Mark as done')
            print('5. Show only pending tasks')
            print('6. Quit')

            choose = input('Choose an option: ')

            if choose == '1':
                add_task(tasks)
            elif choose == '2':
                view_tasks(tasks)
            elif choose == '3':
                remove_task(tasks)
            elif choose == '4':
                mark_done(tasks)
            elif choose == '5':
                show_pending(tasks)
            elif choose == '6':
                break
        except ValueError:
            print('Choose between options 1,2,3,4,5 and 6.')

main()