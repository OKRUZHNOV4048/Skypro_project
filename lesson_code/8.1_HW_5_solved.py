# Теперь, когда герой умеет просто ходить, научим его ходить на какое-то расстояние.
# Функции похожи на методы и им тоже можно передавать аргументы. Этим и займемся.

# Отредактируйте функции перемещения из прошлого задания так, чтобы при вызове

# hero.go_right(50)
# персонаж говорил:
# Я иду 50 метров направо

class Hero:

  def go_right(self, l):
    print(f"Я иду {l} метров направо")

  def go_left(self, l):
    print(f"Я иду {l} метров налево")

  def observe(self):
    print("Я осматриваюсь")


hero = Hero()

hero.go_right(50)
hero.go_left(30)
hero.observe()