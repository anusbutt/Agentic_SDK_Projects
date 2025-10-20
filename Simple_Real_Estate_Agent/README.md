# 🏠 Real Estate Agent – OpenAI Agents SDK Project

An intelligent **AI Real Estate Assistant** built using the [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/).  
This project demonstrates how to build an agentic AI system with **tools**, **guardrails**, and **streaming responses**.

---

## 🚀 Overview

This AI agent acts as a **Real Estate Assistant** that:
- Lists available houses or apartments  
- Provides details about specific properties  
- Uses input guardrails to reject non–real-estate topics  
- Streams live responses and tool calls directly in the terminal  

---

## 🧠 Features

- **Tool Integration:** Automatically calls functions to fetch and display property data.  
- **Guardrails:** Prevents the agent from answering unrelated queries.  
- **Streaming Execution:** Displays tool outputs and responses as they’re generated.  
- **Safe Reasoning:** Keeps conversations on-topic and professional.  

---

## 🗂️ Folder Structure

Real_Estate_Agent/
│
├── main.py # Main entry script
├── tools.py # Tools for fetching property info
├── guardrails.py # Defines allowed topics
├── configuration.py # API and model setup
├── requirements.txt # Dependencies
└── README.md # Documentation


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/Real_Estate_Agent.git
cd Real_Estate_Agent

2️⃣ Create a Virtual Environment
uv venv
uv pip install -r requirements.txt

Or using standard Python:

python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

3️⃣ Run the Project
uv run main.py

🧱 Key Components

| Component     | Description                                 |
| ------------- | ------------------------------------------- |
| **Agent**     | Defines instructions, tools, and guardrails |
| **Runner**    | Manages streaming execution                 |
| **Tools**     | Handle property data operations             |
| **Guardrail** | Blocks irrelevant or unsafe inputs          |


🧩 Future Enhancements

Integrate real API data (e.g., Zillow, Realtor)

Add search filters (price range, location, type)

Store data in a database

Create a Streamlit or Next.js UI


🧑‍💻 Author

Developed by: Anus Butt
Tech Stack: Python, OpenAI Agents SDK
License: MIT