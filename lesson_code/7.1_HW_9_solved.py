# Некоторые рыбы предпочитают морскую воду, некоторые — пресную.
# Разделите список словарей на два, затем выведите названия вида из каждого словаря в строку. Вот так:

# Морские: Тунец, Скумбрия
# Пресноводные: Красноперка, Карась

fish = [
    {"specie": "Белуга", "water": "fresh"},
    {"specie": "Карась", "water": "fresh"},
    {"specie": "Красноперка", "water": "fresh"},

    {"specie": "Морской окунь", "water": "sea"},
    {"specie": "Тунец", "water": "sea"},
    {"specie": "Скумбрия", "water": "sea"},

]

fresh_water = []
sea_water = []
for item in fish:
    if item["water"] == "sea":
        sea_water.append(item["specie"])
    else:
        fresh_water.append(item["specie"])

print(f"Морские: {', '.join(sea_water)}")
print(f"Пресноводные: {', '.join(fresh_water)}")
