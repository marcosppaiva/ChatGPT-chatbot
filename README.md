# Chatbot with ChatGPT and Gradio

This application uses the openai API to create a chatbot and
the gradio framework to create a web interface.


## 1. Project Structure
```bash
chatbot/
├── .env
├── chatbot/
│   ├── __init__.py
│   └── src/
│       ├── __init__.py
│       ├── app.py
│       └── chatbot.py
├── README.md
└── requirements.txt
```

## 2. How to use

2.1. Download the project 
    
    $ git clone https://github.com/marcosppaiva/ChatGPT-chatbot.git
    $ cd ChatGPT-chatbot

2.2. Create a .env file with your openai key

    # .env file 
    $ OPENAI_API_KEY = YOUR_KEY

2.3. Install dependencies
    
    # if you prefer to create a venv
    $ pip install -r requirements.txt

2.4. Launch the application 

    $ python  chatbot/src/app.py

## 3. Application

![NSSM_IO](/assets/images/run_app.png)



## 4. References

* [OpenAI Documentation](https://platform.openai.com/docs/)
* [Gradio](https://gradio.app/)
