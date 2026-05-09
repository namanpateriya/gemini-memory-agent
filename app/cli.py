import argparse
import json

from app.service import MemoryAgentService

parser = argparse.ArgumentParser(description="Gemini Memory Agent")

parser.add_argument("--message", help="Message to remember/respond to")
parser.add_argument("--inspect", help="Inspect relevant memories")
parser.add_argument("--clear", action="store_true", help="Clear memory")

args = parser.parse_args()


if args.message:
    result = MemoryAgentService.remember(args.message)
    print(json.dumps(result, indent=2))


if args.inspect:
    result = MemoryAgentService.inspect_memory(args.inspect)
    print(json.dumps(result, indent=2))


if args.clear:
    result = MemoryAgentService.clear_memory()
    print(json.dumps(result, indent=2))
