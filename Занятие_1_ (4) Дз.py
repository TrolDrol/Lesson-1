def polindrom(clovo):
    adict = [clovo]
    adict2 = []
    adict2.append(clovo[::-1])
    if adict == adict2:
        print(True)
    else:
        print(False)

clovo = input(f'Введите слово: ')
polindrom(clovo)