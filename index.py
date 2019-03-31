class To_Do_List:
  def __init__(self):
    self.list = [None]
    self.messages = {
      'start': 'What would you like to do?\n  create  edit  delete  complete  list  stop',
      'create': 'Type to do',
      'edit': 'Which task would you like to edit?',
      'delete': 'Which task(s) would you like to delete?',
      'complete': 'Which task(s) have you completed?'
    }

  def run_app(self):
    userInput = self.get_input([self.messages['start']])
    if(userInput == 'create'):
      self.create_task()
      self.run_app()
    elif(userInput == 'edit'):
      self.edit_task()
      self.run_app()
    elif(userInput == 'delete'):
      self.delete_task()
      self.run_app()
    elif(userInput == 'complete'):
      self.complete_task()
      self.run_app()
    elif(userInput == 'list'):
      print(self.get_formatted_list())
      self.run_app()
    elif(userInput == 'stop'):
      print(self.get_formatted_list())
    else:
      print('I didn\'t quite get that.')
      self.run_app()

  def get_input(self, messages):
    return raw_input('\n{message}\n\n'.format(message = '\n'.join(messages)))

  def get_formatted_list(self):
    formatted_list = '\n'
    for i in range(1, len(self.list)):
      formatted_list += ('{i}: {task} -> {status}\n'.format(i = i, task = self.list[i]['task'], status = self.list[i]['status']))
    return formatted_list

  def get_valid_task_key(self, messages):
    task_key = ''
    while not unicode(task_key, 'utf-8').isnumeric():
      task_key = self.get_input(messages)
    return int(task_key)

  def create_task(self):
    task = self.get_input([self.messages['create']])
    self.list.append({
      'task': task,
      'status': 'incomplete'
    })

  def edit_task(self):
    task_key = self.get_valid_task_key([self.messages['edit'], self.get_formatted_list()])
    task_status = self.list[task_key]['status']
    task = self.get_input([self.messages['create']])
    self.list[task_key] = {
      'task': task,
      'status': task_status
    }

  def delete_task(self):
    task_key = self.get_valid_task_key([self.messages['delete'], self.get_formatted_list()])
    del self.list[task_key]

  def complete_task(self):
    task_key = self.get_valid_task_key([self.messages['complete'], self.get_formatted_list()])
    self.list[task_key]['status'] = 'complete'


my_list = To_Do_List()

my_list.run_app()