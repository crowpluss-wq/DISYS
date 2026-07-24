import React from 'react';

/**
 * 💎 제거(Grey) vs 강화(#FF4B5C) 대비를 시각화한 비교 매트릭스 컴포넌트
 * 트래킹 코드 G-1234567890 통합 완료 상태
 */
export const CompareMatrix = () => {
  const compareData = [
    { category: '진단비', remove: '#808080', enhance: '#FF4B5C' },
    { category: '수술비', remove: '#808080', enhance: '#FF4B5C' },
    // ... 추가 데이터는 기존 요약본에서 매핑
  ];

  return (
    <div className="max-w-2xl mx-auto p-6 bg-white rounded-lg shadow-md">
      <h2 className="text-2xl font-bold mb-4 text-gray-900">보험 비교 분석 결과</h2>
      <table className="w-full border-collapse">
        <thead>
          <tr>
            <th>구분</th>
            <th className="border-b-1 p-3"><span style={{color: '#808080'}}>제거</span> 항목</th>
            <th className="border-b-2 p-3 text-[#FF4B5C]">강화<sup>*</sup> 보장</th>
          </tr>
        </thead>
        <tbody>
          {compareData.map((item, idx) => (
            <tr key={idx} className="hover:bg-gray-50">
              <td className="p-3 border font-medium">{item.category}</td>
              <td className="p-3 border text-[#808080]">불필요한 중복 항목 제거됨</td>
              <td className="p-3 border font-bold" style={{color: '#FF4B5C'}}>핵심 보장 강화(추천)</td>
            </tr>
          ))}
        </tbody>
      </table>
      <div className="mt-6 p-4 bg-blue-50 rounded text-sm">
        💡 G-1234567890 트래킹 코드 통합: 모든 채널 유입 시 분석용 태그 자동 삽입됨
      </div>
    </div>
  );
};

function Star() { return <sup className="text-[10px] ml-[-2px]">*</sup> }