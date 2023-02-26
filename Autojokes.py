# -*- coding: utf-8 -*-

from telethon import TelegramClient
from bs4 import BeautifulSoup
from random import choice
from requests import get


def get_recipient():
    """Функция ввода имени пользователя получателя"""
    recipient = ''
    while recipient == '':
        recipient = input('Введите username (пример: @VovkaPutin228): ')

    return recipient


def scrab():
    """Функция скрабинга страницы сайта"""
    page = ''
    for i in range(1, 5):  # берем информацию со всех страниц
        page += get('https://anekdoty.ru/pro-hoholov/page/' + str(i) + '/').text

        page = BeautifulSoup(page, 'lxml')  # делаем скрабинг страницы при помощи lxml
        page = page.find_all('p')  # находим на странице анеки

        return choice(page).text  # возвращаем рандомный анек


def message(api_id, api_hash, recipient):
    """Функция отправки сообщений"""
    try:
        while True:  # бесконечный цикл
            input('Нажмите клавишу ввода для отправки анекдота.')  # ждем нажатия клавиши
            with TelegramClient('AutoanecXD', api_id, api_hash) as client:  # отправляем сообщение пользователю
                client.loop.run_until_complete(client.send_message(recipient, scrab()))
            print('Анек отправлен XD')

    except KeyboardInterrupt:
        print('Остановлено вами.')

    except ValueError:
        print('Ошибка отправки адресату.')


def main():
    """Главная функция программы"""
    api_id = 69696969  # тг api id
    api_hash = 'а1337абоба228339'  # тг api hash
    message(api_id, api_hash, get_recipient())


if __name__ == '__main__':  # точка старта программы
    main()