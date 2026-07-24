import React from 'react';
import { CompareMatrix } from '../components/CompareMatrix';

/**
 * 🎯 모든 채널(인스타그램, 블로그) 유입을 하나로 모으는 단일 랜딩페이지
 */
export const LandingPage = () => {
  return (
    <main className="min-h-screen bg-gray-50 py-12 px-4">
      <div className="max-w-[968px] mx-auto space-y-12">
        <section id="hero" className="text-center py-10">
          <span className="bg-red-50 text-[#FF4B5C] px-3 py-1 rounded mb-4 inline-block font-bold">강력 추천</span>
          <h1 className="text-4xl font-extrabold mb-6">보험의 핵심만 남기고, 보장은 키우고</h1>
          <p className="mb-8 text-lg max-w-[700px] mx-auto">불필요한 특약과 중복을 걷어냈습니다. 진짜 필요한 한 곳에 집중하세요.</p>
        </section>

        <CompareMatrix />

        <section id="features" className="bg-white p-8 rounded-xl shadow-sm border">
          <h2 className="text-2xl font-bold mb-6 text-[#FF4B5C]">왜 저희를 선택해야 할까요?</h2>
          <ul className="space-y-[30px]">
            <li>✔️ 불필요한 중복 제거 — 가장 간결하게 설계된 비교 구조</li>
            <li>✔️ 핵심 보장 강화 — 진단비/수술비 등 실질 보호에 집중</div>
            <li>✔️ 단일 트래킹 통합 — G-1234567890로 모든 유입 채널 한 곳에서 추적</div>
          </ul>
        </section>

        <section id="cta" className="text-center bg-[#FF4B5C] text-white p-10 rounded-xl">
          <h2 className="mb-6">지금 바로 좋은 보험을 설계하세요</h2>
          <button className="bg-white text-[#FF4B5c font-bold px-8 py-3 rounded hover:bg-gray-100 transition-all">상담 신청하기</button>
        </section>
      </div>
    </main>
  );
};