from pydantic import BaseModel


class Request(BaseModel):
    id: int
    user_id: int
    description: str
    status: str
    created_at: str
    updated_at: str
