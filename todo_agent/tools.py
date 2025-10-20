from agents import function_tool
from pydantic import BaseModel
from typing import List


tasks = []

class Task(BaseModel):
    title: str

class TaskList(BaseModel):
    tasks: List[str]

@function_tool
def add_tasks(task: Task) -> str:
    """add a new task to todo list"""
    task.append(task.title)
    return "task added!"

@function_tool
def list_tasks() -> TaskList:
    """list all current tasks"""
    if not tasks:
        return TaskList(task=["No Tasks Yet!"])
    return TaskList(tasks=tasks)

@function_tool
def clear_task():
    """clear all tasks"""
    tasks.clear()
    return "All Tasks Cleared!"

