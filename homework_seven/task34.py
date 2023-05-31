#Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
#  Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
#  Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов
#  (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
#  Фраза может состоять из одного слова, если во фразе несколько слов,
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
#  В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”,
# сли с ритмом все не в порядке
def count_vowels(phrase: str) -> int:
    number = 0
    for char in phrase:
        if char in letters:
            number += 1
    return number


def is_right_rhythm_poem(poem: str) -> bool:
    phrases = poem.lower().split(" ")
    return len(set(map(count_vowels, phrases))) == 1

letters = "аеёиоуыэюя"
if is_right_rhythm_poem(input("Винни-Пух, вбей своё стихотворение: ")):
    print("Парам пам-пам")
else:
    print("Пам парам")