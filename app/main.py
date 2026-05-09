from fastapi import FastAPI

from app.schemas import MessageRequest
from app.service import MemoryAgentService

app = FastAPI(
    title="Gemini Memory Agent",
    description="Semantic memory agent powered by Google Gemini",
    version="1.0.0"
)


@app.get("/")
def health():
    return {
        "status": "running",
        "provider": "Google Gemini"
    }


@app.post("/chat")
def chat(req: MessageRequest):
    return MemoryAgentService.remember(req.message)


@app.post("/inspect")
def inspect(req: MessageRequest):
    return MemoryAgentService.inspect_memory(req.message)


@app.post("/clear")
def clear():
    return MemoryAgentService.clear_memory()
