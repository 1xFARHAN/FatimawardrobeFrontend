import re

filepath_app = r'artifacts\fatima-wardrobe\src\App.tsx'

with open(filepath_app, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the className and add style
pattern = r'className=\{`absolute inset-0 h-full w-full object-cover opacity-90 \$\{item\.objectPosition \|\| "object-top"\}[\`]\}'
repl = 'className="absolute inset-0 h-full w-full object-cover opacity-90 object-top md:object-top" style={{ objectPosition: window.innerWidth < 768 && item.id === "hero-1" ? "85% top" : "" }}'

if re.search(pattern, text):
    text = re.sub(pattern, repl, text)
    with open(filepath_app, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Hero image position updated to inline style!")
else:
    print("Hero image pattern not found!")
