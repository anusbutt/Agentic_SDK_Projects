# ✅ Task Manager Agent – OpenAI Agents SDK Project

An AI-powered **Task Management Assistant** built with the [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/).  
This project demonstrates how to integrate **AI reasoning with function calling (tools)** to manage daily tasks dynamically.

---

## 🚀 Overview

The **Task Manager Agent** can:
- Add new tasks  
- List all existing tasks  
- Clear completed or all tasks  

It uses Python tools to perform these actions while the agent handles natural-language instructions from the user.

---

## 🧠 Features

- 🧩 **Tool Integration:** AI directly interacts with Python functions (`add_tasks`, `list_tasks`, `clear_task`)  
- 🤖 **Natural Language Understanding:** Add, list, or clear tasks using plain English commands  
- ⚡ **Synchronous Execution:** Uses `Runner.run_sync()` for quick, single-turn responses  
- 🗒️ **Extendable Logic:** Can easily connect to databases or APIs later  

---

## 🗂️ Folder Structure

Task_Manager_Agent/
│
├── main.py # Entry point – runs the agent
├── tools.py # Task-related tools (add, list, clear)
├── configuration.py # OpenAI API and agent setup
├── requirements.txt # Dependencies
└── README.md # Documentation


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/Task_Manager_Agent.git
cd Task_Manager_Agent

2️⃣ Create a Virtual Environment
uv venv
uv pip install -r requirements.txt


Or using Python directly:

python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

3️⃣ Run the Project
uv run main.py

💬 Example Usage

Input

i will play indoor cricket at 7pm please add this task in to my tasks for today


Output

✅ Task added: "Play indoor cricket at 7pm"


Another Example

show me my tasks


Output

📋 Current tasks:
1. Play indoor cricket at 7pm
2. Call the electrician at 5pm

🧱 Key Components
Component	Description
Agent	The task manager AI with access to tools
Runner	Executes the agent synchronously
Tools	Real Python functions for task operations
Config	Handles API setup and model configuration
🔧 Extendable Ideas

Store tasks in an SQLite or MongoDB database

Add due dates and task categories

Create a web UI using Streamlit or Next.js

Schedule reminders with cron jobs or background workers

🧑‍💻 Author

Developed by: Anus Butt
Tech Stack: Python, OpenAI Agents SDK
License: MIT