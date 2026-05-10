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

        response = result.get("response", "")

        retrieval_success = len(result.get("retrieved_memories", [])) > 0

        keyword_match = (
            case["expected_keyword"].lower()
            in response.lower()
        )

        passed = (
            result["status"] == "success"
            and retrieval_success
            and keyword_match
        )

        results.append({
            "query": case["query"],
            "passed": passed,
            "retrieval_success": retrieval_success,
            "keyword_match": keyword_match
        })

        print("\n====================")
        print(f"Query: {case['query']}")
        print(f"Passed: {passed}")
        print(f"Retrieval Success: {retrieval_success}")
        print(f"Keyword Match: {keyword_match}")
        print(f"Response: {response}")
        print(f"Retrieved Memories: {result['retrieved_memories']}")

    return results


def summarize(results):

    total = len(results)

    passed = sum(1 for r in results if r["passed"])

    retrieval_pass = sum(
        1 for r in results if r["retrieval_success"]
    )

    keyword_pass = sum(
        1 for r in results if r["keyword_match"]
    )

    print("\n====================")
    print("EVALUATION SUMMARY")
    print("====================")
    print(f"Total Cases: {total}")
    print(f"Passed Cases: {passed}")
    print(f"Retrieval Success: {retrieval_pass}")
    print(f"Keyword Matches: {keyword_pass}")


if __name__ == "__main__":
    results = evaluate()
    summarize(results)
