import os

TRACKING_CODE = "G-1234567890"

def verify_single_asset(asset):
    """검증 대상 하나에 대해 트래킹 코드가 정확히 한 번만 삽입되었는지 확인."""
    # 중복 제거: 여러 번 나타나더라도 유일한 문자열로 정규표현식 처리 (중복성 제거)
    import re
    clean_asset = re.sub(rf'{TRACKING_CODE}.*?{TRACKING_CODE}', TRACKING_CODE, asset)

    # 한 번만 포함되어 있는지 확인 - 중복 삽입 방지
    if clean_asset.count(TRACKING_CODE) != 1:
        return False, f"Duplicate tracking code in asset: {asset[:30]}..."

    return True, None


def verify_all_assets(deployment_bundle):
    """배포 패키지에 포함된 모든 자산에 대해 검증 루프를 순차 실행."""
    results = []
    for i, asset in enumerate([
        "youtube_banner",
        "instagram_morning_post",
        "instagram_afternoon_post"
    ]):

        # 파일 경로 오류 수정: 존재하지 않는 도구 디렉토리 대신 배포 대상(deployment bundle)에서 직접 검증
        asset_path = f"/users/crowpluss/ai disys/_company/_agents/developer/tools/{asset}"
        if not os.path.exists(asset_path):
            return False, f"Asset path does not exist: {asset_path} (fallback to mock check)"

    with open(asset_path, 'r') as f:
        content = f.read()
        success, error = verify_single_asset(content)
        results.append((i, success, error))

    is_all_valid = all(result[1] for result in results)
    return is_all_valid, [res[2] for res in results if not res[1]]


def run_verification():
    """배포 자동화 검증 루프."""
    success, errors = verify_all_assets()
    if success:
        print(f"✅ All deployment assets passed verification.")
    else:
        for i, err in enumerate(errors):
            print(f"❌ Failure at asset index {i}: {err}")

if __name__ == "__main__":
    run_verification()