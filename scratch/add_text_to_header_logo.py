import re

filepath = r'artifacts\fatima-wardrobe\src\App.tsx'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

header_logo_pattern = r'<Link href="/" className="flex items-center justify-center" data-testid="link-logo">\s*<img src="/Fatima_logo\.png" alt="Fatima Wardrobe" className="h-14 md:h-16 w-auto object-contain" />\s*</Link>'
header_logo_repl = """<Link href="/" className="flex items-center gap-3" data-testid="link-logo">
            <img src="/Fatima_logo.png" alt="Fatima Wardrobe Logo" className="h-10 md:h-12 w-auto object-contain" />
            <div className="flex flex-col items-center md:items-start leading-none text-[#2f2925]">
              <span className="block text-[15px] md:text-[19px] font-semibold tracking-[.34em]">
                FATIMA
              </span>
              <span className="mt-[2px] md:mt-1 block text-center md:text-left font-mono-ui text-[7px] md:text-[8px] tracking-[.48em]">
                WARDROBE
              </span>
            </div>
          </Link>"""

if re.search(header_logo_pattern, text):
    text = re.sub(header_logo_pattern, header_logo_repl, text)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Header logo updated to include text!")
else:
    print("Header logo pattern not found!")
