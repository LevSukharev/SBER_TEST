import re
from functools import cmp_to_key
'''
Напишите функцию, которая принимает на вход строку и для каждого особенного номера, встречающегося в строке, выводит соответствующий хороший номер.
'''
def task1(s: str) -> str:
    all_numbers = re.findall(r'^\d{2,4}\\\d{2,5}\D', s) \
                  + re.findall(r'\D\d{2,4}\\\d{2,5}\D', s) \
                  + re.findall(r'\D\d{2,4}\\\d{2,5}$', s)
    special_numbers = [''.join(filter(lambda x: x.isdigit() or x == '\\', list(i))).split('\\') for i in all_numbers]
    del all_numbers
    special_numbers = list(map(lambda x: '\\'.join([('00'+x[0])[-4:], ('000'+x[1])[-5:]]), special_numbers))

    return special_numbers
'''
Напишите функцию, которая добавляет k банкоматов таким образом, чтобы максимальное расстояние между соседними банкоматами являлось минимально возможным, 
и возвращает список новых расстояний между банкоматами.
'''
def task2():
    present_atms, future_atms = [int(i) for i in input().split()]
    intervals = [int(input()) for _ in range(present_atms)]
    for _ in range(future_atms):
        index_of_max = intervals.index(max(intervals))
        new_interval = int(intervals.pop(index_of_max) / 2)
        intervals = intervals[:index_of_max] + [new_interval] * 2 + intervals[index_of_max:]
    return intervals
'''
Напишите функцию, которая принимает на вход список строк, состоящих из цифр, и возвращает максимальное возможное число, 
которое может получиться в результате конкатенации всех строк из этого списка.
'''
def task3(strings: list) -> int:
    if strings:
        return (int(''.join(
            list(sorted(strings, key=cmp_to_key(lambda p1, p2: int(p1 + p2) - int(p2 + p1)), reverse=True)))))
    else:
        return 0




