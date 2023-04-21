# Создай класс Number c полем value (указывается при инициализации)

# Добавь методы:
# .get() возвращает текущее value
# .add(<значение>) добавляет указанное число к value
# .subtract(<значение>) вычитает указанное число из value

class Number:

  def __init__(self, value):
    self.value = value

  def get(self):
    return self.value

  def add(self, present_value_plus):
    self.value += present_value_plus

  def subtract(self, present_value_minus):
    self.value -= present_value_minus




# Пример использования, не влияет ни на что, можно удалить.

x = Number(7)
x.add(3)
x.subtract(10)
x.get()

# Не удаляйте этот код, он нужен для проверки

n = Number(7)
print(n.get())
n.add(3)
print(n.get())
n.subtract(5)
print(n.get())