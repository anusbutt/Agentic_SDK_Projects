from agents import function_tool, RunContextWrapper
from context import CheckOrderStatus, CreateSupportTicket, ProcessRefund, FaqLookup, EscalateIssue


@function_tool
def check_order_status(wrapper: RunContextWrapper[CheckOrderStatus]) -> str:
    """check order status by ID"""
    fake_orders = {"A123": "shipped", "B456": "Processing", "C789": "Delivered"}
    return fake_orders.get(wrapper.context.order_id, "order not found")

@function_tool
def create_support_ticket(wrapper: RunContextWrapper[CreateSupportTicket]):
    """Create Support Ticket."""
    return f"Ticket created for {wrapper.context.customer_name}. Issue: {wrapper.context.issue}"

@function_tool
def process_refund(wrapper: RunContextWrapper[ProcessRefund]):
    """Process a refund for a given order"""
    return f"Refund of {wrapper.context.amount:.2f} has been issued for order id: {wrapper.context.order_id}"

@function_tool
def faq_lookup(wrapper: RunContextWrapper[FaqLookup]):
    """lookedup frequently asked questions."""
    q = wrapper.context.question.lower()
    faq_data={
        "return": "You can return items within 30 days of purchase.",
        "refund": "Refunds are processed within 5–7 business days.",
        "return policy": "You can return items within 30 days of purchase.",
        "shipping time": "Shipping usually takes 3–5 business days.",
        "payment methods": "We accept credit cards, PayPal, and Apple Pay.",
    }
    for key, answer in faq_data.items():
        if key in q:
            return answer
    return "I couldn't find this in our FAQs"
@function_tool
def escalate_issue(wrapper: RunContextWrapper[EscalateIssue]):
    """Escalate issue to human support staff."""
    return f"Issue: {wrapper.context.issue_id} has been escalated to a senior supportive representative."
