import json
from selenium import webdriver
# 크롤링 로직은 각 사 보장 구조 추출에 집중 (제거/강화 매트릭스용 데이터 확보)
def scrape_insurance_data(source_list):
    results = []
    for source in source_list:
        # 구현체는 샘플로 대체 - 실제 환경에서 selenium 세팅 필요
        print(f"Scraping {source['name']} from {source['url']}")
        results.append({
            "company": source["name"],
            "coverage": "parsed coverage details",
            "pros_cons": {"remove": [], "strengthen": []},
            "premium_level": ""
        })
    return results

if __name__ == "__main__":
    with open("data_sources.json") as f:
        source = json.load(f)
    scrape_insurance_data(source)
</scraper.py>

<create_file path="researcher_expanded_scope.md">
# Researcher 확장 분석 계획 (전 보험사 조사)

## 목표
대한민국 주요 보험사의 상품을 전수 조사하여 핵심 보장과 장단점을 비교 매트릭스에 통합함.

## 방법론
- **데이터 소스**: `data_sources.json` 기반 크롤링 자동화
- **분석 구조**: 제거(Grey)/강화(Red) 대비 유지 (불필요 특약 제외, 핵심 보장 강화)
- **사실 검증**: 추측 배제하고 확인된 수치만 근거로 사용

## 산출물 계획
[ ] scraping script (`scraper.py`) deployment
[ ] 비교 데이터 추출 및 `insurance_comparison_matrix_expanded.md` 업데이트