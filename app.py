import streamlit as st
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from langchain.chat_models import ChatOpenAI

OPENAI_API_KEY = "<your-key>"

llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, temperature=0.7, model="ft:gpt-3.5-turbo-0613:personal::7t7cBpHq")

def query_llm_model(prompt_text):
    prompt = PromptTemplate(
         input_variables=["prompt_text"],
         template="""
                You are a helpful Assistant who can write function plugins in Sinequa. {prompt_text}"""
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run({
        'prompt_text': prompt_text
    })

def app():
    st.title("Sinequa Function Plugin Developer")
    
    user_input = st.text_area("Enter your prompt:")
    if st.button('Submit'):
        result = query_llm_model(user_input)
        
        # Assuming 'result' contains the C# code, wrap it in markdown code block with C# formatting
        formatted_code = f"```csharp\n{result}\n```"
        st.markdown(formatted_code, unsafe_allow_html=True)

if __name__ == '__main__':
    app()
