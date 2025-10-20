from pydantic import BaseModel

class CheckOrderStatus(BaseModel):
    order_id: str

class CreateSupportTicket(BaseModel):
    customer_name: str
    issue: str

class ProcessRefund(BaseModel):
    order_id: str
    amount: float

class FaqLookup(BaseModel):
    question: str

class EscalateIssue(BaseModel):
    issue_id: str
