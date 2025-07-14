#  CLI Chatbot with Gemini Pro (Gen AI Chatbot)

A simple yet powerful command-line chatbot powered by Google’s Gemini Pro API. It supports contextual memory stored in JSON, allows loading external files as context, and is ideal for testing LLMs from the terminal.

---

##  Tech Stack

 LLM: Gemini 1.5 Flash (models/gemini-1.5-flash-latest)

 Memory: JSON-based long-term memory

 File Context: Supports .txt, .pdf, .docx

 Secrets: Uses .env to securely store your API key

 Language: Python 3.10+

---

##  Features

 Chat with Gemini directly in the terminal

 Maintains memory across sessions (memory.json)

 Load and chat with documents using upload [file_path]

 Fast & lightweight with Gemini Flash model

---

 API Key Setup
Create a .env file in the project root:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

---

 Memory Example (memory.json)
```json
[
  {
    "user": "her is the assignment",
    "bot": "Okay, I see the assignment description. To help you, I need you to choose ONE of the five case studies..."
  },
  {
    "user": "make an erd for this assignment",
    "bot": "You did not select a case study. I need you to choose one of the five case studies (1-5)..."
  },
  {
    "user": "2",
    "bot": "Okay, you've chosen Case Study 2: Hospital Patient Record System. Here's a conceptual ERD for this system..."
  }
]
```
All chat history is automatically saved and loaded across sessions.

---

##  How to Run

1. Install dependencies
```bash
pip install -r requirements.txt
```
2. Create .env file
```env
GOOGLE_API_KEY = "your_actual_key"
```
3. Run the chatbot
```bash
python main.py
```

---

##  Uploading Files (Document Context)

You can load a .txt, .pdf, or .docx file into the chatbot to give it extra context to answer your questions more accurately.

###  How to Upload a File

Type the following in the chatbot interface:

```bash
upload C:\Users\Lenovo\Downloads\Final_Database_Assignment.pdf
```
If the file exists and is supported, the chatbot will respond with:

```text
📄 File loaded into context successfully.
```
From now on, your questions will be answered with that document in mind, until you upload another or restart the session.


