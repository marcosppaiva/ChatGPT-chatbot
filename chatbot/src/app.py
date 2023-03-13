"""
    Developed by Marcos Pereira
    email: marcosppaivap@gmail.com
"""
import gradio as gr

from chatbot import ChatBot

chat = ChatBot()


def send_message(message):
    """
    Sends a message to the chatbot and returns the chatbot's response.

    Args:
        message (str): The message to be sent to the chatbot.

    Returns:
        List[Tuple[str, str]]: A list of tuples representing the chatbot's response, where each tuple contains two strings representing a message from the user and the chatbot's corresponding response.
    """
    reply = chat.send_message(message)

    response = [(reply[i]["content"], reply[i+1]["content"])
                for i in range(0, len(reply)-1, 2)]

    return response


with gr.Blocks() as demo:
    chatbot = gr.Chatbot()

    with gr.Row():
        txt = gr.Textbox(show_label=False, placeholder="Enter text and press enter").style(
            container=False)

        txt.submit(send_message, txt, chatbot)

        # No function, no input to that function, submit action to textbox is a js function that returns empty string, so it clears immediately.
        txt.submit(None, None, txt, _js="() => {''}")

demo.launch()
