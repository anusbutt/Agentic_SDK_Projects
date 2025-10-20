from agents import Agent, ModelSettings
from tool import check_order_status, create_support_ticket, process_refund, faq_lookup, escalate_issue

order_agent=Agent(
    name="Order Support Agent",
    instructions="You are an order support agent. "
        "Always try to solve the problem using the tools provided. "
        "Rules: "
        "- If a customer provides an order ID, call the `check_order_status` tool. "
        "- If a customer asks about return/refund/return policy, call the `faq_lookup` tool. "
        "- Never transfer the user back to another agent if you can solve it yourself. "
        "- Respond with the result of the tool call directly.",
    tools=[check_order_status, faq_lookup]
)

billing_agent=Agent(
    name="Billing Support Agent",
    instructions="Handle payments, refunds, and billing issues.",
    tools=[process_refund]
)

tech_agent=Agent(
    name="Technical Support Agent",
    instructions="Assist with technical issues and escalate if needed.",
    tools=[create_support_ticket, escalate_issue]
)

faq_agent=Agent(
    name="FAQs Agent",
    instructions="Answer frequently asked questions about company policies.",
    tools=[faq_lookup]
)