from agents import function_tool
from datetime import datetime
import random

@function_tool
def generate_random_number(max: int) -> str:
    """Generate a random number up to a maximum"""
    return f"🎲 Random Number: {random.randint(0, max)}"

@function_tool
def get_current_datetime() -> str:
    """Return the current date and time"""
    return f"📅 Current time: {datetime.now()}"

@function_tool
def generate_color_palette(theme: str) -> str:
    """Generate a color palette based on a theme"""
    if theme.lower() == "pastel":
        return "🎨 Pastel Palette: #fddde6, #fef6e4, #d0f4de, #a9def9"
    elif theme.lower() == "dark":
        return "🎨 Dark Palette: #1e1e2e, #282a36, #3b4252, #2e3440"
    return "🎨 Default Palette: #ffffff, #cccccc, #999999"

@function_tool
def create_timeline(start_date: str, end_date: str) -> str:
    """Create a basic timeline between two dates"""
    return f"📋 Timeline: Start on {start_date}, end on {end_date}. Milestones will be generated."
