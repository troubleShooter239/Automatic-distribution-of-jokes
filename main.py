# Подключаем модули, которые понадобятся нам в скрипте
from telethon import TelegramClient as tg
from bs4 import BeautifulSoup as bs
from requests import get
from random import choice
from config import API_ID, API_HASH
import lxml


def choice_topic() -> str:
    """
    Функция выбора темы анекдотов
    """
    print(
        '1. Программисты\n'
        '2. Черный юмор\n'
        '3. Детские\n'
        '4. Самые смешные\n'
        '5. Тупо, но смешно\n'
        '6. Короткие'
    )

    while True:
        topic = input('Выберите тему (цифра): ')
        if topic == '1' or topic == '2' or topic == '3' or \
                topic == '4' or topic == '5' or topic == '6' or topic == '7':
            break
        else:  # Если ввели значение больше (меньше), чем представлено
            print('Нет такого пункта меню. Попробуйте снова: ')

    return topic  # Возвращаем номер темы


def parsing(amount: int, url: str) -> list:
    """
    Функция парсинга каждой страницы с анекдотами по выбранной теме
    """
    page = get(url)  # Собираем html-код с первой страницы
    page = bs(page.text, 'lxml')  # Делаем парсинг страницы при помощи lxml
    jokes = [i.text for i in page.find_all('p')]  # Собираем все анекдоты в один список

    for i in range(2, amount):  # Прогоняем все остальные страницы
        page = get(url + str(i) + '/')  # Собираем html-код со страницы
        page = bs(page.text, 'lxml')  # Делаем парсинг страницы при помощи lxml
        jokes += [i.text for i in page.find_all('p')]  # Собираем все анекдоты в один список

    return jokes  # Возвращаем список


def collection_of_jokes(topic: str) -> list:
    """
    Функция, возвращающая рандомный анекдот
    """
    if topic == '1':
        amount = 12
        url = 'https://anekdoty.ru/pro-programmistov/'
    elif topic == '2':
        amount = 6
        url = 'https://anekdoty.ru/cherniy-yumor/'
    elif topic == '3':
        amount = 26
        url = 'https://anekdoty.ru/detskie/'
    elif topic == '4':
        amount = 20
        url = 'https://anekdoty.ru/samye-smeshnye/'
    elif topic == '5':
        amount = 28
        url = 'https://anekdoty.ru/tupo-no-smeshno/'
    else:
        amount = 14
        url = 'https://anekdoty.ru/korotkie/'

    return parsing(amount, url)  # Возвращаем все анекдоты по выбранной теме


def get_recipient() -> str:
    """
    Функция ввода имени пользователя получателя
    """
    recipient = ''  # Здесь будем хранить имя получателя
    while recipient == '':  # Пока не исчезнет пустота...
        recipient = input(
            'Введите имя или номер получателя '
            '(пример: @VovkaPutin228): '
        )  # Выводим...

    return recipient  # Возвращаем имя получателя


def amount_of_jokes() -> int:
    """
    Функция ввода кол-ва отправляемых анекдотов
    """
    while True:
        try:  # Проверка, вводит ли пользователь число
            amount = int(input(
                'Введите кол-во анекдотов, которых отправим '
                '(0 для отправки по нажатии клавиши Enter): '
            ))
            break

        except ValueError:  # Исключение, если вводим не число
            print('Вы ввели не число. Попробуйте снова: ')

    return amount  # Возвращаем кол-во анекдотов


def message(api_id: int, api_hash: str, recipient: str, jokes: list):
    """
    Функция отправки сообщений
    """
    amount = amount_of_jokes()  # Здесь храним кол-во анекдотов

    try:
        if amount == 0:  # Если ввели кол-во анекдотов равное 0
            # Данный блок работает, пока не завершим работу скрипта в целом
            while True:  # Бесконечный цикл...
                input('Нажмите клавишу ввода для отправки анекдота.\n')  # Ждем нажатия клавиши...
                with tg('AutoanecXD', api_id, api_hash) as client:  # Отправляем сообщение пользователю...
                    client.loop.run_until_complete(client.send_message(recipient, choice(jokes)))
                print('Анекдот отправлен XD')

        else:  # Если кол-во анекдотов не равно 0
            for i in range(amount):  # Запускаем цикл, при котором отправляем нужное кол-во анекдотов
                with tg('AutoanecXD', api_id, api_hash) as client:  # Отправляем сообщение пользователю
                    client.loop.run_until_complete(client.send_message(recipient, choice(jokes)))
                print(i + 1, ' Анекдот отправлен XD')

    except KeyboardInterrupt:
        print("Остановлено вами. ")


def main():
    """
    Главная функция программы
    """
    if API_ID == 0 or API_HASH == '':
        print('Вы не ввели api_id и (или) api_hash')
        return 0

    recipient = get_recipient()  # Выбор получателя

    topic = choice_topic()  # Выбор темы анекдотов

    print('Идёт поиск анекдотов по заданной теме. Пожалуйста, подождите...')
    jokes = collection_of_jokes(topic)  # Запускаем сбор анекдотов в список
    print('Все анекдоты найдены!')

    message(API_ID, API_HASH, recipient, jokes)  # Запускаем отправку анекдотов адресату


if __name__ == '__main__':  # Точка старта программы
    main()
