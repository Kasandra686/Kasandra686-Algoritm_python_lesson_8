# Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
# Пример работы функции:
#
# func("papa")
# 6
# func("sova")
# 9

import hashlib

s = input('Введите строку: ')


def substrings_counter(s):
    hash_list = set()
    count = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if s[i:j] != '' and s[i:j] != s:
                hash_list.add(hashlib.sha1(s[i:j].encode('utf-8')).hexdigest())
                count = len(hash_list)

    print(f'Сумма подстрок: {count}')


substrings_counter(s)
