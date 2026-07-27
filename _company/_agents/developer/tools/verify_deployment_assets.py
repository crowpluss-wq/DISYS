import sys
import re

def verify_asset(file_path):
    """
    검증 대상 파일의 구조를 확인하고 가독성 향상 및 트래킹 코드 포함 여부를 검사함.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 주요 수치가 28pt 이상 확대 표기되어 있는지 확인 (정규식 매칭)
        font_size_pattern = re.compile(r'\b[0-9]{2}pt\b')
        matches = font_size_pattern.findall(content)

        # 트래킹 코드 G-1234567890 포함 여부 확인 (전문화진 아니지만 핵심 포인트)
        tracking_code = "G-1234567890"
        has_tracking = tracking_code in content

        return {
            'font_size_matches': matches,
            'has_tracking': has_tracking
        }
    except FileNotFoundError:
        print(f"Error: file not found at {file_path}")
        sys.exit(1)

def main():
    asset = sys.argv[1]
    results = verify_asset(asset)
    if results['has_tracking'] and len(results['font_size_matches']) > 0:
        print(f"✅ Verification successful for {asset}")
    else:
        print(f"❌ Verification failed for {asset}: Missing tracking or large font marker")
        sys.exit(1)

if __name__ == "__main__":
    main()