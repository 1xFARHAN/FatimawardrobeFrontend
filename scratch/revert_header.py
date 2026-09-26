import re

filepath = r'artifacts\fatima-wardrobe\src\App.tsx'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Revert header background
text = text.replace('className="sticky top-0 z-40 border-b border-[#eaeaea] bg-white"', 'className="sticky top-0 z-40 border-b border-[#ded2c4] bg-[#f6f1e8]/95 backdrop-blur-md"')

# 2. Revert navigation typography
text = text.replace('className={`text-[13px] font-semibold uppercase tracking-wide transition-colors hover:text-[#f1592a] ${link.label === "Sale" ? "text-[#f1592a]" : "text-[#2f2925]"}`}', 'className={`text-[12px] font-medium uppercase tracking-[0.1em] transition-colors hover:text-[#a74636] ${link.label === "Sale" ? "text-[#a74636]" : "text-[#2f2925]"}`}')

# 3. Revert announcement bar
text = text.replace('className="bg-[#eecbd2] py-2.5 text-center text-[12px] font-medium text-gray-900"', 'className="bg-[#b9ced5] py-2 text-center text-[10px] tracking-[.08em] text-[#24383c]"')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

print("Reverted header changes")
