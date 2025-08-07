import wikipedia
from agents import RunContextWrapper, function_tool
from context import UserContext

@function_tool
async def search_wikipedia_tool(wrapper: RunContextWrapper[UserContext]):
    """Search Wikipedia for related trends or competitors"""
    try:
        summary = wikipedia.summary(wrapper.context.idea, sentences=3)
        return f"🔍 Wikipedia Summary:\n{summary}"
    except Exception as e:
        return f"❌ Search failed: {e}"


@function_tool
async def suggest_pricing_tool(wrapper: RunContextWrapper[UserContext]):
    """Suggest pricing tiers based on audience"""
    audience = wrapper.context.audience.lower()
    if audience == "enterprise":
        return {
            "Basic": "$99/month",
            "Pro": "$299/month",
            "Enterprise": "$999/month"
        }
    elif audience == "consumer":
        return {
            "Free": "$0",
            "Pro": "$9.99/month",
            "Premium": "$19.99/month"
        }
    else:
        return {
            "Standard": "$29/month"
        }

@function_tool
async def generate_tech_stack_tool(wrapper: RunContextWrapper[UserContext]):
    """suggest a tech stack based on the product type"""
    product_type = wrapper.context.product_type.lower()

    if "mobile" in product_type:
        return ["Flutter", "Firebase", "Supabase"]
    elif "web" in product_type:
        return ["Next.js", "FastAPI", "PostgreSQL"]
    elif "ai" in product_type:
        return ["Python", "HuggingFace", "VectorDB", "FastAPI"]
    else:
        return ["React", "MongoDB", "Nodejs"]

@function_tool
def generate_seo_keyword_tools(wrapper: RunContextWrapper[None]):
    """Generate basic SEO keywords from product idea"""
    base = wrapper.context.idea.lower().split()
    keywords = list(set(base + [f"{w} app" for w in base if len(w) > 3]))
    return keywords[:10]
