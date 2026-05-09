import json
import os

from app.service import MemoryAgentService

BASE_DIR = os.path.dirname(__file__)
TEST_FILE = os.path.join(BASE_DIR, "test_cases.json")


def evaluate():
    with open(TEST_FILE, "r", encoding="utf-8") as f:
        cases = json.load(f)

    results = []

    for case in cases:
        MemoryAgentService.clear_memory()

        MemoryAgentService.remember(case["memory"])

        result = MemoryAgentService.remember(case["query"])

        passed = (
            result["status"] == "success"
            and len(result["retrieved_memories"]) > 0
        )

        results.append({
            "query": case["query"],
            "passed": passed
        })

        print("\n====================")
        print(f"Query: {case['query']}")
        print(f"Passed: {passed}")
        print(f"Retrieved Memories: {result['retrieved_memories']}")

    return results


if __name__ == "__main__":
    evaluate()
