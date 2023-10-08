from random import choice

from message_sender import MessageSender
import config


class Menu:
    """
    A class for configuring message settings interactively.

    Methods:
        __init__(self) -> None:
            Initializes the Menu instance and collects user inputs for topic, recipient, and the number of jokes to send.

        get_topic(self) -> str:
            Returns the selected topic.

        enter_topic(self) -> str:
            Prompt the user to select a topic and return the chosen topic as a string.

        enter_recipient(self) -> str:
            Prompt the user to enter the recipient's username or number and return it as a string.

        get_number_jokes(self) -> int:
            Prompt the user to enter the number of jokes to send and return the chosen number as an integer.

        run_until_loop(self, jokes: list) -> None:
            Run the joke sending loop based on the configured settings.

    Attributes:
        topic (str): The topic of jokes.
        recipient (str): The recipient's username or number.
        number_jokes (int): The number of jokes to send.
    """
    def __init__(self) -> None:
        self.topic = self.enter_topic()
        self.recipient = self.enter_recipient()
        self.number_jokes = self.get_number_jokes()
        
    def get_topic(self) -> str:
        """
        Returns the selected topic.
        """
        return self.topic
    
    @staticmethod
    def enter_topic() -> str:
        """
        Prompt the user to select a topic and return the chosen topic as a string.
        """
        valid_topics = [str(i) for i in range(1, len(config.TOPIC_INFO) + 1)]

        while True:
            print(config.TOPICS)
            topic = input("Choose a topic (number): ")
            
            if topic in valid_topics:
                return topic
            else:
                print("\nThere is no such menu item.\nPlease, try again: ")

    @staticmethod                    
    def enter_recipient() -> str:
        """
        Prompt the user to enter the recipient's username or number and return it as a string.
        """
        while True:
            recipient = input(
                "Enter the recipient's username or number:"
            )
            if recipient:
                return recipient
            else:
                print("There is empty text.\nPlease, try again:")
    
    @staticmethod
    def get_number_jokes() -> int:
        """
        Prompt the user to enter the number of jokes to send and return the chosen number as an integer.
        """
        while True:
            try:
                amount_str = input(
                    "Enter the number of jokes to send\n"
                    "(press Enter to send upon pressing): "
                )
                if not amount_str:
                    return 0  # Default to 0 if Enter is pressed
                amount = int(amount_str)
                
                if amount >= 0:
                    return amount
                else:
                    print("Please enter a non-negative number.")
                    
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    
    async def run_until_loop(self, jokes: list):
        """
        Run the joke sending loop based on the configured settings.
        """
        sender = MessageSender(config.SESSION_NAME, config.API_ID, config.API_HASH, self.recipient)
        try:
            if not self.number_jokes:
                while True:
                    input("Press the button to send the message.\n")
                    await sender.send_msg(choice(jokes))

            for i in range(self.number_jokes):
                await sender.send_msg(choice(jokes))
                print(f"The {i + 1} joke has been sent.")
                
            print("Done.")
        except KeyboardInterrupt:
            print("Goodbye.")
