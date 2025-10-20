from configuration import config 
from agents import Runner
from context import UserInfo
from agents_setup import Triage_agent
import asyncio

print("Hello from smart-support-system!")

async def main():
    context = UserInfo(name="Anus", age=17, plan="free")

    user_message = input("ask your query here: ")
    result = await Runner.run(
        Triage_agent, 
        user_message, 
        context=context, 
        run_config=config
        )

    print("/n===Final Response=== ")
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
