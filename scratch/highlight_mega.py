import re

filepath = r'artifacts\fatima-wardrobe\src\App.tsx'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# Make the mega menu a floating centered box with strong shadow and borders
mega_pattern = r'\{activeMega && \(\s*<div\s*onMouseLeave=\{\(\) => setActiveMega\(null\)\}\s*className="absolute left-0 right-0 border-t border-\[#ded2c4\] bg-\[#ffffff\] shadow-xl transition-opacity duration-200"\s*>\s*<div className="mx-auto max-w-\[1200px\] px-8 py-10">'

mega_replacement = """{activeMega && (
          <div
            onMouseLeave={() => setActiveMega(null)}
            className="absolute left-1/2 -translate-x-1/2 top-[100%] w-full max-w-[1050px] mt-[1px] bg-[#ffffff] shadow-[0_20px_50px_rgba(47,38,32,0.2)] border border-[#ded2c4] transition-opacity duration-200"
          >
            <div className="mx-auto w-full px-8 py-10">"""

text = re.sub(mega_pattern, mega_replacement, text, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

print("Mega menu highlighted")
