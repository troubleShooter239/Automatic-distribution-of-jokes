from asyncio import create_task, gather

from bs4 import BeautifulSoup
from aiohttp import ClientSession

from config import TOPIC_INFO


class HTMLParser:
    """
    A class for asynchronously parsing web pages and collecting jokes based on selected topics.

    Attributes:
        topic_info (dict): A dictionary mapping topic names to their corresponding URL and number of pages.
        jokes (list): A list of collected jokes as strings.

    Methods:
        __init__(self) -> None:
            Initializes an instance of the HTMLParser class.

        get_jokes(self) -> list[str]:
            Returns the collected jokes.

        is_internet_available(self) -> bool:
            Checks if an internet connection is available.

        get_page_data(self, session: ClientSession, url: str) -> None:
            Asynchronously retrieves and parses HTML content from a given URL using BeautifulSoup.

        gather_data(self, topic: str) -> list[str]:
            Asynchronously gathers data from multiple pages for the specified topic and returns the collected jokes.
    """
    def __init__(self) -> None:
        self.topic_info: dict = TOPIC_INFO
        self.jokes: list[str] = []
    
    def get_jokes(self) -> list[str]:
        """
        Returns the collected jokes.

        Returns:
            list[str]: A list of collected jokes as strings.
        """
        return self.jokes
    
    @staticmethod
    async def is_internet_available() -> bool:
        """
        Checks if an internet connection is available.

        Returns:
            bool: True if the internet connection is available, False otherwise.
        """
        try:
            async with ClientSession() as session:
                async with session.get("https://www.google.com", timeout=5) as response:
                    return response.status == 200
        except Exception:
            return False
        
    async def get_page_data(self, session: ClientSession, url: str):
        """
        Asynchronously retrieves and parses HTML content from a given URL 
        using BeautifulSoup.

        Args:
            session (ClientSession): An aiohttp ClientSession for making HTTP requests.
            url (str): The URL of the web page to be parsed.
        """
        async with session.get(url) as response:
            soup = BeautifulSoup(await response.text(), "lxml")
            self.jokes += [i.text for i in soup.find_all('p')] 
            print(f"[INFO]Parsed page: {url}")
    
    async def gather_data(self, topic: str) -> list[str]:
        """
        Asynchronously gathers data from multiple pages for the specified 
        topic and returns the collected jokes.

        Args:
            topic (str): The selected topic for collecting jokes.

        Returns:
            list[str]: A list of collected jokes as strings.
        """
        async with ClientSession() as session:
            number_pages, url = self.topic_info[topic]
            tasks = []
            
            for i in range(2, number_pages + 1):
                task = create_task(self.get_page_data(session, url + str(i) + '/'))
                tasks.append(task)
                
            await gather(*tasks)
        print("[INFO]Done.")           
        return self.jokes
