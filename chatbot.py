import os
import json
from dotenv import load_dotenv
import google.generativeai as genai
from PyPDF2 import PdfReader
from docx import Document

load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("models/gemini-1.5-flash-latest")

MEMORY_FILE = "memory.json"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return []

def save_memory(history):
    with open(MEMORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

def format_memory(memory):
    return "\n".join([f"User: {m['user']}\nBot: {m['bot']}" for m in memory])

def read_text_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def read_pdf_file(path):
    reader = PdfReader(path)
    return "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])

def read_docx_file(path):
    doc = Document(path)
    return "\n".join([para.text for para in doc.paragraphs if para.text.strip()])

# Load file content as context
def load_file_context(path):
    if path.endswith(".txt"):
        return read_text_file(path)
    elif path.endswith(".pdf"):
        return read_pdf_file(path)
    elif path.endswith(".docx"):
        return read_docx_file(path)
    else:
        print("❌ Unsupported file type. Use .txt, .pdf, or .docx")
        return ""

def main():
    print("🤖 Gemini CLI Assistant with Memory & File Context")
    print("Type 'exit' to quit, or 'upload [file_path]' to load a document.\n")

    history = load_memory()
    file_context = ""

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            print("👋 Goodbye!")
            break

        elif user_input.lower().startswith("upload "):
            path = user_input.split(" ", 1)[1]
            if os.path.exists(path):
                file_context = load_file_context(path)
                print("📄 File loaded into context successfully.\n")
            else:
                print("❌ File not found.\n")
            continue

        memory_text = format_memory(history)
        full_prompt = f"{file_context}\n\n{memory_text}\nUser: {user_input}\nBot:"

        try:
            response = model.generate_content(full_prompt)
            bot_reply = response.text.strip()
        except Exception as e:
            bot_reply = f"[Error] {e}"

        print(f"Gemini: {bot_reply}\n")

        history.append({"user": user_input, "bot": bot_reply})
        save_memory(history)

if __name__ == "__main__":
    main()
