import json 

try:
  with open('level1/04 Todo CLI/tasks.json', 'r') as f:
    tasks = json.load(f)
except FileNotFoundError:
    tasks = []

while True:
    try:
      print('\n=== Todo CLI ===')
      print('1. Add task')
      print('2. View tasks')
      print('3. Remove task')
      print('4. Mark task as done')
      print('5. Show only pending tasks')
      print('6. Quit')


      choose = input('Choose an option: ')
      
      if choose == '1':
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
         with open('level1/04 Todo CLI/tasks.json', 'w') as f:
          json.dump(tasks,f)
      elif choose == '2':
         for i, task in enumerate(tasks, 1):
            print(f"{i}. [{task['status']}] {task['name']} ({task['priority']})")
      elif choose == '3':
          number = int(input('Remove a task: '))
          if 1 <= number <= len(tasks):  
                  tasks.pop(number - 1)
                  with open('level1/04 Todo CLI/tasks.json', 'w') as f:
                      json.dump(tasks, f)
          else :
              print('Invalid task number')
      elif choose == '4':
        number = int(input('Mark a task as done: '))
        if 1 <= number <= len(tasks):
           tasks[number -1]['status'] = 'done'
           with open('level1/04 Todo CLI/tasks.json', 'w') as f:
              json.dump(tasks, f)
        else:
           print('Invalid task number.')
      elif choose == '5': 
         for i, task in enumerate(tasks, 1):
            if task['status'] == 'pending':
               print(f"{i}. [{task['status']}] {task['name']} ({task['priority']})")
      elif choose == '6':
         break
    except ValueError:
      print('Choose between options 1,2,3 and 4')