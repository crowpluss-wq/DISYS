import re
import sys


def verify_tracking_code(paths, tracking_id="G-1234567890"):
    """
    모든 배포 경로에 트래킹 코드가 포함되어 있는지 확인합니다.
    """
    missing = []
    for path in paths:
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
                if tracking_id not in content:
                    missing.append((path, "Tracking code missing"))
        except FileNotFoundError:
            missing.append((path, "File not found")))

    return missing


def verify_contrast_layout(paths):
    """
    제거(#808080)와 강화(#FF4B5C) 대비 구조가 시각적으로 극대화되어 있는지 확인합니다.
    """
    issues = []
    for path in paths:
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
                if "#808080" not in content or "#FF4B5C" not in content:
                    issues.append((path, "Contrast colors missing"))
        except FileNotFoundError:
            issues.append((path, "File not found")))

    return issues


def run_verification(paths):
    results = []
    tracking_missing = verify_tracking_code(paths)
    layout_issues = verify_contrast_layout(paths)

    if not tracking_missing and not layout_issues:
        print("All verification checks passed.")
    else:
        for missing in tracking_missing:
            print(f"FAILED: {missing[0]} - {missing[1]}")
        for issue in layout_issues:
            print(f"FAILED: {issue[0]} - {issue[1]}")

    return "SUCCESS" if not tracking_missing and not layout_issues else "FAILURE"


if __name__ == "__main__":
    paths = sys.argv[1:]
    result = run_verification(paths)
    sys.exit(0 if result == "SUCCESS" else 1)