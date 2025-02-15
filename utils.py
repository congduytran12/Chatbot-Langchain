import groq
import streamlit as st
from streamlit.logger import get_logger
from langchain_groq import ChatGroq
from langchain_ollama import ChatOllama
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings

logger = get_logger('Langchain-Chatbot')

#decorator
def enable_chat_history(func):

    # to clear chat history after swtching chatbot
    current_page = func.__qualname__
    if "current_page" not in st.session_state:
        st.session_state["current_page"] = current_page
    if st.session_state["current_page"] != current_page:
        try:
            st.cache_resource.clear()
            del st.session_state["current_page"]
            del st.session_state["messages"]
        except:
            pass

    # to show chat history on ui
    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]
    for msg in st.session_state["messages"]:
        st.chat_message(msg["role"]).write(msg["content"])

    def execute(*args, **kwargs):
        func(*args, **kwargs)
    return execute

def display_msg(msg, author):
    """Method to display message on the UI

    Args:
        msg (str): message to display
        author (str): author of the message -user/assistant
    """
    st.session_state.messages.append({"role": author, "content": msg})
    st.chat_message(author).write(msg)

def choose_custom_groq_key():
    groq_api_key = st.sidebar.text_input(
        label="Groq API Key",
        type="password",
        placeholder="gsk_...",
        key="SELECTED_GROQ_API_KEY"
    )
    
    # Groq currently supports these models
    available_models = ["mixtral-8x7b-32768", "llama-3.1-8b-instant", "llama-3.3-70b-versatile"]
    
    model = st.sidebar.selectbox(
        label="Model",
        options=available_models,
        key="SELECTED_GROQ_MODEL"
    )

    if not groq_api_key:
        st.error("Please add your Groq API key to continue.")
        st.info("Obtain your key from this link: https://console.groq.com/keys")
        st.stop()
    
    try:
        client = groq.Groq(api_key=groq_api_key)
        # Verify the API key works
        client.chat.completions.create(
            messages=[{"role": "user", "content": "test"}],
            model=model,
            max_tokens=1
        )
    except Exception as e:
        st.error(f"Authentication failed: {str(e)}")
        st.stop()

    return model, groq_api_key

def configure_llm():
    available_llms = ["llama3.1:8b","llama3.2:3b","use your groq api key"]
    llm_opt = st.sidebar.radio(
        label="LLM",
        options=available_llms,
        key="SELECTED_LLM"
        )

    if llm_opt == "llama3.1:8b":
        llm = ChatOllama(model="llama3.1")
    elif llm_opt == "llama3.2:3b":
        llm = ChatOllama(model="llama3.2")
    else:
        model, groq_api_key = choose_custom_groq_key()
        llm = ChatGroq(model_name=model, temperature=0, streaming=True, api_key=groq_api_key)
    return llm

def print_qa(cls, question, answer):
    log_str = "\nUsecase: {}\nQuestion: {}\nAnswer: {}\n" + "------"*10
    logger.info(log_str.format(cls.__name__, question, answer))

@st.cache_resource
def configure_embedding_model():
    embedding_model = FastEmbedEmbeddings(model_name="BAAI/bge-small-en-v1.5")
    return embedding_model

def sync_st_session():
    for k, v in st.session_state.items():
        st.session_state[k] = v