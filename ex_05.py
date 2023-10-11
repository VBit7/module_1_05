def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


def get_phone_numbers_for_countries(list_phones):
    dict_phone = {'JP': [], 'SG': [], 'TW': [], 'UA': []}

    # dict_iso = {'JP': '81',
    #             'SG': '65',
    #             'TW': '886',
    #             'UA': '380'
    #            }
    
    for item in list_phones:
        item = sanitize_phone_number(item)
        print(item)
        if item.find('81') == 0:
            dict_phone['JP'].append(item)
        elif item.find('65') == 0:
            dict_phone['SG'].append(item)
        elif item.find('886') == 0:
            dict_phone['TW'].append(item)
        else:
            dict_phone['UA'].append(item)

    return dict_phone


print(get_phone_numbers_for_countries([' +38(050)123-32-34', '0503451234', '(050)8889900', '+819000111223', '+651234567890', '+886444556678']))


'''
Повернемося до нашого завдання із телефонними номерами. Компанія розширюється та вийшла на ринок Азії.
Тепер у списку можуть знаходитись телефони різних країн. Кожна країна має свій телефонний код .

Компанія працює з наступними країнами

Країна      Код ISO   Префікс
Japan       JP        +81
Singapore   SG        +65
Taiwan      TW        +886
Ukraine     UA        +380
Щоб ми могли коректно виконати рекламну SMS кампанію, необхідно створити для кожної країни свій список телефонних номерів.

Напишіть функцію get_phone_numbers_for_сountries, яка буде:

1. Приймати список телефонних номерів.
2. Санітизувати (нормалізувати) отриманий список телефонів клієнтів за допомогою нашої функції sanitize_phone_number.
3. Сортувати телефонні номери за вказаними у таблиці країнами.
4. Повертати словник зі списками телефонних номерів для кожної країни у такому вигляді:
{
    "UA": [<тут список телефонів>],
    "JP": [<тут список телефонів>],
    "TW": [<тут список телефонів>],
    "SG": [<тут список телефонів>]
}
5. Якщо не вдалося порівняти код телефону з відомими, цей телефон повинен бути доданий до списку словника з ключем 'UA'.
'''