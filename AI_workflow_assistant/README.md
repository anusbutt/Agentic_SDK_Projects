 🚀 Multi-Agent Developer Assistant

[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Chainlit](https://img.shields.io/badge/Chat%20UI-Chainlit-FF6B6B)](https://chainlit.dev/)

## 🌟 Features
- **Specialized AI Agents** (Dev, Design, PM)
- **Tool Integration** (Random numbers, color palettes, timelines)
- **Smart Triage System** routes questions to appropriate agents
- **Gemini API** powered responses
- **Chainlit Web UI**

## 🛠️ Tech Stack

```mermaid
graph LR
    A[Python] --> B[Multi-Agent Framework]
    B --> C[Gemini API]
    B --> D[Chainlit UI]
    B --> E[Custom Tools]
⚡ Quick Start
Clone repository:

bash
git clone https://github.com/yourusername/multi-agent-assistant.git
cd multi-agent-assistant
Install dependencies:

bash
pip install -r requirements.txt
Configure environment:

bash
echo "GEMINI_API_KEY=your_api_key_here" > .env
Run the app:

bash
chainlit run main.py
🤖 Agent System
Diagram
Code
graph TD
    A[Triage Agent] -->|Dev Question| B[Dev Assistant]
    A -->|Design Question| C[Design Assistant]
    A -->|PM Question| D[PM Assistant]
🛠️ Available Tools
Tool	Description	Agent
generate_random_number	Creates random numbers	Dev
get_current_datetime	Gets current time	All
generate_color_palette	Color schemes	Design
create_timeline	Project timelines	PM
📂 Project Structure
text
.
├── main.py               # Entry point
├── agents/               # Agent definitions
├── tools/                # Custom tools
├── .env                  # Configuration
└── README.md
📝 Example Queries
bash
"Generate a random number between 1-100"
"Create a pastel color palette"
"Make a 3-month project timeline"
📜 License
MIT © 2024 [Your Name]

