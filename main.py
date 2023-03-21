# -*- coding: utf-8 -*-

try:  # Обрабатываем сообщения об ошибке
    # Подключаем модули, которые понадобятся нам в скрипте
    from telethon import TelegramClient as tg
    from bs4 import BeautifulSoup as bs
    from requests import get
    from traceback import print_exc
    from sys import stdout
    from random import choice
    import lxml


    def choice_topic():
        """Функция выбора темы анекдотов"""
        print('1. Хохлы\n2. Программисты\n3. Гитлер\n4. Негры\n'
              '5. Секс\n6. Черный юмор\n7. Про мать')
        while True:
            try:
                topic = int(input('Выберите тему (цифра): '))
                if topic == 1 or topic == 2 or topic == 3 or \
                        topic == 4 or topic == 5 or topic == 6 or topic == 7:
                    break
                else:  # Если ввели значение больше (меньше), чем представлено
                    print('Нет такого пункта меню. Попробуйте снова: ')

            except ValueError:  # Исключение, если ввели не число
                print('Вы ввели не число. Попробуйте снова: ')
        return topic  # Возвращаем номер темы


    def parsing(amount, url):
        """Функция парсинга каждой страницы с анекдотами по выбранной теме"""
        jokes = []  # В этом списке будем хранить анекдоты
        for i in range(2, amount):  # Прогоняем все страницы
            page = get(url + str(i) + '/')  # Собираем html-код со страницы
            page = bs(page.text, 'lxml')  # Делаем парсинг страницы при помощи lxml
            page = page.find_all('p')  # Находим на странице анекдоты (они помечены тегом <p>)
            jokes += [i.text for i in page]  # Собираем все анекдоты в один список
        return jokes  # Возвращаем список


    def collection_of_jokes(topic):
        """Функция, возвращающая рандомный анекдот"""
    num = randint(1, 16)
    if num == 1:  # Выбор ссылки и кол-ва страниц для заданной темы
        amount = 4
        url = 'https://anekdoty.ru/pro-hoholov/page/'
    elif num == 2:
        amount = 12
        url = 'https://anekdoty.ru/pro-programmistov/page/'
    elif num == 3:
        amount = 3
        url = 'https://anekdoty.ru/pro-gitlera/page/'
    elif num == 4:
        amount = 11
        url = 'https://anekdoty.ru/pro-negrov/page/'
    elif num == 5:
        amount = 22
        url = 'https://anekdoty.ru/pro-seks/page/'
    elif num == 6:
        amount = 6
        url = 'https://anekdoty.ru/cherniy-yumor/page/'
    elif num == 7:
        amount = 15
        url = 'https://anekdoty.ru/pro-mamu/page/'
    elif num == 8:
        amount = 26
        url = 'https://anekdoty.ru/detskie/page/'
    elif num == 9:
        amount = 7
        url = 'https://anekdoty.ru/pro-armyan/page/'
    elif num == 10:
        amount = 19
        url = 'https://anekdoty.ru/pro-gruzinov/page/'
    elif num == 11:
        amount = 3
        url = 'https://anekdoty.ru/pro-klounov/page/'
    elif num == 12:
        amount = 20
        url = 'https://anekdoty.ru/samye-smeshnye/page/'
    elif num == 13:
        amount = 28
        url = 'https://anekdoty.ru/tupo-no-smeshno/page/'
    elif num == 14:
        amount = 14
        url = 'https://anekdoty.ru/korotkie/page/'
    elif num == 15:
        amount = 2
        url = 'https://anekdoty.ru/pro-invalidov/page/'
    else:
        amount = 5
        url = 'https://anekdoty.ru/pro-mobilizaciyu/page/'
        
    return parsing(amount, url)  # Возвращаем все анекдоты по выбранной теме


    def get_recipient():
        """Функция ввода имени пользователя получателя"""
        recipient = ''  # Здесь будем хранить имя получателя
        while recipient == '':  # Пока не исчезнет пустота...
            recipient = input('Введите имя или номер получателя '
                              '(пример: @VovkaPutin228): ')  # Выводим...
        return recipient  # Возвращаем имя получателя


    def amount_of_jokes():
        """Функция ввода кол-ва отправляемых анеков"""
        while True:
            try:  # Проверка, вводит ли пользователь число
                amount = int(input('Введите кол-во анекдотов, которых отправим '
                                   '(0 для отправки по нажатии клавиши Enter): '))
                break

            except ValueError:  # Исключение, если вводим не число
                print('Вы ввели не число. Попробуйте снова: ')
        return amount  # Возвращаем кол-во анекдотов


    def message(api_id, api_hash, recipient, jokes):
        """Функция отправки сообщений"""
        amount = amount_of_jokes()  # Здесь храним кол-во анекдотов
        if amount == 0:  # Если ввели кол-во анекдотов равное 0
            # Данный блок работает, пока не завершим работу скрипта в целом
            while True:  # Бесконечный цикл...
                input('Нажмите клавишу ввода для отправки анекдота.')  # Ждем нажатия клавиши...
                with tg('AutoanecXD', api_id, api_hash) as client:  # Отправляем сообщение пользователю...
                    client.loop.run_until_complete(client.send_message(recipient, choice(jokes)))
                print('Анекдот отправлен XD')

        else:  # Если кол-во анекдотов не равно 0
            for i in range(amount):  # Запускаем цикл, при котором отправляем нужное кол-во анекдотов
                with tg('AutoanecXD', api_id, api_hash) as client:  # Отправляем сообщение пользователю
                    client.loop.run_until_complete(client.send_message(recipient, choice(jokes)))
                print(i + 1, ' Анекдот отправлен XD')


    def main():
        """Главная функция программы"""
        #################################################
        api_id = 0  # Telegram api id (Сюда нужно ввести свои значения)
        api_hash = ''  # Telegram api hash (Сюда нужно ввести свои значения)
        #################################################
        if api_id == 0 or api_hash == '':
            print('Вы не ввели api_id и (или) api_hash')
            return 0

        recipient = get_recipient()  # Выбор получателя
        topic = choice_topic()  # Выбор темы анекдотов
        print('Идёт поиск анекдотов по заданной теме. Пожалуйста, подождите...')
        jokes = collection_of_jokes(topic)  # Запускаем сбор анекдотов в список
        print('Все анекдоты найдены!')
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
