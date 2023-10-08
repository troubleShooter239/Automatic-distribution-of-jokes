from telethon import TelegramClient


class MessageSender:
    """
    A class for sending messages using the Telethon library.
    
    Attributes:
        session_name (str): The name of the Telethon session.
        api_id (int): The API ID provided by Telegram for your application.
        api_hash (str): The API hash provided by Telegram for your application.
        recipient (str): The username or phone number of the message recipient.

    Methods:
        send_message(message: str) -> None:
            Sends a message to the specified recipient asynchronously.
    
    Example Usage:
        sender = MessageSender('my_session', 123456, 'my_api_hash', '@recipient_username') 
        
        await sender.send_message("Hello!")
    """
    def __init__(self, session_name: str, 
                 api_id: int, api_hash: str,
                 recipient: str) -> None:
        self.session_name = session_name
        self.api_id = api_id
        self.api_hash = api_hash
        self.recipient = recipient
        
    async def send_msg(self, message: str):
        """
        Send message to recipient asynchronously.
        
        Args:
            message (str): The message to send.
        """
        try:
            async with TelegramClient(self.session_name, 
                                      self.api_id, self.api_hash) as client:
                await client.send_message(self.recipient, message)
        except ConnectionError as e:
            print(f"Error! {e}")
            