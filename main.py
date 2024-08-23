import json
import sys
from pathlib import Path

if (args_count := len(sys.argv)) > 2:
    print(f"One argument expected, got {args_count - 1}")
    raise SystemExit(2)
elif args_count < 2:
    print("You must specify the target file")
    raise SystemExit(2)

target_file = Path(sys.argv[1])

if not target_file.is_file():
    print("The target file doesn't exist")
    raise SystemExit(1)

f = open(target_file)
data = json.load(f)
with open('Salesforce_Document_IDs.txt', 'w') as f:
    for i in data["result"]:
        f.write(f"{i["record"]["Id"]}\n")
