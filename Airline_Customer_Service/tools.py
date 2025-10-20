from agents import function_tool, RunContextWrapper
from context import AirlineAgentContext
from openai.types.responses import ResponseTextDeltaEvent


@function_tool(name_override="faq_lookup_tool", description_override="lookup frequently ask questions")
def faq_lookup_tool(question: str) -> str:
    question_lower = question.lower()
    if any(
        keyword in question_lower
        for keyword in ["bag", "baggage", "luggage", "carry-on", "hand luggage", "hand carry"]
    ):
        return (
            "You are allowed to bring one bag on the plane. "
            "It must be under 50 pounds and 22 inches x 14 inches x 9 inches."
        ) 
    elif any(
        keyword in question_lower
        for keyword in ["seat", "seats", "seating", "plane"]
        ):
        return (
            "There are 120 seats on the plane. "
            "There are 22 business class seats and 98 economy seats. "
            "Exit rows are rows 4 and 16. "
            "Rows 5-8 are Economy Plus, with extra legroom. "
        )
    elif any(
        keyword in question_lower
        for keyword in ["wifi", "internet", "wireless", "connectivity", "network", "online"]
        ):
        return"We have free wifi on the plane, join Airline-Wifi"
    return "I'm sorry, I don't know the answer to that question." 


@function_tool
def update_seat(
    context: RunContextWrapper[AirlineAgentContext], confirmation_number: str, new_seat: str
) -> str:
    """
    Update the seat for a given confirmation number.

    Args:
        confirmation_number: The confirmation number for the flight.
        new_seat: The new seat to update to.
    """
    context.context.confirmation_number = confirmation_number
    context.context.seat_number = new_seat
    assert context.context.flight_number is not None, "flight number is required"
    return f"Updated seat to {new_seat} for confirmation number {confirmation_number}"









        
