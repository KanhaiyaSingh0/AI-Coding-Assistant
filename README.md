# AI Coding Assistance

AI Coding Assistance is a full-stack application that helps you generate, explain, and debug code using AI. The project features a FastAPI backend and a Streamlit frontend, powered by the euriai API.

---

## 🚀 Features

- **Generate Code:** Instantly create code snippets for various languages and topics.
- **Explain Code:** Get clear explanations for programming concepts at different levels.
- **Debug Code:** Paste your code and let the AI help you find and fix issues.
- **Simple UI:** Clean, user-friendly interface built with Streamlit.

---

## 🛠️ Tech Stack

- **Backend:** FastAPI (Python)
- **Frontend:** Streamlit (Python)
- **AI Model:** euriai API
- **Other:** dotenv, requests, langchain

---

## ⚡ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/KanhaiyaSingh0/AI-Coding-Assistant.git
cd AI-Coding-Assistant
```

### 2. Set up your environment

```bash
python -m venv venv
# Activate the virtual environment:
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Add your environment variables

Create a `.env` file in the root directory and add your euriai API key:

```
EURIAI_API_KEY=your_api_key_here
```

### 4. Run the backend

```bash
uvicorn main:app --reload
```

### 5. Run the frontend

```bash
streamlit run app.py
```

---

## 📸 Screenshots

<img width="1049" height="671" alt="image" src="https://github.com/user-attachments/assets/40f96c89-8415-4bc8-a1e1-0b0acc77437a" />


---

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙋‍♂️ Author

**Kanhaiya Singh**  
[LinkedIn](https://www.linkedin.com/in/kanhaiyasingh0/)  
[GitHub](https://github.com/KanhaiyaSingh0)

---
