# Chatbot Simple Implementations With Langchain And Streamlit

Langchain is a powerful library designed to streamline the development of applications using Large Language Models (LLMs). \
It provides a comprehensive integration of various components, simplifying the process of combining them to create powerful applications.

## Sample chatbot features
Here are some features of chatbot implementations using Langchain and Streamlit:
-  **Basic Chatbot** \
  Engage in interactive conversations with the LLM.

- **Context aware chatbot** \
  A chatbot that remembers previous conversations and provides responses accordingly.

-  **Chatbot with Internet Access** \
  An internet-enabled chatbot capable of answering user queries about recent events.

-  **Chat with your documents** \
  Empower the chatbot with the ability to access custom documents, enabling it to provide answers to user queries based on the referenced information.


-  **Chat with Websites** \
  Enable the chatbot to interact with website contents.

## How to setup the environment

### Install the dependencies
```pip install -r requirements.txt```

### Install Ollama models
```ollama pull llama3.1 && ollama pull llama3.2```

### Run the chatbot
Run the command ```streamlit run app.py``` and go to http://localhost:8501 to display the chatbot