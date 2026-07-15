# 과제: 전 보험사 조사 및 신모델 대비표 작성 (Researcher + Writer 배분)

## 목표
- 한국 내 주요 보험(삼성화재, 한화 등) 설계 분석
- 진단비·수술비 60% 강화 모델 적용
- 제거/강화 대비 구조를 통한 소비자 체감형 비교 보고서 도출

## 가용 데이터 및 자원
- insurance_audit_log.md: 보험 상품 전수 조사 기초 자료
- reports/researcher_comparison_matrix_updated.md: 한화 대비 설계 분석 결과
- reports/diagnosis_surgery_enhancement_model.md: 진단비·수술비 강화 모델

## 산출물 정의
1. [Researcher] insurer_audit_summary.json - 각 사별 핵심 약점 및 제거 대상 항목 정리 (json 포맷)
2. [Writer] comparison_report.md - 일반 소비자용 대비 구조 기반 비교 보고서 (제거#808080, 강화#FF4B5C 적용)

## 배분 내용
- **Researcher**: insurer_audit_summary.json 생성 (data enrichment 단계 처리 및 수치 정교화 포함)
- **Writer**: comparison_report.md 집필 (2016-7-13 approved wording 기반, 제거/강화 대비 구조 시각적 강조 적용)

## 진행 지침
- researcher 결과물 내 중복 제거 사항을 grey로 처리하고 핵심 강화 포인트를 orange(#FF4B5C) 컬러로 명시할 것
- writer은 2067-713 approved wording 기반의 소비자용 문구 준수