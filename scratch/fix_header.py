import re

filepath = r'artifacts\fatima-wardrobe\src\App.tsx'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update header background to solid white, matching Khaadi
header_bg_pattern = r'className="sticky top-0 z-40 border-b border-\[#ded2c4\] bg-\[#f6f1e8\]/95 backdrop-blur-md"'
header_bg_replacement = r'className="sticky top-0 z-40 border-b border-[#eaeaea] bg-white"'
text = re.sub(header_bg_pattern, header_bg_replacement, text)

# 2. Fix the navigation link typography (remove excessive tracking, make font-semibold, Khaadi orange for Sale)
nav_pattern = r'className=\{`text-\[12px\] font-medium uppercase tracking-\[0\.1em\] transition-colors hover:text-\[#a74636\] \$\{link\.label === "Sale" \? "text-\[#a74636\]" : "text-\[#2f2925\]"\}`\}'
nav_replacement = r'className={`text-[13px] font-semibold uppercase tracking-wide transition-colors hover:text-[#f1592a] ${link.label === "Sale" ? "text-[#f1592a]" : "text-[#2f2925]"}`}'
text = re.sub(nav_pattern, nav_replacement, text)

# 3. Update the announcement bar to pale pink like Khaadi
announcement_pattern = r'className="bg-\[#b9ced5\] py-2 text-center text-\[10px\] tracking-\[\.08em\] text-\[#24383c\]"'
announcement_replacement = r'className="bg-[#eecbd2] py-2.5 text-center text-[12px] font-medium text-gray-900"'
text = re.sub(announcement_pattern, announcement_replacement, text)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

print("Header styling fixed!")
