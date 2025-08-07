from pydantic import BaseModel

class UserContext(BaseModel):
    name: str
    uid: int
    is_premium_user: bool = False
    issue_type: str = "general"
    product_type: str
