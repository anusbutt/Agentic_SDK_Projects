from agents_config import triage_agent
from agents import Runner
from configuration import config
import asyncio
from openai.types.responses import ResponseTextDeltaEvent


async def main():
    result = Runner.run_streamed(triage_agent, "from where i can collect my luggage?", run_config=config)
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            print(event.data.delta, end="", flush=True)

if __name__=="__main__":
    asyncio.run(main())