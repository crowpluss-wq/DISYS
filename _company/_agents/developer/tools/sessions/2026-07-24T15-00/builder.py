import json
import sys

def build(package):
    print(f"BUILDING: {json.dumps(package)}")

if __name__ == "__main__":
    data = json.loads(sys.stdin.read())
    build(data["package"])
