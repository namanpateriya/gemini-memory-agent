import argparse
import json

from app.service import MemoryAgentService, memory_store

parser = argparse.ArgumentParser(description="Gemini Memory Agent")

parser.add_argument(
    "--message",
    help="Message to remember/respond to"
)

parser.add_argument(
    "--inspect",
    help="Inspect relevant memories"
)

parser.add_argument(
    "--clear",
    action="store_true",
    help="Clear memory"
)

args = parser.parse_args()


def pretty_print(result):
    print(json.dumps(result, indent=2, ensure_ascii=False))


if args.message:
    result = MemoryAgentService.remember(args.message)
    pretty_print(result)

elif args.inspect:

    if not memory_store.memories:
        print("No memories available. Add memories first using --message")

    else:
        result = MemoryAgentService.inspect_memory(args.inspect)
        pretty_print(result)

elif args.clear:
    result = MemoryAgentService.clear_memory()
    pretty_print(result)

else:
    parser.print_help()
