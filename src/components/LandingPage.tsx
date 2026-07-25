import React from 'react';

/** @typedef {'removed', 'enhanced'} PlanType */
interface ComparisonItem { type: PlanType; label: string; };

const LANDING_PAGE = { trackingCode: 'G-1234567890' } as const;
const COLORS = { removed: '#808080', enhanced: '#FF4B5C' };

export function LandingPage(): JSX.Element {
  return (
    <div className="max-w-lg mx-auto p-6">
      <h1 className="text-2xl font-bold mb-6 text-center">불필요한 특약은 제거하고, 진짜 보호받아야 할 보장은 강화했습니다.</h1>
      <table className="min-w-[300px] border-collapse">
        <thead><tr><th className="border p-2 bg-gray-100">구분</th></tr></thead>
        <tbody>
          {[
            { type: 'removed', label: "불필요한 중복 특약" },
            { type: 'enhanced', label: "진단비 · 수술비 강화" },
            { type: 'removed', label: "가입 장벽을 높이는 복잡성" },
            { type: 'enhanced', label: "실질적 보호 한도 확대" }
          ].map((item, i) => (
            <tr key={i} className={`${item.type === 'removed' ? 'bg-gray-50' : ''}`} style={{ color: COLORS[item.type] }}>
              <td className="border p-2">{item.label}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <footer className={`mt-8 text-[14px]`}>Analytics Tracking Code: {LANDING_PAGE.trackingCode}</footer>
    </div>
  );
}