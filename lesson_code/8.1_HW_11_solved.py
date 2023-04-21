# При инициализации экземпляра класса задается поле motto.

# Сделайте так, чтобы при вызове метода say, motto
# выводилось на стандартный вывод в формате:
# Питомир говорит: Кусь за Русь!


class Hero:

  def __init__(self, name, motto):
    self.name = name
    self.motto = motto

  def say(self):
    print(self.name, "говорит:", self.motto)

# Не удаляйте код ниже, это проверка (иначе мы укусим вас за бочок)

pythomir = Hero("Питомир", "Кусь за Русь!")
pythomir.say()
djangomir = Hero("Джангомир", "Работает - и ладно!")
djangomir.say()