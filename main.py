# -*- coding: utf-8 -*-

try:  # Обрабатываем сообщения об ошибке
    # Подключаем модули, которые понадобятся нам в скрипте
    from telethon import TelegramClient as tg
    from bs4 import BeautifulSoup as bs
    from requests import get
    from traceback import print_exc
    from sys import stdout
    from random import choice


    def parsing():
        """Функция парсинга страницы сайта"""
        jokes = []  # Объявляем список для сбора анекдотов со всех страниц
        for i in range(1, 5):  # Берем информацию со всех страниц
            page = get('https://anekdoty.ru/pro-hoholov/page/' + str(i) + '/')  # Собираем html-код со страницы
            page = bs(page.text, 'lxml')  # Делаем парсинг страницы при помощи lxml
            page = page.find_all('p')  # Находим на странице анекдоты (они помечены тегом <p>)
            jokes += [i.text for i in page]  # Собираем все анекдоты в один список
        return jokes  # Возвращаем все анекдоты


    def get_recipient():
        """Функция ввода имени пользователя получателя"""
        recipient = ''
        while recipient == '':  # Пока не исчезнет пустота...
            recipient = input('Введите username (пример: @VovkaPutin228): ')  # Выводим...
        return recipient  # Возвращаем имя получателя


    def amount_of_jokes():
        """Функция ввода кол-ва отправляемых анеков"""
        print('Введите кол-во анеков, которых отправим (0 для отправки по нажатии Enter): ')
        while True:
            try:  # Проверка, вводит ли пользователь число
                amount = int(input())
                break
            except ValueError:
                print('Вы ввели не число. Попробуйте снова: ')
        return amount  # Возвращаем кол-во анекдотов


    def message(api_id, api_hash, recipient, jokes):
        """Функция отправки сообщений"""
        amount = amount_of_jokes()
        if amount == 0:  # Если ввели кол-во анекдотов равное 0
            # Данный блок работает, пока не завершим работу скрипта в целом
            while True:  # Бесконечный цикл...
                input('Нажмите клавишу ввода для отправки анекдота.\n')  # Ждем нажатия клавиши...
                with tg('AutoanecXD', api_id, api_hash) as client:  # Отправляем сообщение пользователю...
                    client.loop.run_until_complete(client.send_message(recipient, choice(jokes)))
                print('Анек отправлен XD')

        else:  # Если кол-во анекдотов не равно 0
            for i in range(amount):  # Запускаем цикл, при котором отправляем нужное кол-во анекдотов
                with tg('AutoanecXD', api_id, api_hash) as client:  # Отправляем сообщение пользователю
                    client.loop.run_until_complete(client.send_message(recipient, choice(jokes)))
                print(i + 1, ' Анек отправлен XD')


    def main():
        """Главная функция программы"""
        jokes = parsing()  # Запускаем сбор анекдотов в список
        api_id = 12345  # Telegram api id (Сюда нужно ввести свои значения)
        api_hash = 'adsa986987897hgfg78798a7fa7898321'  # Telegram api hash (Сюда нужно ввести свои значения)
        recipient = get_recipient()
        message(api_id, api_hash, recipient, jokes)  # Запускаем отправку анекдотов адресату


    if __name__ == '__main__':  # Точка старта программы
        main()


except KeyboardInterrupt:  # При нажатии ctrl + c
    print('\nОстановлено вами.')

except ValueError:  # Если ввести некорректные данные
    print('\nОшибка отправки адресату.')

except 0:  # Обрабатываем ошибки...
    print('\nПроизошла неизвестная ошибка.')  # Сообщение об ошибке
    print('\n=======ИНФОРМАЦИЯ ОБ ОШИБКЕ=========')  # Верхняя граница репорта об ошибке
    print_exc(limit=2, file=stdout)  # Подробный репорт об ошибке и ее причинах
    print('========КОНЕЦ========')  # Конец репорта
