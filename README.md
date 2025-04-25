# 🧠 Legal Research AI Advisor

### Welcome to the Legal Research AI Advisor!  
This is a simple and powerful tool that lets you ask legal questions in plain English and get helpful, AI-generated answers — fast.

Whether you're a student, lawyer, or just someone curious about law, this tool can assist with legal research and case summaries using smart AI behind the scenes.

---

## ✨ What It Does

- Ask your legal questions in natural language  
- Get summaries of related case laws or concepts  
- Upload your own legal documents (PDFs or Word files) for analysis  
- Get answers powered by large language models (Groq or OpenAI)  
- Clean, user-friendly interface built with Streamlit  

---

## 🔧 How to Set It Up

### 1. Clone the project

First, clone the repository to your local machine using the following command:

```bash
git clone https://github.com/Pa2608/AI-legal-advisor.git
cd AI-legal-advisor
```

### 2. Install the required Python libraries
After cloning the project, install the necessary Python libraries by running:

```bash
pip install -r requirements.txt
```

### 3. Add your API key
You need an API key to access Groq. Open the config.py file and paste your API key like this:

```bash
GROQ_API_KEY = "your_actual_api_key"
```

### ▶️ How to Run
Once everything is set up, start the app by running the following command:

```bash
streamlit run app.py
```

This will launch a browser window where you can start interacting with the tool and asking legal questions!

### 🗂️ Project Overview
Here’s the structure of the project:

<pre> ``` 
  📁 legal-research-ai-advisor/ 
  └── app.py → Main app logic 
  └── config.py → API key setup 
  └── utils/ → PDF/docx parsing, etc. 
  └── data/ → Sample legal documents (optional) 
  └── requirements.txt → Python dependencies 
  └── README.md → This file ``` 
</pre>

### 📄 License
This project is under the MIT License — free to use and modify.
## Made with ❤️ by Parth Varecha
