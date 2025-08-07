from agents import Runner, Agent, OpenAIChatCompletionsModel, set_tracing_disabled
from openai import AsyncOpenAI
from dotenv import load_dotenv
from tools import get_current_datetime, generate_random_number, generate_color_palette, create_timeline
from agents.run import RunConfig
import chainlit as cl
import os

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

external_client = AsyncOpenAI(
    api_key = gemini_api_key,
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash",
    openai_client = external_client,
)

config = RunConfig(
    model = model,
    model_provider = external_client,
    tracing_disabled = True
)

dev_agent: Agent = Agent(
    name="Dev Assistant",
    instructions="You are a dev assistant. Use tools to generate code, dates, or numbers.",
    tools = [generate_random_number, get_current_datetime]
)

design_agent: Agent = Agent(
    name="Design Assistant",
    instructions = "You are a design assistant. Use tools to generate color palettes or get time.",
    tools = [generate_color_palette, get_current_datetime]
)

pm_agent: Agent = Agent(
    name="Pm Assistant",
    instructions="You are a PM assistant. Use tools to create timelines or get the time.",
    tools=[create_timeline, get_current_datetime]
)


triage_agent: Agent = Agent(
    name="Triage Agent",
    instructions= ("You are a triage agent. Route code or dev questions to Dev Assistant, "
        "design-related queries to Design Assistant, and project management questions to PM Assistant. "
        "If unsure, say: '❌ I can only help with dev, design, or project tasks.'"
    ),
    handoffs = [design_agent, dev_agent, pm_agent]
)

@cl.on_message
async def main(message: cl.Message):
    try:
        result = await Runner.run(triage_agent, message.content, run_config=config)
        await cl.Message(content=result.final_output).send()
    except Exception as e:
        await cl.Message(content=f"❌ Error: {str(e)}").send()