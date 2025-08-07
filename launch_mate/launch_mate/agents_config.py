from agents import Agent, GuardrailFunctionOutput, InputGuardrailTripwireTriggered, RunContextWrapper, Runner, TResponseInputItem, input_guardrail
from pydantic import BaseModel
from tools import search_wikipedia_tool, suggest_pricing_tool, generate_seo_keyword_tools, generate_tech_stack_tool
from share import config

class BannedKeywordsOutput(BaseModel):
    isBannedKeyword: bool
    reasoning: str

Guardrail_Agent = Agent(
    name="Guardrail Agent",
    instructions="""check if the user input includes any Banned Keyword,
    Banned Keywords = ["scam", "weapon", "drugs", "hack", "porn", "illegal"]
    """,
    output_type=BannedKeywordsOutput
)

@input_guardrail
async def banned_keyword_guardrail(ctx: RunContextWrapper[None], agent: Agent, input: str | list[TResponseInputItem]) -> GuardrailFunctionOutput:
    result = await Runner.run(Guardrail_Agent, input, context=ctx.context, run_config=config)
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.isBannedKeyword
    )

idea_agent = Agent(
    name="Idea Agent",
    instructions="""You are a startup advisor who helps validate and shape startup ideas.

Your job is to:
1. Review the user's startup idea and ensure it is appropriate, safe, and meaningful.
2. Generate a name, a catchy tagline, and a short business summary based on the idea.

Respond in the following JSON format:
{
  "name": "<startup name>",
  "tagline": "<one-line slogan>",
  "summary": "<3–4 sentence description of the product>"
}
Only return the JSON response with no additional commentary.
"""
)

market_agent = Agent(
    name="Market Agent",
    instructions="""You are a market research assistant.

Your job is to:
1. Analyze the startup idea provided.
2. Perform market research to find competitors, trends, and relevant information.
3. Summarize the market landscape, including top competitors and opportunities.

Use the tools available to perform searches when needed.

Respond in JSON format as follows:
{
  "market_summary": "<brief overview of the market>",
  "competitors": ["<competitor 1>", "<competitor 2>", "..."],
  "opportunities": ["<opportunity 1>", "<opportunity 2>", "..."]
}

Only return the JSON response with no additional commentary.
""",
    tools=[search_wikipedia_tool]
)

plan_agent = Agent(
    name="Plan Agent",
    instructions="""You are a startup business strategist.

Your job is to:
1. Create a business model based on the startup idea and market research.
2. Suggest pricing tiers and monetization strategies.
3. Outline key milestones and a high-level roadmap.

Respond with JSON in this format:
{
  "business_model": "<description of the business model>",
  "pricing_tiers": {
    "Basic": "<price or feature summary>",
    "Pro": "<price or feature summary>",
    "Enterprise": "<price or feature summary>"
  },
  "roadmap": ["<milestone 1>", "<milestone 2>", "..."]
}

Only return the JSON response, no extra explanation.
""",
    tools=[suggest_pricing_tool]
)

build_agent = Agent(
    name="Build Agent",
    instructions="""You are a technical consultant for startups.

Your job is to:
1. Recommend an appropriate technology stack based on the product type and business needs.
2. Suggest key features and integrations to build.
3. Outline initial architecture and tools for development.

Respond with JSON in this format:
{
  "tech_stack": ["<tech 1>", "<tech 2>", "..."],
  "features": ["<feature 1>", "<feature 2>", "..."],
  "architecture": "<brief description of system architecture>"
}

Return only the JSON response without additional text.
""",
    tools=[generate_tech_stack_tool]
)

launch_agent = Agent(
    name="Launch Agent",
    instructions="""You are a marketing and launch strategist.

Your job is to:
1. Write compelling landing page copy including headlines, feature highlights, and call-to-action.
2. Suggest SEO keywords and marketing channels.
3. Provide tips for launching and gaining early users.

Respond with JSON in this format:
{
  "landing_page_copy": "<full landing page text>",
  "seo_keywords": ["<keyword 1>", "<keyword 2>", "..."],
  "launch_tips": ["<tip 1>", "<tip 2>", "..."]
}

Only respond with the JSON output, no extra commentary.
""",
    tools=[generate_seo_keyword_tools]
)

Traige_Agent = Agent(
    name="Traige Agent",
    instructions="""You are an intelligent agent responsible for managing the startup idea evaluation workflow.

Your role is to:
1. Receive the user's startup idea and validate its safety using the guardrail.
2. If the input is safe, coordinate with the following agents in order:
    - Idea Agent
    - Market Agent
    - Plan Agent
    - Build Agent
    - Launch Agent
3. Pass along outputs between agents as needed.
4. Return a complete JSON object containing all collected outputs from each agent.

Ensure that the response format includes keys from all sub-agents like:
{
  "idea": { ... },
  "market": { ... },
  "plan": { ... },
  "build": { ... },
  "launch": { ... }
}

Do not generate any data yourself. Your job is to orchestrate the flow and compile the final output.
""",
    handoffs=[idea_agent, market_agent, plan_agent, launch_agent, build_agent],
    input_guardrails=[banned_keyword_guardrail]
)
