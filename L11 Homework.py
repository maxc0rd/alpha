# Всі пункти є частиною одного завдання, тому можна використовувати функції кілька разів та не дублювати код.
# Якщо хочете, можете використовувати дефолтні значення та анотацію типів.
#
# 1. Написати функцію, яка отримує один параметр - ім'я директорії та повертає словник виду
# {'filenames': [список файлів у папці], 'dirnames': [список усіх підпапок у папці]}.
# Підпапки враховувати лише першого рівня вкладення. Папка в папці в папці - таке не брати))
#
import os


def create_dirs_list(dirname: str) -> list:

    dirs_list = os.listdir(dirname)
    for dirs in dirs_list.copy():
        if not os.path.isdir(os.path.join(dirname, dirs)):
            dirs_list.remove(dirs)

    return dirs_list


def create_files_list(dirname: str) -> list:

    files_list = os.listdir(dirname)
    for file in files_list.copy():
        if not os.path.isfile(os.path.join(dirname, file)):
            files_list.remove(file)

    return files_list


def files_dirs_dict(dirname: str) -> dict:

    dict_1 = {"filenames": create_files_list(dirname), "dirnames": create_dirs_list(dirname)}

    return dict_1


fd_dict = files_dirs_dict("Folder1")
print(fd_dict)

# 2. Написати функцію, яка отримує два параметри – словник, описаний у пункті 1
# і значення булю (True/False) - можна зробити за замовчуванням.
# Функція повертає той самий словник, але з відсортованими іменами файлів та папок у відповідних списках.
# Булеве значення True означає, що порядок сортування алфавітний, False – зворотний порядок.
#


def sorting_dict(some_dict: dict, boolean: bool = False) -> dict:

    temp_dict = some_dict.copy()
    if boolean:
        temp_dict["filenames"].sort()
    else:
        temp_dict["dirnames"].sort(reverse=True)

    return temp_dict


print(sorting_dict(fd_dict, True))

# 3. Написати функцію, яка отримує два параметри - словник, описаний у пункті 1 та рядок, який може бути
# або ім'ям файлу, або ім'ям папки. (У імені файлу має бути точка).
# Залежно від того, що функція отримала (ім'я файлу або ім'я папки) – записати його у відповідний список
# та повернути оновлений словник.
#


def updated_dict(same_dict: dict, some_str: str) -> dict:

    upd_dict = same_dict.copy()
    if "." in some_str:
        upd_dict["filenames"].append(some_str)
    else:
        upd_dict["dirnames"].append(some_str)

    return upd_dict


print(updated_dict(fd_dict, "find.txt"))

# 4* (*здавати не обов'язково).
# Написати функцію, яка отримує два параметри - словник, описаний у пункті 1 та ім'я директорії.
# Функція перевіряє відповідність отриманого словника та реальної файлової системи в отриманій папці та,
# якщо треба, створює потрібні папки та порожні файли, відповідно до структури словника.
#

