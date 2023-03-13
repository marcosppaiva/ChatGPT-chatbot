"""
    Developed by Marcos Pereira
    email: marcosppaivap@gmail.com
"""
import os
from typing import List

import openai
from dotenv import load_dotenv


class ChatBot():
    """Class responsible for representing a conversation bot."""

    def __init__(self) -> None:
        """Constructor method for the ChatBot class."""
        self.message_history = []
        load_dotenv()
        openai.api_key = os.getenv("OPENAI_API_KEY", "")

    def send_message(self, message: str) -> List:
        """_summary_

        Args:
            message (str): _description_

        Returns:
            List: _description_
        """
        self.message_history.append({"role": "user", "content": message})
        print(self.message_history)

        # TODO: adicionar modelo como parametro.
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=self.message_history)

        reply = completion.choices[0].message.content

        self.message_history.append({"role": "assistant", "content": reply})

        print("Message_History", self.message_history)

        return self.message_history
