def real_len(text: str) -> int:

    text = text.replace('\n', '') \
               .replace('\f', '') \
               .replace('\r', '') \
               .replace('\t', '') \
               .replace('\v', '')

    return len(text)


print(real_len('Alex\nKdfe23\t\f\v.\r'))



"""
Напишіть функцію real_len, яка підраховує та повертає довжину рядка без наступних керівних символів: [\n, \f, \r, \t, \v]

Для перевірки правильності роботи функції real_len їй будуть передані наступні рядки:

'Alex\nKdfe23\t\f\v.\r'
'Al\nKdfe23\t\v.\r'
"""