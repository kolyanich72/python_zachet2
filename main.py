from faker import Faker
import json
from conf import MODEL as M
from random import randint as rndm_n, uniform as rndm_flt

fk = Faker('ru_RU')


def pk_(counter_pk=1):
    """
    функция генератор
    устанавливается начальное значение через аргумент функции-генератора на момент инициализации.
    :param counter_pk:
    :return: int
    """
    while True:
        yield counter_pk
        counter_pk += 1


def gen_title():
    """генерация названия книги
    :return: str
    """
    return fk.text(max_nb_chars=20)


def gen_isbn():
    """генерация м/н номера isbn13 книги
    :return: int
    """
    return fk.isbn13()


def gen_author(x: int):
    """генерация списка авторов книги
    :param количество авторов = int
    :return: список авторов = list
    """
    aut_list = [fk.name() for i in range(x)]
    return aut_list


def f_book_gen():
    """
    генератор книги
    :return: dictionary
    """
    bk = {'title': gen_title(), 'year': rndm_n(1800, 2023), 'pages':  rndm_n(1, 500),
          'isbn13':  gen_isbn(), 'rating': rndm_n(0, 5),
          'price': round(rndm_flt(1, 10000), 2), 'author': gen_author(rndm_n(1, 3))
          }
    return bk


def initial():
    """
    запуск формирования файла json со списком из 100 книг
    :return:
    """
    with open('json_book_file', 'w', encoding='utf-8') as f1:
        for _ in range(1, 101):
            pk = next(pk_(_))
            data = {'model': M, 'pk': pk, 'fields': f_book_gen()}
            f1.write(json.dumps(data, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    initial()
