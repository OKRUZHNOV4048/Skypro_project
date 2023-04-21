# Создай класс Circle, с полем radius (указывается при инициализации)

# Добавь методы:
# get_radius() - возвращает радиус
# get_diameter() - возвращает двойной радиус
# get_perimeter() - возвращает 2*радиус*Пи (можно использовать pi=3.14 или math.pi)

import math

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def get_diameter(self):
        return 2 * self.radius

    def get_perimeter(self):
        return 2 * self.radius * math.pi

# Не удаляйте этот код, он нужен для проверки

circle_1 = Circle(7)
print("радиус", circle_1.get_radius() )
print("диаметр", circle_1.get_diameter() )
print("периметр", round(circle_1.get_perimeter(),1))