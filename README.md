# 🌐 Gemini Translator - AI-Powered Language Translation App
Gemini Translator is an AI-powered language translation app built using Streamlit and LangChain. It leverages Google's Generative AI (Gemini model) to translate text into various languages, providing both the translated text and its Romanized pronunciation in a single line. This makes it a perfect tool for users who want to quickly understand and pronounce phrases in different languages.

🛠️ Features
Instant Translation: Translate text to any language using the power of Google's Generative AI (Gemini model).
Romanized Pronunciation: Get the Romanized pronunciation of the translated text for easier reading and pronunciation.
User-Friendly Interface: Built with Streamlit, providing a simple and intuitive user experience.
Supports Multiple Languages: Translate into various languages by specifying the language code (e.g., 'es' for Spanish, 'fr' for French).
🚀 Getting Started
Follow these steps to set up and run the Gemini Translator on your local machine.

Prerequisites
Python 3.8 or higher
Streamlit
LangChain library
API keys for LangChain and Google Generative AI
Installation
Clone the Repository:

bash
Copy code
git clone https://github.com/yourusername/gemini-translator.git
cd gemini-translator
Install Dependencies:

bash
Copy code
pip install streamlit langchain-google-genai langchain-core
Set Up Environment Variables:

Create a .env file in the project root directory and add your API keys:

bash
Copy code
LANGCHAIN_API_KEY=your_langchain_api_key
LANGCHAIN_PROJECT=Language_Translator_App
LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
LANGCHAIN_TRACING_V2=true
GOOGLE_API_KEY=your_google_api_key
Running the App
Start the Streamlit app using the following command:

bash
Copy code
streamlit run translator_app.py
Usage
Enter the text you want to translate.
Specify the language code for the target language (e.g., 'es' for Spanish, 'fr' for French).
Click the Translate button.
The app will display the translated text along with its Romanized pronunciation.
Example
If you enter:

Text: "How are you?"
Language Code: "ta" (for Tamil)
Output:

makefile
Copy code
Translation: எப்படி இருக்கீங்க? (eppati irukkiṅka?)
🧩 Code Structure
translator_app.py: Main Streamlit application script.
.env: Environment variables for API keys (not included in the repository).
requirements.txt: Python dependencies for the project.
🔧 Dependencies
Streamlit
LangChain
Google Generative AI
Install all dependencies using:

bash
Copy code
pip install -r requirements.txt
💡 How It Works
The user inputs text and selects the target language code.
The app initializes a chatbot instance using the Gemini model (gemini-1.5-flash).
It creates a message prompt requesting translation with Romanized pronunciation.
The chatbot processes the input and returns the translation in the specified format.
The result is displayed to the user.
