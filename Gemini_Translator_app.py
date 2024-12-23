import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Set environment variables (Make sure to use .env for security in production)
LANGCHAIN_API_KEY = st.secrets["LANGCHAIN_API_KEY"]
LANGCHAIN_PROJECT = st.secrets["LANGCHAIN_PROJECT"]
LANGCHAIN_ENDPOINT = st.secrets["LANGCHAIN_ENDPOINT"]
LANGCHAIN_TRACING_V2 = st.secrets["LANGCHAIN_TRACING_V2"]
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]

# Streamlit app title
import streamlit as st

st.write('<h1 style="text-align: center; color: blue;">Gemini Translator</h1>', unsafe_allow_html=True)
#st.title(":blue[Language Translator]")

# User inputs for language and text

text = st.text_input("Enter text to translate:")
lang = st.text_input("Enter language code (e.g., 'es' for Spanish, 'fr' for French):")

# Button to trigger translation
button = st.button("Translate")

# Check if both inputs are provided
if lang != "" and text != "":
    if button:
        # Initialize the chatbot
        chatbot = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
        
        # Define the message template
        template = """Translate the following into {language} 
        and translated language should be in {language} and 
        Romanized Pronunciation both also. 
        both sholuld in a single line for example 'எப்படி இருக்கீங்க? (eppati irukkiṅka?)') and 
        don't explain. if {language} is not a correct language or language code then give an error 'Warning: 
        Please Type Correct Language to Translate' :"""
        messages = ChatPromptTemplate.from_messages([
    ("system",template),
    ("user","{text}")
])
        
        # Define output parser
        parser = StrOutputParser()
        
        # Create the translation chain
        chains = messages | chatbot | parser
        
        # Invoke the chain with user inputs
        response = chains.invoke({"language": lang, "text": text})
        if "Warning" not in response:
            # Display the result
            st.write("**Translation:**", response)
        else:
            st.warning("Please Type Correct Language to Translate")
else:
    st.warning("Please enter both language code and text.")
