from pydantic import BaseModel
from configuration import config
from agents import (
    Agent,
    GuardrailFunctionOutput,
    InputGuardrailTripwireTriggered,
    RunContextWrapper,
    Runner,
    TResponseInputItem,
    input_guardrail,
)

class customer_support_guardrail(BaseModel):
    is_customer_support_query: bool
    reasoning: str

guardrail_agent=Agent(
    name="guardrail check",
    instructions="""You are a guardrail agent that checks if the user's query is a customer support query. 
    If the user is just greeting (hi, hello, etc.), treat it as a valid customer support context.""",  
    output_type=customer_support_guardrail,
)

@input_guardrail
async def customer_guardrail(
    ctx: RunContextWrapper[None], agent: Agent, input: str | list[TResponseInputItem]
    ) -> GuardrailFunctionOutput:
    result=await Runner.run(guardrail_agent, input, context=ctx.context,run_config=config)

    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=not result.final_output.is_customer_support_query
    )
