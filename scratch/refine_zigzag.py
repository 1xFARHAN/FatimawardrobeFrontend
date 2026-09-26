import re

filepath = r'artifacts\fatima-wardrobe\src\App.tsx'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# Make the outer container narrower (max-w-[1200px] was already set, let's keep it max-w-[1100px] to bring things even closer)
pattern_container = r'<div className="mx-auto max-w-\[1200px\] px-5 py-12 md:px-12 md:py-20 flex flex-col gap-16 md:gap-24">'
repl_container = r'<div className="mx-auto max-w-[1100px] px-5 py-12 md:px-12 md:py-16 flex flex-col gap-12 md:gap-16">'
text = re.sub(pattern_container, repl_container, text)

# Balance the image and text widths to 50/50 and reduce the gap
pattern_row = r'className=\{`group flex flex-col \$\{isEven \? \'md:flex-row\' : \'md:flex-row-reverse\'\} items-center gap-8 md:gap-16`\}'
repl_row = r'className={`group flex flex-col ${isEven ? \'md:flex-row\' : \'md:flex-row-reverse\'} items-center gap-8 md:gap-12`}'
text = re.sub(pattern_row, repl_row, text)

# Image block width
pattern_img = r'<div className="w-full md:w-\[45%\] lg:w-\[40%\] overflow-hidden relative bg-\[#ebe1d5\]">'
repl_img = r'<div className="w-full md:w-[48%] lg:w-[48%] overflow-hidden relative bg-[#ebe1d5]">'
text = re.sub(pattern_img, repl_img, text)

# Text block width
pattern_text = r'<div className=\{`w-full md:w-\[45%\] lg:w-\[50%\] flex flex-col justify-center text-center \$\{isEven \? \'md:text-left\' : \'md:text-right\'\} reveal`\}'
repl_text = r'<div className={`w-full md:w-[48%] lg:w-[48%] flex flex-col justify-center text-center ${isEven ? \'md:text-left\' : \'md:text-right\'} reveal`}'
text = re.sub(pattern_text, repl_text, text)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

print("Refined zig-zag layout!")
