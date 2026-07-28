import sys

def verify(files):
    tracker = "G-1234567890"
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            if content.count(tracker) > 1:
                print(f"Error: duplicate tracker in {file}")
                sys.exit(2)

def apply_fixes(files):
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            new_content = content.replace('트래킹 코드', tracker)
            with open(file, 'w', encoding='utf-8') as fw:
                fw.write(new_content)

if __name__ == "__main__":
    files = [f for f in sys.argv[1:] if f.endswith(".md")]
    verify(files)
    apply_fixes(files)