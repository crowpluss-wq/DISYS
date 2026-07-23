import os

def verify_tracking():
    """
    배포 패키지 내 트래킹 코드 중복 및 누락 여부를 검증하는 스크립트입니다.
    """
    banner_file = 'reports/banner_package_unified.md'
    tracker_tag = '[INSERT TRACKING CODE HERE]'

    if not os.path.exists(banner_file):
        return "에러: banner 파일이 존재하지 않습니다."

    with open(banner_file, 'r') as f:
        content = f.read()

    count = content.count(tracker_tag)
    result = f"검증 결과: 트래킹 태그 발견 횟수 = {count}"

    if count == 1:
        return result + "\n✅ 검증 통과: 단일한 경로로 통합됨."
    elif count > 1:
        return result + "\n❌ 중복 감지: 여러 위치에 트래킹 태그가 있습니다. 하나만 남겨야 합니다."
    else:
        return result + "\n⚠️ 누락 확인: 트래킹 태그를 찾을 수 없습니다."

if __name__ == "__main__":
    print(verify_tracking())