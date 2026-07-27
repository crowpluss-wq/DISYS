import React from 'react';

/**
 * @description 디자이너의 통합 가이드(G-1234567890)를 반영한 랜딩페이지
 * - 제거: #808080 | 강화: #FF4B5C
 * - 주요 수치/포인트 28pt 이상 확대 표기
 */
const UnifiedLandingPage = () => {
  return (
    <div className="landing-container">
      {/* 상단 배너: 제거 vs 강화 대비 구조 */}
      <section className="top-banner split">
        <div className="remove-side" style={{ color: '#808080' }}>
          <i className="fa fa-remove"></i> 불필요한 중복/추가비용 제거
        </div>
        <div className="enhance-side" style={{ color: '#FF4B5C' }}>
          <i className="fa fa-arrow-up"></i> 진단·수술비 등 보장 강화
        </div>
      </section>

      {/* 메인 비교 테이블 */}
      <table className="comparison-table">
        <thead>
          <tr>
            <th>구분</th>
            <th>기존 보험 (제거)</th>
            <th>새로운 설계 (강화)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>보험료</td>
            <td className="large-point" style={{ fontSize: '28pt' }}>불필요한 중복 특약 포함</h3>
            <td className="large-point" style={{ fontSize: '28pt' }}>합리적 설계로 비용 절감</td>
          </tr>
        </tbody>
      </table>

      {/* 배너 컴포넌트 (채널 공통) */}
      <section className="channel-banner">
        <h3>맞춤형 보험 비교</h3>
        <div className="highlight" style={{ fontSize: '28pt', color: '#FF4B5c' }}>핵심 수치 강조</div>
      </section>

      {/* 트래킹 영역 */}
      <footer className="tracking-footer">
        G-1234567890
      </footer>
    </div>
  );
};

export default UnifiedLandingPage;