from agents import Agent, Runner
from configuration import config
from tools import add_tasks, clear_task, list_tasks

task_agent: Agent = Agent(
    name="Task Agent",
    instructions="you are a task manager agent. you add list and clear tasks using given tools.",
    tools=[clear_task, add_tasks, list_tasks]
)
result = Runner.run_sync(task_agent, "i will play indoor cricket at 7pm please add this task in to my tasks for today", run_config=config)
print(result.final_output)