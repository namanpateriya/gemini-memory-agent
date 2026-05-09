from pydantic import BaseModel


class MessageRequest(BaseModel):
    message: str


class MemoryResponse(BaseModel):
    status: str
    response: str
    retrieved_memories: list
