import re

filepath = r'artifacts\fatima-wardrobe\src\App.tsx'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the mega menu wrapper width classes
# From: w-full max-w-[1050px]
# To: w-fit min-w-[max-content]
mega_pattern = r'className="absolute left-1/2 -translate-x-1/2 top-\[100%\] w-full max-w-\[1050px\] mt-\[1px\] bg-\[#ffffff\] shadow-\[0_20px_50px_rgba\(47,38,32,0\.2\)\] border border-\[#ded2c4\] transition-opacity duration-200"'

mega_replacement = r'className="absolute left-1/2 -translate-x-1/2 top-[100%] w-fit mt-[1px] bg-[#ffffff] shadow-[0_20px_50px_rgba(47,38,32,0.2)] border border-[#ded2c4] transition-opacity duration-200 rounded-sm"'

text = re.sub(mega_pattern, mega_replacement, text, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

print("Mega menu width adjusted to fit-content")
