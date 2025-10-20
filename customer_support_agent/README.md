# 🤖 AI Customer Support System – Multi-Agent Architecture (OpenAI Agents SDK)

An intelligent, **multi-agent customer support system** built with the [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/).  
This project demonstrates how to orchestrate multiple specialized AI agents — each responsible for different domains of customer support — under a single unified assistant.

---

## 🚀 Overview

The system is composed of several specialized agents that handle specific categories of user issues:

| Agent | Responsibility |
|--------|----------------|
| 🛒 **Order Agent** | Handles order tracking, return policy queries, and order-related FAQs |
| 💳 **Billing Agent** | Manages payments, refunds, and billing disputes |
| 🧰 **Technical Agent** | Troubleshoots technical issues and escalates if necessary |
| 📚 **FAQ Agent** | Answers general company FAQs |
| 🎯 **Orchestrator Agent** | Routes queries intelligently to the right specialized agent |

Each agent uses **tools**, **guardrails**, and **handoffs** to process user requests safely and efficiently.

---

## 🧠 Features

- **Multi-Agent Handoff System:** Automatic routing between Order, Billing, Tech, and FAQ agents  
- **Tool-Driven Actions:** Executes Python functions (`check_order_status`, `process_refund`, etc.) to simulate backend operations  
- **Guardrails for Safety:** Ensures inputs and outputs stay within customer support boundaries  
- **Streaming Responses:** Live message streaming as the AI generates its response  
- **Error Handling:** Graceful handling of invalid queries using guardrail tripwires  

---

## 🗂️ Folder Structure

AI_Customer_Support/
│
├── main.py # Entry point (orchestrator loop)
├── agents_setup.py # Defines all sub-agents and handoffs
├── tool.py # Support-related tools
├── configuration.py # API and model settings
├── input_guardrails.py # Validates allowed input topics
├── output_guardrails.py # Controls safe responses
├── requirements.txt # Dependencies
└── README.md # Documentation

yaml
Copy code

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/AI_Customer_Support.git
cd AI_Customer_Support
2️⃣ Create a Virtual Environment
bash
Copy code
uv venv
uv pip install -r requirements.txt
Or using Python directly:

bash
Copy code
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
3️⃣ Run the Project
bash
Copy code
uv run main.py
💬 Example Interaction
User Input:

vbnet
Copy code
ask: what's the status of my order ID #ORD-1205?
Output:

bash
Copy code
🔍 Checking order status...
✅ Your order #ORD-1205 has been shipped and will arrive within 3 days.
User Input:

perl
Copy code
ask: I want a refund for my last payment.
Output:

sql
Copy code
💳 Processing refund...
✅ Refund for your last payment has been initiated. You’ll receive it within 3–5 business days.
User Input:

perl
Copy code
ask: my app keeps crashing when I open it
Output:

sql
Copy code
⚙️ Technical issue detected. Creating a support ticket...
🎟️ Ticket created successfully! Our technical team will reach out within 24 hours.
🧩 Key Components
Component	Description
Agents	Define expertise and tool access
Tools	Handle backend-like logic (orders, refunds, tickets)
Guardrails	Enforce safe input/output boundaries
Orchestrator	Directs messages to the right agent dynamically
Runner	Executes agents and streams responses in real-time

⚠️ Guardrail Behavior
If a user asks something outside the scope (e.g., “Who is the president?”),
the system immediately rejects it with:

sql
Copy code
⚠️ I can only assist with customer support–related questions.
🔮 Future Enhancements
Integrate real e-commerce APIs for live order and refund data

Add authentication per customer session

Build a web dashboard using Streamlit or Next.js

Add analytics for tracking agent performance

🧑‍💻 Author
Developed by: Anus Butt
Tech Stack: Python, OpenAI Agents SDK
License: MIT

Copy code
