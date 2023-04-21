# Skypro. Курс "Python-разработчик 2.0". Поток 19.0. Окружнов Алексей.
# Курсовая работа 1.
# Консольное приложение, помогающее изучать коды азбуки Морзе.

import random

def morse_encode(word):
	"""
	Функция morse_encode принимает str значение.
	После приведения str к нижнему регистру пакует str в list посимвольно.
	Далее перебором цикла for и через сопоставление с ключами
  	словаря letter_encryption формируется зашифрованное слово, значение которого
  	принимает переменная encrypted_word с разделителем " " для каждой отдельной
	зашифроанной буквы.
	"""
	letter_encryption = {
		"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.",
    "g": "--.", "h": "....", "i": "..", "j": ".---","k": "-.-", "l": ".-..",
    "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.",
    "s": "...","t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
    "y": "-.--", "z": "--.."
	}

	original_word = list(word.lower())

#	encrypted_word = ""

	encrypted_word = [letter_encryption[letter] for letter in original_word]
	return " ".join(encrypted_word)

#	for w in original_word:
#		if w in letter_encryption.keys():
#			encrypted_word += letter_encryption[w]
#			encrypted_word += " "
#	return encrypted_word


def get_word():
	"""
	Функция get_word при вызове возвращает случайное слово
	из списка слов для тренировок, который задан ниже в основной
	части программы и который можно дополнять.
	"""
	return random.choice(word_training)


def print_statistics(answers):
	"""
	Функция print_statistics в качестве аргумента принимает список
	из bool значений, ничего не возвращает в код,
	но сразу выводит статистику через print..
	"""
	print(
		f"\nВсего задачек: {word_number - 1}\n"
		f"Отвечено верно: {answers.count(True)}\n"
		f"Отвечено неверно: {answers.count(False)}\n"
	)


# Функционал программы искусственно ограничен.
# Программа работает только со словами, но не с символами или фразами.
# Это вытекает из условий задания на курсовую, указанных в шагах 0 и 1.
# Функционал легко расширяется путем добавления
# в словарь letter_encryption внутри функции morse_encode
# новых ключей и значений.

# Списки я задаю после импортов и функций, как это было указано
# в задании на курсовую.
# Список word_training содержит рандомные слова для тренировки.

word_training = [
	"lamp", "system", "horse", "air", "play", "tell", "small",
	"end", "shot", "jack", "land", "build", "work", "success"
]

# Список answers, содержащий элементы bool, отражающие
# правильность/неправильность выбора пользователя для дальнейшей
# подготовки статистики.
answers = []

word_number = 1 # Номер итерации в цикле из 5 выводов с зашифрованным словом.

answer_user = ""

input("""Сегодня мы потренируемся расшифровывать морзянку.
Нажмите Enter и начнем!
""")

while word_number <= 5:
	original_word = get_word() 
	encrypted_word = morse_encode(original_word)
	"""
	Здесь функция get_word, которая при вызове возвращает случайное слово
	является аргументом morse_encode, где слово, возвращенное
	из get_word зашифровывается.
	"""
	answer_user = input(
      f"Слово {word_number}: {encrypted_word}\nЧто это за слово?\n")
	if answer_user == original_word:
		print(f"Верно! Это {original_word}.")
		answers.append(True)
	else:
		print(f"Не верно! Это было слово {original_word}.")
		answers.append(False)
	word_number += 1

print_statistics(answers)
