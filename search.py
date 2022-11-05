file = open("расположение файла")
word = input ("Какое слово нужно найти? :")
number = 0
count = 0
lines = list()
for line in file:
    count += 1
    if word in line:
        number += 1
        lines.append(count)
        print(line.rstrip())
if number != 0 :
    print(f"Введенное слово повторяется в тексте {number} раз в {count} строчках")
else:
    print("Введенного слова нет в тексте")

