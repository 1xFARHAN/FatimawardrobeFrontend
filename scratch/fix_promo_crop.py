import re

filepath = r'artifacts\fatima-wardrobe\src\App.tsx'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

pattern = r'src="/images/hero-luxury-courtyard\.png"\s*alt="Gulbahar collection"\s*className="absolute inset-0 h-full w-full object-cover object-top opacity-100"'
repl = r'src="/images/hero-luxury-courtyard.png"\n        alt="Gulbahar collection"\n        className="absolute inset-0 h-full w-full object-cover object-right md:object-top opacity-100"'

text = re.sub(pattern, repl, text)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

print("Promo tile crop fixed!")
