print("Введите текст: ")
text = input()
text1 = text.split() if text.count("") >= 1 else text

pat = text1[0][-2:]
res = ''
if pat == 'ей':
    for i in text1:
        if i[-3:] == 'хей':
            res += i[-4]+i[:-4]+" "
        else:
            res += i[:-2]+" "

else:
    for i in text1:
        if i[0] not in 'уеыаоэяию':
            res += i[1:] + i[0] + 'хей '
        else:
            res += i + 'ей '

print(res)