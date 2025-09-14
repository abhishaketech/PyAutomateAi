import os
import google.generativeai as genai

# Configure the API key.
# The SDK automatically uses the GOOGLE_API_KEY environment variable.
genai.configure()

# Initialize the Gemini 1.5 Flash model.
# Use 'gemini-1.5-flash-latest' for the latest version.
model = genai.GenerativeModel('gemini-1.5-flash-latest')

# Define your prompt.
prompt = "Explain the concept of a 'black hole' in simple terms."

# Make the request to the model.
response = model.generate_content(prompt)

# Print the model's response.
print(response.text)