import re
from collections import Counter

# шаблон страницы новостей (любые символы, потом / и 8 цифр подряд)
# http://www.petefreitag.com/cheatsheets/regex/
pattern = '.*/[0-9]{8}'
prog = re.compile( pattern )
# если поставить опцию 'w' при обращении к файлу, то он будет очищен
# если 'a' - данные будут добавлены в конец файла
a = []
with open('URLs.txt', 'r') as f:
    for line in f:
        # убираем символ переноса строки для каждой читаемой строчки
        line = line.strip()

        # если текст строки удовлетворяем регулярному выражению pattern, то выводим строку
        if prog.match(line):
            line2 = line.split('/')
            a.append(line2[1])
print(Counter(a))