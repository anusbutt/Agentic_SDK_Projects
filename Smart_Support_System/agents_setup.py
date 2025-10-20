from agents import Agent, handoff, RunContextWrapper
from context import UserInfo


def check_user_eligibility(ctx: RunContextWrapper[UserInfo]):
    """runs before handing off to a spacialist agent"""
    name = ctx.context.name
    age = ctx.context.age
    plan = ctx.context.plan

    if age < 18:
        return f"Sorry. users under 18 can't access technical support"
    if plan.lower() == "free":
        return f"Hi {name}. Please upgrade to premium for prior support" 
    return f"Welcome {name}! you are eligible for handoff"


technical_agent: Agent = Agent(
    name="technical agent",
    instructions =(
        "You are a professional technical support specialist. "
        "Diagnose system or app issues and provide clear 3-step fixes."
    )
)

billing_agent: Agent = Agent(
    name="billing agent",
    instructions=(
        "You are a friendly billing representative. Handle refunds, "
        "subscriptions, and account payment inquiries concisely."
    )
)

def triage_agent_instruction(context: RunContextWrapper[UserInfo], agent: Agent) -> str:
    """Dynamic instructions injected at runtime."""
    return f"""
You are the Triage Agent.
User details:
- Name: {context.context.name}
- Age: {context.context.age}
- Plan: {context.context.plan}

Your role:
1. Determine if the query is technical or billing-related.
2. If technical → hand off to Technical Agent.
3. If billing → hand off to Billing Agent.
4. If unrelated → answer yourself briefly.
Always stay polite and limit answers to 5 lines.
"""

Triage_agent: Agent[UserInfo] = Agent(
    name="triage_agent",
    instructions=triage_agent_instruction,
    handoffs = [
        billing_agent,
        handoff(
            agent=technical_agent,
            on_handoff=check_user_eligibility,
        )
    ]
)