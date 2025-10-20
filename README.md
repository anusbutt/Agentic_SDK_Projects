🧠 Agentic AI Projects

Welcome to the Agentic AI Projects Repository — a curated collection of practical, real-world projects built using the OpenAI Agents SDK.
Each project demonstrates a different use case for multi-agent systems, tool integration, and guardrails using Python.

🚀 Overview

This repository contains several small-to-medium scale projects showcasing how autonomous and cooperative AI agents can work together across industries — from customer service to task management.

All projects are written in Python and use:

🧩 OpenAI Agents SDK

⚙️ Async I/O (asyncio)

🧰 Custom Tools and Guardrails

🧑‍💻 OOP and modular architecture

📁 Projects Included
Project	Description	Features
🧠 Smart Support System	A triage-based customer support agent that routes queries to technical or billing specialists based on context.	Multi-agent handoffs, eligibility checks, context-based routing
🏠 Simple Real Estate Agent	An AI assistant that lists or fetches property details using custom tools and input guardrails.	Tool-calling, streaming responses, guardrail filtering
🗓️ To-Do Task Agent	A task management agent that can add, list, and clear your tasks using tool-based functions.	Tool integration, simple user-agent interaction
💬 Customer Support Agent	A multi-agent orchestrator that routes between order, billing, technical, and FAQ agents.	Input/output guardrails, dynamic handoffs
✈️ Airline Customer Service	(Optional) An airline support demo handling flight status, refund, and rescheduling queries.	Tool-based support, structured responses
🚀 Launch Mate (Main)	A utility module for managing and launching projects or workflows.	Project orchestrator logic
⚡ Tech Stack

Language: Python 3.11+

Framework: OpenAI Agents SDK

Environment: Async/Await

Version Control: Git & GitHub

Configuration: .env, uv, pyproject.toml

🧩 Key Concepts Demonstrated

🤖 Multi-Agent Orchestration — multiple agents collaborating on specialized tasks

🧠 Context Passing — sharing user context between agents

🔧 Tool Integration — connecting agents to external or internal Python tools

🧍 Guardrails — controlling agent input/output behavior for safety and accuracy

🪄 Dynamic Instructions — runtime customization of agent prompts

🧰 Setup Instructions

Clone the Repository

git clone https://github.com/<your-username>/Agentic-AI-Projects.git
cd Agentic-AI-Projects


Create Virtual Environment

python -m venv .venv
.venv\Scripts\activate  # (Windows)


Install Dependencies

pip install -r requirements.txt


Run Any Project

uv run Smart_Support_System/main.py

🧑‍💻 Author

Anus Butt
AI Developer | Agentic AI & Python OOP Enthusiast
📍 Pakistan

🌟 Contributing

Pull requests and forks are welcome!
If you’d like to add your own Agentic AI project, follow the same directory structure and naming convention.

🪪 License

This project is released under the MIT License — feel free to use and modify it for educational or personal purposes.