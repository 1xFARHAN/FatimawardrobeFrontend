import re

filepath = r'artifacts\fatima-wardrobe\src\App.tsx'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Add useRef to react imports
text = text.replace('import { useEffect, useMemo, useState } from "react";', 'import { useEffect, useMemo, useState, useRef } from "react";')

# 2. Add sliderRef and useEffect to Home
home_start_pattern = r'function Home\(\) \{\s*return \('
home_start_replacement = """function Home() {
  const sliderRef = useRef<HTMLDivElement>(null);
  
  useEffect(() => {
    const interval = setInterval(() => {
      if (sliderRef.current) {
        const slider = sliderRef.current;
        const maxScroll = slider.scrollWidth - slider.clientWidth;
        if (slider.scrollLeft >= maxScroll - 10) {
          slider.scrollTo({ left: 0, behavior: 'smooth' });
        } else {
          slider.scrollBy({ left: slider.clientWidth / (window.innerWidth > 768 ? 4 : 2), behavior: 'smooth' });
        }
      }
    }, 5000);
    return () => clearInterval(interval);
  }, []);

  return ("""
text = re.sub(home_start_pattern, home_start_replacement, text)

# 3. Add ref={sliderRef} to the bestsellers div
div_pattern = r'<div className="flex overflow-x-auto gap-3 md:gap-5 snap-x snap-mandatory pb-2 \[\&::-webkit-scrollbar\]:hidden \[-ms-overflow-style:none\] \[scrollbar-width:none\]">'
div_replacement = r'<div ref={sliderRef} className="flex overflow-x-auto gap-3 md:gap-5 snap-x snap-mandatory pb-2 [&::-webkit-scrollbar]:hidden [-ms-overflow-style:none] [scrollbar-width:none]">'
text = re.sub(div_pattern, div_replacement, text)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

print("Auto slider added")
