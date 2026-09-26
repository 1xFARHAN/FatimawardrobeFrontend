import re

filepath = r'artifacts\fatima-wardrobe\src\App.tsx'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

pattern = r'const bagCount = store\.bag\.reduce\(\(sum, item\) => sum \+ item\.quantity, 0\);'
repl = 'const bagCount = store.bag.reduce((sum, item) => allProducts.some(p => p.id === item.id) ? sum + item.quantity : sum, 0);'

if re.search(pattern, text):
    text = re.sub(pattern, repl, text)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Fixed bagCount bug.")
else:
    print("Could not find bagCount definition!")
