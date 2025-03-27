# Dockerfile Generator

This project provides tools to generate Dockerfiles for various programming languages using AI models. It includes two implementations: one using the **Ollama LLM** and another using the **Gemini hosted LLM**.

## Project Structure

- **Local LLM (Ollama):** Generates Dockerfiles using the Ollama LLM model.
- **Hosted LLM (Gemini):** Generates Dockerfiles using the Gemini hosted LLM model.
- **Customizable:** Specify the programming language to generate Dockerfiles tailored to your needs.
- **Best Practices:** Dockerfiles are generated with best practices, including:
  - Base image selection
  - Dependency installation
  - Working directory setup
  - Source code addition
  - Application execution

## Prerequisites

### Installing Ollama

#### Download and Install Ollama

- **For Linux:**
  ```bash
  curl -fsSL https://ollama.com/install.sh | sh
  ```

- **For MacOS:**
  ```bash
  brew install ollama
  ```

#### Start Ollama Service
```bash
ollama serve
```

#### Pull Llama3 Model
```bash
ollama pull llama3.2:1b
```

## Setup

### Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Linux/MacOS
# or
.\venv\Scripts\activate  # On Windows
```

### Install Dependencies
```bash
pip3 install -r requirements.txt
```

### Run the Application
```bash
python3 generate_dockerfile.py
```

## How It Works

1. The script takes a programming language as input (e.g., Python, Node.js, Java).
2. Connects to the Ollama API running locally.
3. Generates an optimized Dockerfile with best practices for the specified language.
4. Returns the Dockerfile content with explanatory comments.

## Example Usage

```bash
python3 generate_dockerfile.py
```

- **Input:** Enter programming language (e.g., `python`).
- **Output:** The generated Dockerfile will be displayed.

## Troubleshooting

- Ensure the Ollama service is running before executing the script.
- Verify the correct model is downloaded.
- Adapt best practices for other programming languages as needed.