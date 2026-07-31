# [개발자 기술 사양] 제거 vs 강화 대비 구조 및 배포 자산 검증 (GA4 G-1234567890)

## 🛡 시각/텍스트 통합 사항
Designer에서 정의한 **세로형 2분할 레이아웃**을 모든 배포 채널의 표준으로 삼는다. 모바일 환경 가독성을 위해 핵심 문구는 최소 **28pt 이상** 확대 적용한다.

- **제거(Grey)**: `#808080`, 불필요한 항목 삭제 및 아이콘 처리
- **강화(Enhance)**: `#FF4B5c`, 진단비·수술비 등 핵심 보장 강조형 디자인
- **카드뉴스**: 정보성/감성적 대비 구조를 담은 2종 소스 활용

## 🔗 배포 자산 검증 루프 (GA4 G-1234567890)
각 배포 경로의 트래킹 코드 삽입 상태를 다음 항목에 따라 일괄적으로 재검증한다:

| 채널 | 대상 프로토콜 / 파라미터 | 추적 코드 (G-1234567890)| 검증 결과(Status) |
| :--- | :--- | :--- | :--- |
| YouTube Info/Emotion | UTM_source=youtube&utm_medium=video | G-1234567890 | Pass / Fail (Run verify_deployment_assets.py) |
| Instagram Morning/Afternoon | utm_source=instagram&utm_medium=social | G-1234567890 | Pass / Fail (Run verify_deployment_assets.py) |

## 🛠️ 검증 프로세스 및 도구
검증 루프 실패 시 에러 메시지 기반 자동 재시도(최대 2회). 결과는 `verify_deployment_assets.py`를 통해 확인한다.

```bash
# 전체 배포 자산의 트래킹 코드 삽입 정확성 검증
python3 verify_deployment_assets.py --all-routes --ga4 G-1234567890
```

## 📝 결과 요약 및 후속 조치
모든 채널에 GA4 추적 코드가 올바르게 매핑되었는지 확인한 뒤, 통과 시 `publish_to_blog.py`로 최종 배포를 승인한다. 검증 실패 시 해당 경로의 파라미터 재정합 후 재실행한다.

## 📁 출력물 패키지
- [x] 통합 기술 사양서 (developer.md)
- [ ] 트래킹 코드 전수 검증 결과 리포트 (`verify_deployment_assets.py` 실행 시 생성됨)