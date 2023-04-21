# Создай класс Square с полями
# Длина строны (side_length) – целое число
# Цвет (color) – строка, поле опциональное и равно по умолчанию white

# Добавить методы:
# set_side(length) – задает размер стороны
# set_color(color) - задает цвет
# get_side() - возвращает side_length в виде целого числа
# get_color() - возвращает color
# get_perimeter() - возвращает периметр (сторону * 4)

class Square:

  def __init__(self, side_lenght, color="white"):
    self.side_lenght = side_lenght
    self.color = color

  def set_side(self, lenght):
    self.side_lenght = lenght

  def set_color(self, color_):
    self.color = color_

  def get_side(self):
    return self.side_lenght

  def get_color(self):
    return self.color

  def get_perimeter(self):
    perimeter = self.side_lenght * 4
    return perimeter

# Не удаляйте этот код, он нужен для проверки

square_1 = Square(2)
print(square_1.get_side())
print(square_1.get_perimeter())
print(square_1.get_color())
print("—-")
square_1.set_side(3)
square_1.set_color("red")
print(square_1.get_side())
print(square_1.get_perimeter())
print(square_1.get_color())
print("—-")
square_1 = Square(1, "black")
print(square_1.get_side())
print(square_1.get_perimeter())
print(square_1.get_color())