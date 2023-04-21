# Создай класс TodoList у которого есть поле задачи tasks – список строк)

# При инициализации список задач будет пустым.

# Добавь к классу метод add_task(<название задачи>) который добавляет задачу в список

# Создай переменную todo_list – экземпляр класса TodoList c задачами:

# Выключить свет
# Поменять лампочку
# Включить свет

class TodoList:
  def __init__(self):
    self.tasks = []

  def add_task(self, task):
    self.tasks.append(task)


todo_list = TodoList()
todo_list.add_task("Выключить свет")
todo_list.add_task("Поменять лампочку")
todo_list.add_task("Включить свет")

# Не удаляйте этот код, он нужен для проверки

print(" ".join(todo_list.tasks))