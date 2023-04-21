# Skypro. Курс "Python-разработчик 2.0". Поток 19.0. Окружнов Алексей.
# Домашнее задание 2. Консольное приложение для обучения английскому.

user_name = input("Привет! Предлагаю проверить свои знания английского! Расскажи, как тебя зовут! ")

print(f"Привет, {user_name}, начинаем тренировку!")
print("Вставь пропущенные слова в следующих трех предложениях:")

score_counter = 0 # Задаем переменную - счетчик количества баллов.
correct_answer_counter = 0 # Задаем переменную - счетчик правильных ответов.

# Далее три блока по количеству вопросов для пользователя и обработок данных от пользовательского ввода.
# Для значений правильных ответов задаю переменные. Как мне кажется, такой код более удобен для работы в будущем.
# Например, если потом нужно будем поменять вопросы для пользователя.

correct_answer_1 = "is"
user_answer_1 = input("My name ___ Vova ")
if user_answer_1 == correct_answer_1:
	print("Ответ верный! \nВы получаете 10 баллов!")
	score_counter += 10
	correct_answer_counter += 1
else:
	print(f"Неправильно \nПравильный ответ: {correct_answer_1}")

correct_answer_2 = "am"
user_answer_2 = input("I ___ coder ")
if user_answer_2 == correct_answer_2:
	print("Ответ верный! \nВы получаете 10 баллов!")
	score_counter += 10
	correct_answer_counter += 1
else:
	print(f"Неправильно \nПравильный ответ: {correct_answer_2}")

correct_answer_3 = "in"
user_answer_3 = input("I live ___ Moscow ")
if user_answer_3 == correct_answer_3:
	print("Ответ верный! \nВы получаете 10 баллов!")
	score_counter += 10
	correct_answer_counter += 1
else:
	print(f"Неправильно \nПравильный ответ: {correct_answer_3}")

# Для корректного вывода данных вводим еще две переменных:
# - определяющую верное окончание слова "вопрос" в зависимости от числа;
# - определяющую верное окончание слова "процент" в зависимости от числа.
# Я это делаю для потенциального масштабирования программы.
# Вдруг в перспективе она будет включать в себя более 3 вопросов. Ну и для тренировки тоже.

correct_writing_answ = "вопрос"
if 11 <= correct_answer_counter%100 <= 14 or 5 <= correct_answer_counter%10 <= 9 or correct_answer_counter%10 == 0:
	correct_writing_answ = "вопросов"
elif 2 <= correct_answer_counter%10 <= 4:
	correct_writing_answ = "вопроса"

# Здесь мы расчитываем значение процентого отношения набранных баллов
# к максимально возможному количеству:

correct_answer_perc = round(score_counter*100/30)

correct_writing_perc = "процент"
if 11 <= correct_answer_perc%100 <= 14 or 5 <= correct_answer_perc%10 <= 9 or correct_answer_perc%10 == 0:
	correct_writing_perc = "процентов"
elif 2 <= correct_answer_perc%10 <= 4:
	correct_writing_perc = "процента"

# После получения всех данных от пользователя и обработки их далее вывод информации
# о количестве правильных ответов, количестве баллов и процентом отношении набранных
# баллов к максимально возможному количеству:

print(f"\nВот и все, {user_name}! \nВы ответили на {correct_answer_counter} {correct_writing_answ} из 3 верно.")
print(f"Вы заработали {score_counter} баллов! \nЭто {correct_answer_perc} {correct_writing_perc}!")
