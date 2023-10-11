import re


def replace_spam_words(text, spam_words):
    for item in spam_words:
        search_str = r'\b' + re.escape(item)
        replace_str = '*' * len(item)
        text = re.sub(search_str, replace_str, text, flags=re.IGNORECASE)

    return text


print(replace_spam_words('blue socks and red shoes', ['blue', 'white', 'red']))



'''
У шостій задачі ми писали функцію is_spam_words, яка визначала, чи є чи ні стоп-слова у тексті повідомлення.
Підемо далі та застосуємо функцію sub модуля re для заміни вказаних у списку стоп-слів на деякий шаблон.
Наприклад, всі "погані" слова замінюватимемо зірочками.
Напишіть функцію replace_spam_words, яка приймає рядок (параметр text),
перевіряє його на вміст заборонених слів зі списку (параметр spam_words),
та повертає результат рядок, але замість заборонених слів, підставлений шаблон з *,
причому довжина шаблону дорівнює довжині забороненого слова. Визначити нечутливість до регістру стоп-слів.
'''