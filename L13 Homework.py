# Написати клас та реалізувати його методи: (основа – ДЗ № 10)
#

class File:

    def __init__(self, filename):
        self.filename = filename
        self.read_file = self.reading_file()

    def reading_file(self):

        with open(self.filename, "r") as temp_file:
            data = temp_file.readlines()

        return data

    def as_list(self):

        result = []

        for i in self.read_file:
            result.append(i.strip(".\n"))

        return result

    def only_lastnames(self):

        lastnames = []

        for i in self.read_file:
            lastnames.append(i.split("\t")[1])

        return lastnames

    def dict_dates(self):

        dict_dates = []

        for i in self.read_file:
            if " - " in i:
                dict_dates.append(dict(date=i.split(" - ")[0]))

        return dict_dates


# 1. Ініціалізація класу з одним параметром – ім'я файлу.
#

test_file = File("domains.txt")

print(test_file.filename)

# 2. Написати метод екземпляра класу, який створює атрибут екземпляра класу
# у вигляді списку рядків (назви повертати без крапки)
#

test_file.all_domains = test_file.as_list()

print(test_file.all_domains)

# 3. Написати метод екземпляра класу, який повертає список усіх прізвищ із файлу.
# Кожен рядок файлу містить номер, прізвище, країну, кілька (таблиця взята з вікіпедії).
# Розділювач - символ табуляції "t"
#

second_names = File("names.txt")

print(second_names.only_lastnames())

# 4. Написати метод екземпляра класу, який повертає список
# словників виду {"date": date} у яких date - це дата з рядка (якщо є),
# Наприклад [{"date": "1st January 1919"}, {"date": "8th February 1828"}, ...]
#

date_list = File("authors.txt")

print(date_list.dict_dates())

# 5* (*здавати не обов'язково).
# Написати метод екземпляра класу, отримує у вигляді параметра ім'я файлу (authors.txt) та повертає список
# словників виду {"date_original": date_original, "date_modified": date_modified}
# у яких date_original - це дата з рядка (якщо є),
# а date_modified - ця ж дата, представлена у форматі "dd/mm/yyyy" (d-день, m-місяць, y-рік)
# Наприклад [{"date_original": "8th February 1828", "date_modified": 08/02/1828}, ...]