import streamlit as st

st.set_page_config(
    page_title="Langchain Chatbot",
    layout='wide'
)

st.header("Chatbot Implementations with Langchain")

st.write("""
Langchain is a powerful framework designed to streamline the development of applications using Language Models (LLMs). It provides a comprehensive integration of various components, simplifying the process of assembling them to create robust applications.

Leveraging the power of Langchain, the creation of chatbots becomes effortless. Here are a few examples of chatbot implementations catering to different use cases:

- **Basic Chatbot**: Engage in interactive conversations with the LLM.
- **Context aware chatbot**: A chatbot that remembers previous conversations and provides responses accordingly.
- **Chatbot with Internet Access**: An internet-enabled chatbot capable of answering user queries about recent events.
- **Chat with your documents**: Empower the chatbot with the ability to access custom documents, enabling it to provide answers to user queries based on the referenced information.
- **Chat with Websites**: Enable the chatbot to interact with website contents.

To explore sample usage of each chatbot, please navigate to the corresponding chatbot section.
""")