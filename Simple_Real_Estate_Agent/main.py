import asyncio
from agents import Agent, Runner, InputGuardrailTripwireTriggered, ItemHelpers
from openai.types.responses import ResponseTextDeltaEvent, ResponseCompletedEvent
from tools import list_properties, get_property
from configuration import config
from guardrails import real_estate_guardrail

agent: Agent = Agent(
    name="Real Estate Agent",
    instructions=(
        "You are a simple real estate assistant. "
        "When users ask about available houses or apartments, use the tools provided."
    ),
    tools=[list_properties, get_property],
    input_guardrails=[real_estate_guardrail]
)

async def main():
    print("🏠 Real Estate Agent is ready! (Type 'exit' to quit)\n")
    
    while True:
        try:
            user_msg = input("Ask your query here: ").strip()
            if user_msg.lower() in ["exit", "quit"]:
                print("\n👋 Exiting Real Estate Agent. Goodbye!")
                break

            print("\n🤖 Thinking...\n")
            result = Runner.run_streamed(agent, user_msg, run_config=config)

            async for event in result.stream_events():
                if event.type == "raw_response_event":
                    continue
                elif event.type == "agent_updated_stream_event":
                    print(f"Agent updated: {event.new_agent.name}")
                    continue
                elif event.type == "run_item_stream_event":
                    if event.item.type == "tool_call_item":
                        print("-- Tool was called")
                    elif event.item.type == "tool_call_output_item":
                        print(f"-- Tool output: {event.item.output}")
                    elif event.item.type == "message_output_item":
                        print(f"-- Message output:\n {ItemHelpers.text_message_output(event.item)}")
                    else:
                        pass  

            print("=== Run complete ===")


        except InputGuardrailTripwireTriggered:
            print("⚠️ I am not allowed to answer any question except about real estate.")
        except KeyboardInterrupt:
            print("\n👋 Gracefully exiting...")
            break

if __name__ == "__main__":
    asyncio.run(main())
