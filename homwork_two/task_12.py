#Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
#школьница. Петя помогает Кате по математике. Он задумывает два
#натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
#этого Петя делает две подсказки. Он называет сумму этих чисел S и их
#произведение P. Помогите Кате отгадать задуманные Петей числа.
S = 8
P = 15
x = abs(int(input('Введите первое натуральное число X ')))
y = abs(int(input('Введите второе натуральное число Y ')))
if x + y == S and x * y == P:
    print("числа верные")
else:
    print("числа не верные")


