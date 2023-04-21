# Skypro. Курс "Python-разработчик 2.0". Поток 19.0. Окружнов Алексей.
# Домашнее задание 3. Консольное приложение для обучения английскому с дополнительными списками и циклами.

questions = ["My name ___ Vova", "I ___ a coder", "I live ___ Moscow"] # Создаем список вопросов.
answers = ["is", "am", "in"] # Создаем правильных ответов.

score_counter = 0 # Задаем переменную - счетчик количества баллов.
correct_answer_counter = 0 # Задаем переменную - счетчик правильных ответов.

correct_writing_answ = "вопрос" # Задаем переменную, определяющую верное окончание слова "вопрос" в зависимости от числа.
correct_writing_perc = "процент" # Задаем переменную, определяющую верное окончание слова "процент" в зависимости от числа.

user_decision = input("Привет! Предлагаю проверить свои знания английского! Наберите \"ready\", чтобы начать!\n")

if user_decision == "ready":
	for i in range(len(questions)):
		user_answer = input(questions[i])
		if user_answer == answers[i]:
			print("Ответ верный! \nВы получаете 10 баллов!")
			score_counter += 10
			correct_answer_counter += 1
		else:
			print(f"Неправильно \nПравильный ответ: {answers[i]}")

	correct_answer_perc = round(score_counter * 100 / (10 * len(questions)))

	# Определение верных окончаний слов "вопрос" и "ответ":

	if 11 <= correct_answer_counter % 100 <= 14 or 5 <= correct_answer_counter % 10 <= 9 or correct_answer_counter % 10 == 0:
		correct_writing_answ = "вопросов"
	elif 2 <= correct_answer_counter % 10 <= 4:
		correct_writing_answ = "вопроса"

	if 11 <= correct_answer_perc % 100 <= 14 or 5 <= correct_answer_perc % 10 <= 9 or correct_answer_perc % 10 == 0:
		correct_writing_perc = "процентов"
	elif 2 <= correct_answer_perc % 10 <= 4:
		correct_writing_perc = "процента"

	# После получения всех данных от пользователя и обработки их далее вывод информации
	# о количестве правильных ответов, количестве баллов и процентом отношении набранных
	# баллов к максимально возможному количеству:

	print(f"\nВот и все! \nВы ответили на {correct_answer_counter} {correct_writing_answ} из 3 верно.")
	print(f"Вы заработали {score_counter} баллов! \nЭто {correct_answer_perc} {correct_writing_perc}!")

else:
	print("Кажется, вы не хотите играть. Очень жаль.")