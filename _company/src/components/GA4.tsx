import React, { useEffect } from 'react';

const GA4 = () => {
  useEffect(() => {
    const script = document.createElement('script');
    script.async = true;
    // Global site tag (gtag.js) - Google Analytics
    script.src = 'https://www.googletagmanager.com/gtag/js?id=G-1234567890';
    document.head.appendChild(script);

    window.dataLayer = window.dataLayer || [];
    function gtag() {
      window.dataLayer.push(arguments);
    }
    gtag('js', new Date());
    gtag('gtag','G-1234567890');
  }, []);

  return null;
};

export default GA4;