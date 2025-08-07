# 🤖 Multi-Agent Developer Assistant

[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Chainlit](https://img.shields.io/badge/Chat%20UI-Chainlit-FF6B6B)](https://chainlit.dev/)

<div align="center">
  <img src="https://placehold.co/600x400/1e293b/white?text=Dev+Assistant" alt="Agent System Diagram" width="400"/>
</div>

## 🌟 Features
- **Specialized AI Agents** for different development roles
- **Tool Integration** for practical functionality
- **Smart Triage System** routes questions to appropriate agents
- **Chainlit Web UI** for easy interaction
- **Gemini API** powered responses

## 🛠️ Tech Stack
- Python 3.10+
- OpenAI-compatible API (Gemini 2.0 Flash)
- Chainlit for chat interface
- Custom agent framework
- Dotenv for environment management

## ⚡ Quick Start

1. **Set up environment**:
   ```bash
   git clone https://github.com/yourusername/multi-agent-assistant.git
   cd multi-agent-assistant
   pip install -r requirements.txt
Configure API key:

bash
echo "GEMINI_API_KEY=your_api_key_here" > .env
Run the application:

bash
chainlit run main.py
🤖 Agent System
Diagram
Code
graph TD
    A[Triage Agent] -->|Dev Question| B[Dev Assistant]
    A -->|Design Question| C[Design Assistant]
    A -->|PM Question| D[PM Assistant]
    B --> E[Code Generation]
    C --> F[Color Palettes]
    D --> G[Timelines]
🛠️ Available Tools
Tool	Description	Agent
generate_random_number	Creates random numbers	Dev
get_current_datetime	Gets current time/date	All
generate_color_palette	Generates color schemes	Design
create_timeline	Makes project timelines	PM
📜 Environment Variables
env
GEMINI_API_KEY=your_api_key_here
📂 Project Structure
text
.
├── main.py               # Entry point with agent definitions
├── agents/               # Core agent framework
├── tools/                # Custom tool implementations
├── .env                  # Environment configuration
└── README.md
📝 Example Queries
"Generate a random number between 1-100" (Dev)

"Create a pastel color palette" (Design)

"Make a 3-month project timeline" (PM)

📜 License
MIT © 2024 [Anus Butt] | https://img.shields.io/twitter/url/https/twitter.com/yourhandle.svg?style=social&label=Follow%2520%2540yourhandle

