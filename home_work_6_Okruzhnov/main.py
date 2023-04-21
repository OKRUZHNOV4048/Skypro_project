import re

from functions import shuffling_letters_words_dict
from functions import random_word_assignment

user_name = input("Введите ваше имя!\n")

with open("words.txt", "r") as file:
    dict_file_words = {}  # A dictionary formed from words from a custom text file.
    dict_key_counter = 1
    for line in file:
        word_list = line.rstrip("\n")
        dict_file_words[dict_key_counter] = word_list
        dict_key_counter += 1

score_counter = 0
question_counter = 0

while question_counter < 4:

    # A jumbled-word dictionary
    # comparable in key sequence to a dictionary
    # formed from words from a custom text file.
    dict_jumbled_words = shuffling_letters_words_dict(dict_file_words)

    # Random jumbled word with index.
    # The index is needed to compare with the index of the source dictionary
    # to determine the correctness of the answer.
    random_jumbled_word_with_i = random_word_assignment(dict_jumbled_words)

    # Random jumbled word.
    random_jumbled_word = random_jumbled_word_with_i[0]

    # The index of the random jumbled word.
    random_jumbled_i = random_jumbled_word_with_i[1]

    answer_user = input(f"Угадайте слово: {random_jumbled_word}\n")

    if answer_user == dict_file_words[random_jumbled_i]:
        print("Верно! Вы получаете 10 очков")
        score_counter += 10
        question_counter += 1
    else:
        print(f"Неверно! Верный ответ – {dict_file_words[random_jumbled_i]}.")
        question_counter += 1

with open("history.txt", "a", encoding="utf-8") as file:
    file.write(user_name + " " + str(score_counter) + "\n")

with open("history.txt", "r", encoding="utf-8") as file:
    score_and_name_list = []
    for line in file:
        score_and_name_list.append(line.rstrip("\n"))

score_and_name_str = "".join(score_and_name_list)

score_str = re.sub("[^0-9]", " ", score_and_name_str)
score_str = score_str.split()
score_list = []
for i in score_str:
    score_list.append(int(i))

print(f"Всего игр сыграно: {len(score_and_name_list)} игр.")
print(f"Максимальный рекорд: {max(score_list)}.")
