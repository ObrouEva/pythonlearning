tasks = []

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
           else:
              print('Invalid task number.')
      elif choice == '4':
         break
  except ValueError:
     print('Choose between 1,2,3 and 4.')