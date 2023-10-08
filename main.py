from asyncio import run

from config import API_ID, API_HASH
from menu import Menu
from html_parser import HTMLParser


async def main():
    if API_ID == 0 or API_HASH == '':
        print("You have not entered API_ID and/or API_HASH")
        return
    
    if not await HTMLParser.is_internet_available():
        print("Error with internet connection!")
        return
    
    menu = Menu()
    parser = HTMLParser()
    jokes = await parser.gather_data(menu.get_topic())
    await menu.run_until_loop(jokes)


if __name__ == '__main__':
    run(main())
