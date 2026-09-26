import re

filepath = r'artifacts\fatima-wardrobe\src\App.tsx'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace Header Logo
header_logo_pattern = r'<Link\s+href="/"\s+className="flex flex-col items-center justify-center -translate-y-\[2px\]"\s*>\s*<div className="text-\[22px\] font-semibold tracking-\[\.3em\] text-\[#2f2925\]">\s*FATIMA\s*</div>\s*<div className="mt-\[2px\] font-mono-ui text-\[8\.5px\] tracking-\[\.45em\] text-\[#9c8c7d\]">\s*WARDROBE\s*</div>\s*</Link>'
header_logo_repl = '<Link href="/" className="flex items-center justify-center">\n              <img src="/Fatima_logo.png" alt="Fatima Wardrobe" className="h-14 md:h-16 w-auto object-contain" />\n            </Link>'
text = re.sub(header_logo_pattern, header_logo_repl, text)

# Replace Mobile Menu Logo
mobile_logo_pattern = r'<Link\s+href="/"\s+onClick=\{close\}\s+className="text-\[16px\] font-semibold tracking-\[\.3em\]"\s*>\s*FATIMA / WARDROBE\s*</Link>'
mobile_logo_repl = '<Link href="/" onClick={close} className="flex items-center">\n          <img src="/Fatima_logo.png" alt="Fatima Wardrobe" className="h-10 w-auto object-contain" />\n        </Link>'
text = re.sub(mobile_logo_pattern, mobile_logo_repl, text)

# Replace Footer Logo
footer_logo_pattern = r'<div className="text-2xl font-semibold tracking-\[\.35em\]">\s*FATIMA\s*</div>\s*<div className="mt-2 font-mono-ui text-\[9px\] tracking-\[\.48em\]">\s*WARDROBE\s*</div>'
footer_logo_repl = '<img src="/Fatima_logo.png" alt="Fatima Wardrobe" className="h-16 w-auto object-contain brightness-0 invert opacity-90" />'
text = re.sub(footer_logo_pattern, footer_logo_repl, text)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

print("Logos replaced successfully!")
