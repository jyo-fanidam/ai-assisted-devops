import google.generativeai as genai
import os
from dotenv import load_dotenv


# Load environment variables from the .env file
load_dotenv()

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
- 2 staged builds
- Multi-arch support
- Exposing ports
- Environment variables
- Health check
- Using COPY instead of ADD
- Using ARG for build-time variables
- Using ENTRYPOINT instead of CMD
- Create a CI/CD pipeline
- Use a non-root user
- create a new repository
"""

def generate_dockerfile(language):
    response = model.generate_content(PROMPT.format(language=language))
    return response.text  # Access the generated text

if __name__ == "__main__":
    language = input("Enter the language: ")
    dockerfile = generate_dockerfile(language)
    print("\nGenerated Dockerfile:\n")
    print(dockerfile)
 