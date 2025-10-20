from agents import Agent, Runner, InputGuardrailTripwireTriggered, OutputGuardrailTripwireTriggered
from openai.types.responses import ResponseTextDeltaEvent
import asyncio
from configuration import config
from input_guardrails import customer_guardrail
from output_guardrails import customer_support_guardrail
from agents_setup import order_agent, billing_agent, tech_agent, faq_agent

orchestrator_agent=Agent(
    name="Orchestrator Agent",
    instructions=(
        "You are the main support assistant. "
        "When a query belongs to a specialized domain, call the correct agent directly, "
        "wait for its response, and return ONLY that final response to the user. "
        "Never just say you are transferring."
    ),
    handoffs=[order_agent, billing_agent, tech_agent, faq_agent],
    input_guardrails=[customer_guardrail],
    output_guardrails=[customer_support_guardrail]
)

async def main():
    while True:
        try:
            user_input=input("ask: ")
            result=Runner.run_streamed(orchestrator_agent, user_input, run_config=config)
            async for event in result.stream_events():
                if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent) :
                    print(event.data.delta, end="", flush=True)
        except InputGuardrailTripwireTriggered as e:
            print(f"Error: {e}")
        except OutputGuardrailTripwireTriggered as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
