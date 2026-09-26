import re

filepath = r'artifacts\fatima-wardrobe\src\App.tsx'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

header_logo_pattern = r'<Link\s+href="/"\s+className="leading-none text-\[#2f2925\]"\s+data-testid="link-logo"\s*>\s*<span className="block text-\[19px\] font-semibold tracking-\[\.34em\]">\s*FATIMA\s*</span>\s*<span className="mt-1 block text-center font-mono-ui text-\[8px\] tracking-\[\.48em\]">\s*WARDROBE\s*</span>\s*</Link>'
header_logo_repl = '<Link href="/" className="flex items-center justify-center" data-testid="link-logo">\n            <img src="/Fatima_logo.png" alt="Fatima Wardrobe" className="h-14 md:h-16 w-auto object-contain" />\n          </Link>'

if re.search(header_logo_pattern, text):
    text = re.sub(header_logo_pattern, header_logo_repl, text)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Header logo replaced successfully!")
else:
    print("Header logo pattern not found!")
