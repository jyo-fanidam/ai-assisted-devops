import google.generativeai as genai
import os

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# configure the gemini model
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))    
model = genai.GenerativeModel('gemini-1.5-pro')

PROMPT = """
Generate an ideal Dockerfile for {language} with best practices. Do not provide any description
Include:
- Base image
- Installing dependencies
- Setting working directory
- Adding source code
- Running the application
"""
def generate_dockerfile(language):
    response = model.generate_content(PROMPT.format(language=language))
    return response.text

if __name__ == "__main__":
    language = input("Enter the language: ")    
    try:
        dockerfile = generate_dockerfile(language)
        print(dockerfile)
    except Exception as e:
        print(f"An error occurred: {e}")