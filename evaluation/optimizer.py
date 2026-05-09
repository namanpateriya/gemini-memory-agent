from evaluation.evaluator import evaluate


def optimize():
    results = evaluate()

    failures = [r for r in results if not r["passed"]]

    print("\n====================")
    print(f"Failures: {len(failures)}")

    if failures:
        print("Investigate memory retrieval quality")
    else:
        print("System stable")


if __name__ == "__main__":
    optimize()
