from app.memory_store import MemoryStore
from app.utils.gemini_client import GeminiClient
from app.utils.logger import get_logger
from app.config import MAX_INPUT_LENGTH

logger = get_logger(__name__)

memory_store = MemoryStore()
client = GeminiClient()


class MemoryAgentService:

    @staticmethod
    def remember(message: str):
        if not message or not message.strip():
            return {
                "status": "error",
                "response": "empty message",
                "retrieved_memories": []
            }

        message = message[:MAX_INPUT_LENGTH]

        relevant_memories = memory_store.search(message)

        context = "\n".join(relevant_memories)

        prompt = f"""
You are a conversational AI assistant with semantic memory.

Relevant past memories:
{context}

Current user message:
{message}

Answer conversationally while using relevant memories where useful.
"""

        response = client.generate(prompt)

        memory_store.add_memory(message)

        return {
            "status": "success",
            "response": response,
            "retrieved_memories": relevant_memories
        }

    @staticmethod
    def clear_memory():
        memory_store.clear()

        return {
            "status": "success",
            "message": "memory cleared"
        }

    @staticmethod
    def inspect_memory(query: str):
        results = memory_store.search(query)

        return {
            "status": "success",
            "query": query,
            "memories": results
        }
