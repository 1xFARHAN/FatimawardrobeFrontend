import re

filepath = r'artifacts\fatima-wardrobe\src\App.tsx'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# Fix the ArrowRight class in CollectionsPage
pattern = r'<ArrowRight size=\{16\} strokeWidth=\{1\} className=\{`transform transition-transform duration-500 \$\{isEven \? \'group-hover:translate-x-2\' : \'group-hover:-translate-x-2 rotate-180\'\}`\} />'
repl = r'<ArrowRight size={16} strokeWidth={1} className={`transform transition-transform duration-500 group-hover:translate-x-2`} />'

text = re.sub(pattern, repl, text)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

print("Arrow fixed!")
