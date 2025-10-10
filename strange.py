import re
SOGlAS = 'йцкнгшщзхфвпрлджчсмтб'

file = input("Введите файл содержащий текст для перевода")
with open(file, "r", encoding='utf-8') as f, open("out.txt", "w", encoding='utf-8') as out:
    for line in f:
        st = re.sub(r'[,.?/!:—-]+', '', line)
        ob = st.split()
        for word in ob:
            p = word.lower()
            if p[0] in SOGlAS:
                out.write(p[1::] + p[0] + 'ей ')
            if p[0] not in SOGlAS:
                out.write( p + 'хей ')
        out.write('\n')
print("Текст переведён")