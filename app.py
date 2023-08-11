import streamlit as st
from langchain import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

def generate_blog_post(title):
    chat = ChatOpenAI(temperature=0.1) # Here temperature is set a little bit higher to put some variation

    template = "You are a helpful assistant that generates a blog post from the title: {title}. Please provide some content."
    system_message_prompt = SystemMessagePromptTemplate.from_template(template)
    human_template = "{title}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

    chain = LLMChain(llm=chat, prompt=chat_prompt)
    result = chain.run(title=title)
    return result # it will return string with at least 500 words. 

st.title("Blog post generator from title 📔")

title = st.text_input("Enter the title of the blog post:")
OPENAI_API_KEY = st.text_input("Enter your OpenAI API key:")
st.write("You can get your OpenAI API key from https://beta.openai.com/account/api-keys")
if OPENAI_API_KEY:
    st.write("You have entered your OpenAI API key")
    if st.button("Generate"):
        st.write("Generating the blog post...")
        os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
        result = generate_blog_post(title)
        st.write(result)
        st.balloons()
if not OPENAI_API_KEY:
    from config import OPENAI_API_KEY
    if OPENAI_API_KEY.startswith("sk-"):
        if st.button("Generate with default API key"):
            st.write("Generating the blog post...")
            result = generate_blog_post(title)
            st.write(result)
            st.balloons()
    else:
        st.write("Please enter your OpenAI API key")