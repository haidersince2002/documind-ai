import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


# Load environment variables from the .env file
load_dotenv()

# Read the Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY is missing. "
        "Add your API key to the .env file."
    )

# Initialize the Gemini model through LangChain
model = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    temperature=0,
)

# Send a message to Gemini
response = model.invoke(
    "Explain what LangChain is in three simple bullet points."
)

# Print the AI's response
print(response.content)