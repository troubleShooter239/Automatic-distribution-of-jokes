# -*- coding: utf-8 -*-

from telethon import TelegramClient
from bs4 import BeautifulSoup
import requests, lxml, random


def scrab():
    """Функция скрабинга страницы сайта"""
    page = requests.get('https://anekdoty.ru/pro-hoholov/page/' + str(1) + '/')  # пока берем информацию с первой стр
    # с этого сайта можно не только про хохлов анеки кидать
    page = page.text  # преобразование в текст
    soup = BeautifulSoup(page, 'lxml')  # делаем скраблинг страницы при помощи lxml
    page_p = soup.find_all('p')  # находим на странице анеки

    return random.choice(page_p).text # возвращаем рандомный анек


def message(internal_api_id, internal_api_hash, internal_recipient):
    """Функция отправки сообщений"""
    with TelegramClient('AutoanecXD', internal_api_id, internal_api_hash) as client:
        client.loop.run_until_complete(client.send_message(internal_recipient, scrab())) # зацикливаем пока не отправиться сообщение
    print('Анек отправлен XD')


def main():
    """Главная функция программы"""
    # поменять айди и хэш на рандомные чтобы меня не взломали нахуй
    api_id = 2353286  # тг api id
    api_hash = 'a37d3089e20a5cd6e6743b78d59b0b74'  # тг api hash
    recipient = 'me'  # получатель анеков

    message(api_id, api_hash, recipient)


if __name__ == '__main__':
    main()
