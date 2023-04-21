# В качественных играх на каждом новом уровне герои открывают в себе новые способности.
# А кто реализует их? Программисты, конечно!

# Добавьте классу
# Hero
# методы:

# go_up - выводит "Я иду наверх"
# go_down - выводит "Я иду вниз"
# rest - выводит "Я отдыхаю"
#
# Напишите код, который реализует патрулирование:

# Я иду наверх
# Я иду наверх
# Я осматриваюсь
# Я иду вниз
# Я иду вниз
# Я отдыхаю

class Hero:

  def go_right(self):
    print("Я иду направо")

  def go_left(self):
    print("Я иду налево")

  def observe(self):
    print("Я осматриваюсь")

  def up(self):
    print("Я иду наверх")

  def down(self):
    print("Я иду вниз")

  def rest(self):
    print("Я отдыхаю")


hero = Hero()

hero.up()
hero.up()
hero.observe()
hero.down()
hero.down()
hero.rest()
