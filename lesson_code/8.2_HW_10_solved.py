# У нас есть класс Hero и hero — экземляр класса Hero.
# При выполнении print(hero) должна выводиться информация про hero в формате:
# Герой Питомир взял с собой меч, плащ, шляпа
# Реализуйте магический метод repr.

# Формат вывода:
# Герой Питомир взял с собой меч, плащ, шляпа

class Hero():

  def __init__(self, name, posessions):
    self.name = name
    self.posessions = posessions

  def __repr__(self):
    return f"Герой {self.name} взял с собой {', '.join(self.posessions)}"


# Не удаляйте код ниже, он нужен для проверки

hero = Hero("Питомир", ["меч", "плащ", "шляпа"])
print(hero)