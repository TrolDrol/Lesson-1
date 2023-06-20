# def is_polindrom(word):
#     adict = [word]
#     adict2 = []
#     adict2.append(word[::-1])
#     if adict == adict2:
#         return True
#     else:
#         return False
#
# word = input(f'Введите слово: ')
# print(is_polindrom(word)) # Решил оставить и 1 вариант для себя
def is_polindrom(word):
    if word == word[::-1]:
        return True
    else:
        return False

word = input(f'Введите слово: ')
print(is_polindrom(word))