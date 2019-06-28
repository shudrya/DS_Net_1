# -*- coding: utf8 -*-
queries = 'смотреть сериалы онлайн,новости,какая рыба вобла,пхенчхан золото онлайн,сколько дней до 8 марта'
words = ['онлайн', 'золото']
temp_list = queries.split(',')
print([item for item in temp_list if not any(x in item for x in words)])


big_data_list = [
    ['google', 'cpc', 925],
    ['yandex', 'organic', 790],
    ['market', 'cpc', 465],
    ['google', 'organic', 413],
    ['google', 'cpc', 398],
    ['direct', 'none', 115],
    ['yandex', 'cpc', 43]
]
stats = {}
for line in big_data_list:
    stats.setdefault(line[1], 0)
    stats[line[1]] += 1
print(stats)