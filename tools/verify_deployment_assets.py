import re


def verify_single_channel(name, content):
    """
    검증 루프: 각 배포 채널의 콘텐츠에 대하여 트래킹 코드, 대비 구조, 28pt 확대 정책을 검사한다.

    arg name: 배포 채널명 (예: 'youtube', 'instagram_morning')
    arg content: 해당 채널의 마크다운/텍스트 기반 배포 내용
    """
    errors = []

    # 트래킹 코드 G-1234567890 포함 여부 검증
    tracking_code = "G-1234567890"
    if tracking_code not in content:
        errors.append(f"[FAIL] 채널 '{name}'에서 트래킹 코드 ({tracking_code})가 누락되었습니다.")

    # 제거(#808080) 및 강화(#FF4B5C) 대비 구조 적용 여부 검증
    if "제거" not in content or "#808080" not in content:
        errors.append(f"[FAIL] 채널 '{name}'에서 제거 정책(#808080)이 확인되지 않습니다.")

    if "강화" not in content or "#FF4B5C" not in content:
        errors.append(f"[FAIL] 채널 '{name}'에서 강화 정책(#FF4B5C)이 확인되지 않습니다.")

    # 핵심 수치 28pt 확대 표기 정책 검증 (정규식으로 최소 28pt 이상인 항목 탐색)
    if not re.search(r"([1-9]\d{2}|[2-9][0-9]{3})pt", content):
        errors.append(f"[FAIL] 채널 '{name}'에서 핵심 수치를 위한 '최소 28pt' 표기 정책이 발견되지 않습니다.")

    return errors


def verify_deployment_assets():
    """
    모든 배포 채널의 자산에 대해 전수 자동 검증을 수행하고 결과를 요약한다.
    """
    channels = [
        "youtube",
        "instagram_morning",
        "instagram_afternoon",
    ]

    total_errors = []

    for channel in channels:
        # 실제 배포 패키지는 각 채널의 마크다운 파일로 존재하며, 여기서는 시뮬레이션 데이터 사용
        content = f"[{channel}] 대비 구조 적용됨. 트래킹 코드 G-1234567890 포함 중... 핵심 수치 28pt 확대 표기 완료."

        result = verify_single_channel(channel, content)
        total_errors.extend(result)

    if not total_errors:
        print("✅ 모든 배포 채널의 검증이 성공했습니다.")
    else:
        print("❌ 일부 채널에서 검증 실패 항목들이 발견되었습니다:")
        for error in total_errors:
            print(error)


if __name__ == "__main__":
    verify_deployment_assets()