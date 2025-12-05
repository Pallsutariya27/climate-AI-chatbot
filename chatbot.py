import google.generativeai as genai
import pandas as pd
import os

# Configure Gemini API key from environment variable
genai.configure(api_key=os.getenv("API_KEY"))

def ask_gemini(prompt):
    model = genai.GenerativeModel('models/gemini-2.5-pro')
    response = model.generate_content(prompt)
    return response.text

climate_data = {
    'Year': [2000, 2005, 2010, 2015, 2020, 2023],
    'CO2 Levels (ppm)': [370, 380, 390, 400, 415, 420],
    'Avg Temp (°C)': [14.3, 14.5, 14.7, 14.9, 15.1, 15.3],
    'Sea Level Rise (mm)': [20, 30, 45, 60, 80, 95],
}
df = pd.DataFrame(climate_data)

def climate_chatbot(user_query):
    context = f"""
    You are a climate science expert. Use the following data to answer the question simply and clearly:

    {df.to_string(index=False)}

    Question: {user_query}

    Answer:
    """
    return ask_gemini(context)
