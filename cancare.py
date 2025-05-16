import os

# Define project structure
structure = {
    "CanCare": {
        "frontend": {
            "README.md": "# Frontend - CanCare\nFlutter or React Native code goes here.\n",
            "app.py": "# Sample placeholder for front-end logic (e.g., Flask/React entry point)\nprint('Frontend running...')\n"
        },
        "backend": {
            "README.md": "# Backend - CanCare\nFastAPI or Node.js server code goes here.\n",
            "main.py": "# Sample FastAPI placeholder\nfrom fastapi import FastAPI\napp = FastAPI()\n\n@app.get('/')\ndef read_root():\n    return {'message': 'Backend running...'}\n"
        },
        "ai-engine": {
            "README.md": "# AI Engine - CanCare\nGemini integration and NLP modules.\n",
            "gemini_integration.py": "# Placeholder for Gemini API integration\ndef ask_gemini(question):\n    return f'Response to: {question}'\n"
        },
        "docs": {
            "README.md": "# Documentation - CanCare\nWireframes, mockups, diagrams.\n"
        },
        "README.md": "# CanCare - AI-Powered Bedside Companion for Cancer Patients\nThis is the main repository for the CanCare project.\n"
    }
}

# Function to create files and folders
def create_structure(base_path, structure_dict):
    for name, content in structure_dict.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            with open(path, "w") as f:
                f.write(content)

# Set base directory
base_path = "/mnt/data"

# Create project structure
create_structure(base_path, structure)

# Return path for user to download
"/mnt/data/CanCare"