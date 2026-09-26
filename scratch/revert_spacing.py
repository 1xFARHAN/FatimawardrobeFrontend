import re

filepath = r'artifacts\fatima-wardrobe\src\App.tsx'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update Header to be left-aligned (side) with less spacing
header_pattern = r'<header className="pt-10 pb-8 md:pt-24 md:pb-16 text-center">\s*<div className="mx-auto max-w-\[1440px\] px-5 md:px-12 flex flex-col items-center">\s*<p className="font-mono-ui text-\[10px\] uppercase tracking-\[\.25em\] text-\[#a74636\]">The collection</p>\s*<h1 className="mt-4 font-display text-5xl md:text-7xl text-\[#2f2925\] tracking-tight">\{title\}</h1>\s*<p className="mt-6 font-mono-ui text-\[10px\] uppercase tracking-\[\.16em\] text-\[#776b61\]">\s*\{shown\.length\} pieces\s*</p>\s*</div>\s*</header>'

header_replacement = """<header className="pt-6 pb-2 md:pt-10 md:pb-4 border-b border-transparent">
        <div className="mx-auto flex max-w-[1440px] items-end justify-between gap-6 px-5 md:px-12">
          <div>
            <p className="font-mono-ui text-[10px] uppercase tracking-[.25em] text-[#a74636]">The collection</p>
            <h1 className="mt-2 font-display text-4xl md:text-5xl text-[#2f2925] tracking-tight">{title}</h1>
          </div>
          <p className="hidden font-mono-ui text-[10px] uppercase tracking-[.16em] text-[#776b61] sm:block">
            {shown.length} pieces
          </p>
        </div>
      </header>"""

text = re.sub(header_pattern, header_replacement, text, flags=re.DOTALL)

# 2. Update Grid spacing
grid_pattern = r'<div className="grid grid-cols-2 gap-x-2 gap-y-12 md:grid-cols-4 md:gap-x-8 md:gap-y-20">'
grid_replacement = '<div className="grid grid-cols-2 gap-x-2 gap-y-10 md:grid-cols-4 md:gap-x-4 md:gap-y-12">'

text = text.replace(grid_pattern, grid_replacement)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

print("Done")
