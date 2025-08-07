import asyncio
from agents import Runner, InputGuardrailTripwireTriggered
from openai.types.responses import ResponseTextDeltaEvent
from agents_config import Traige_Agent
from context import UserContext
from share import config


context = UserContext(
    name="Ali",
    uid=1001,
    is_premium_user=True,
    idea="A mobile app that gamifies chores for kids",
    audience="consumer",
    product_type="mobile"
)

async def main():
    print("🧠 Console Support System\n(Type 'exit' to quit)\n")

    while True:
        user_input = input("you: ")
        if user_input.strip().lower() in {"exit", "quit"}:
            print("👋 GoodBye")
            break

        try:
            result = Runner.run_streamed(
                starting_agent = Traige_Agent,
                input = user_input,
                context = context,
                run_config = config
            )

            async for event in result.stream_events():
                if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
                    print(event.data.delta, end="", flush=True)

            print()  # 🔚 print newline after output is done

        except InputGuardrailTripwireTriggered as e:
            print(f"\n🚫 Input rejected by guardrail:\n{e.tripwire_info.reasoning}\n")

        except Exception as e:
            print(f"\n❌ Error: {e}\n")

if __name__ == "__main__":
    asyncio.run(main())

