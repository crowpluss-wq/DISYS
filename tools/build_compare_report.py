# 트래킹 태그를 포함한 한 페이지 분량의 보험 비교 보고서를 빌드한다.

TRACKING_TAG = "G-1234567890"


def build_comparison_report(data, output_path):
    summary = {
        "title": "보험 가입자 핵심 보호 강화 및 불필요 중복 제거",
        "tracker": TRACKING_TAG,
        "matrix": data.get("compare"),
        "bottom_line": "불필요한 특약을 걷어내고 진단비·수술비 등 실질적 보장을 강화하여 가입자 가치를 제고",
    }

    with open(output_path, 'w', encoding='utf-8') as f:
        import json
        json.dump(summary, f, indent=2)


def main():
    data = json.loads(open('sessions/2026-07-21T58_developer.json'))
    if not os.path.exists("build"): os.makedirs("build")
    build_comparison_report(data, "build/compare_report.json")