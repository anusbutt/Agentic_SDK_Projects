from pydantic import BaseModel
from agents import Agent, Runner, input_guardrail, TResponseInputItem, InputGuardrailTripwireTriggered, GuardrailFunctionOutput, RunContextWrapper
from configuration import config


class RealEstateOutput(BaseModel):
    is_RealEstateOutput: bool
    reasoning: str

guardrail_agent: Agent = Agent(
    name="guardrail_agent",
    instructions="check if the user is asking about any real estate query",
    output_type=RealEstateOutput
)

@input_guardrail
async def real_estate_guardrail(
    ctx: RunContextWrapper[None], agent: Agent, input: str|list[TResponseInputItem]
) -> GuardrailFunctionOutput:
    result = await Runner.run(guardrail_agent, input, context=ctx.context, run_config=config)

    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered= not result.final_output.is_RealEstateOutput
    )