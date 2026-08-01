## 🎯 통합 리서치 및 데이터 세트 확정 작업

### 목표
불명확한 특약과 보장 범위를 조사하여 `reports/insurance_comparison_matrix_final.md`의 빈칸을 채우고, 제거(#808080) vs 강화(#FF4B5c) 시각화를 위한 정밀 데이터 세트를 구축한다.

### 배분
- **Researcher**: 외부 소스(보험사 홈페이지, 법률 정보 등) 조사를 통해 불명확한 특약/보장 수치 사실 확인 및 보완 → `reports/unclear_terms_verified.json`로 기록 (데이터셋 확정용)
- **한빈**: 검증된 데이터를 기반으로 비교 매트릭스의 빈칸을 채우고 제거/강화 대비 구조에 맞는 형태로 정제 → `reports/refined_comparison_matrix.md` 생산

### 산출물 명세
1. verified_data: 불명확했던 항목들이 수치로 확인된 원시 데이터셋 (Researcher)
2. refined_matrix: 시각화 레이아웃을 위해 보정 및 정렬이 완료된 비교표 (한빈)