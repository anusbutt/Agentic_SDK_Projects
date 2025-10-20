from pydantic import BaseModel
from configuration import config
from agents import (
    Agent,
    GuardrailFunctionOutput,
    OutputGuardrailTripwireTriggered,
    RunContextWrapper,
    Runner,
    TResponseInputItem,
    output_guardrail,
)

class MessageOutput(BaseModel):
    message: str

class customerSupportOutput(BaseModel):
    reasoning: str
    is_customer_support_query: bool

customer_support_guardrail_agent = Agent(
    name = "customer support guardrail",
    instructions = "You are a guardrail agent that checks if the output is a customer support output.",
    output_type = customerSupportOutput,
)

@output_guardrail
async def customer_support_guardrail(
    ctx: RunContextWrapper, agent: Agent, output: MessageOutput
    ) -> GuardrailFunctionOutput:
    result =await Runner.run(customer_support_guardrail_agent, output, context=ctx.context, run_config=config)

    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=not result.final_output.is_customer_support_query
    )