import json # loads the JSON module - gives you json.dump() and json.load()
#jSON is a text format for storing data, like a structured .txt file

try: #attempt to load exisitng tasks - file mignt not exist yet
    with open('level1/04 Todo CLI/tasks.json', 'r') as f:
        # read tasks.json in read mode - 'r' = read only
        # 'with' guarantees the file closes automatically when done
        tasks = json.load(f) 
        # (read the JSON file and convert it back into a Python list)
        # tasks.json contains ["Clean bedroom", "Walk the dog"]
        # json.load() turns that into ['Clean bedroom', 'Walk the dog'])
except FileNotFoundError:
    tasks = [] 
    # file doesn't exist yet - first time running the program
    # so just start with an empty list instead of crashing

while True:
  try: 
      print('\n=== Todo CLI ===')
      print('1. Add task')
      print('2. View tasks')
      print('3. Remove task')
      print('4. Quit ')

      choice = input('Choose: ')

      if choice == '1':
        task = input('Add tasks: ')
        tasks.append(task)
        with open('level1/04 Todo CLI/tasks.json', 'w') as f: #'w' write mode - creates file if missing , overwrites if exists
            json.dump(tasks, f) #json.dump() converts Python lists → Json text and writes it
            # so next time the program starts, tasks.json has the new task
      elif choice == '2':
        for i, task in enumerate(tasks, 1):
            print(f'{i}. {task}')
      elif choice == '3':
        if not tasks:
          print('No tasks to remove.')
        else :
           number = int(input('Remove a task: '))
           if 1 <= number <= len(tasks):   # valid range
              tasks.pop(number - 1)
              with open('level1/04 Todo CLI/tasks.json', 'w') as f: # save again immediately after removing so the file reflects the deletion 
                  json.dump(tasks, f) # placed INSIDE the valid range check - only saves when something actually changed
           else:
              print('Invalid task number.')
      elif choice == '4':
         break
  except ValueError:
     print('Choose between 1,2,3 and 4.')