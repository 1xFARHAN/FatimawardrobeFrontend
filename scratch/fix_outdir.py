import re

filepath = r'artifacts\fatima-wardrobe\vite.config.ts'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

pattern = r"outDir: path\.resolve\(import\.meta\.dirname, 'dist/public'\)"
repl = "outDir: path.resolve(import.meta.dirname, 'dist')"

if re.search(pattern, text):
    text = re.sub(pattern, repl, text)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated outDir to dist in vite.config.ts")
else:
    print("outDir pattern not found!")
