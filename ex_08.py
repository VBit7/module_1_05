grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}

students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}


def formatted_grades(students):
    out_list = []
    for idx, key in enumerate(students):
        string = '{:>4}|{:<10}|{:^5}|{:^5}'
        out_list.append(string.format(idx + 1, key, students[key], grades[students[key]]))
    
    return out_list


print(formatted_grades(students))



'''
Будь-яке число можна записати кількома варіантами запису:

десятковий запис
двійкове представлення
шістнадцятиричне представлення
наукова нотація
з фіксованою точністю (кількістю знаків після коми) та інші.
Наприклад, вивести числа від 1 до 15 в десятковому, шістнадцятиричному, вісімковому і двійковому уявленні:

for i in range(16):
    s = "int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(i)
    print(s)
Крім того, при створенні рядків буває корисним відформатувати рядок так, щоб знаки на різних рядках були один під одним (додати пробілів),
додати заповнення в рядки для того, щоб результат був завжди однієї і тієї ж довжини.

Для таких і подібних завдань в Python вбудована міні-мова форматування рядків .

Або вивести квадрати та куби чисел до 12 у вигляді таблиці, відцентрувавши значення у стовпцях по 10 символів шириною:

width = 5
for num in range(12):
    print('{:^10} {:^10} {:^10}'.format(num, num ** 2, num ** 3))
Мета роботи з метамовою форматування полягає у вказівці у фігурних дужках, яким чином слід перетворити значення перед підстановкою.
Форматування працює і з f-рядками, але для більшій читабельності краще скористатися методом format,
який приймає як аргументи значення для підстановки в рядок, замість виразів у фігурних дужках.

Самі вирази у фігурних дужках можуть складатися з опису, в якому виді слід вивести число (формат запису, кількість знаків після коми та ін.),
і вказівки, чим доповнити рядок (додати пропусків на початку або у кінці, щоб рядок був N знаків завдовжки і т.п.).

Модифікатори
Міні-мова форматування рядків складається з таких модифікаторів, як:

ім'я поля — необов'язковий елемент, можемо вказати яку саме змінну сюди підставити по її імені:
s = "{name} {last_name}".format(last_name="Dilan", name="Bob")
print(s)  # Bob Dilan
перетворення — необов'язковий аргумент вказується після символу ! і може бути або r або s.
Відповідає за те, чи потрібно спробувати перетворити елемент, або відобразити елемент "як є":
s = "{name!r} {last_name!s}".format(last_name="Dilan", name="Bob")
print(s)  # 'Bob' Dilan
специфікація вказується після : і відповідає за те, як відобразити значення.
'''