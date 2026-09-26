import re

filepath = r'artifacts\fatima-wardrobe\src\App.tsx'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# Fix CollectionsPage image
pattern1 = r'className="aspect-\[1\.15\] w-full object-cover transition duration-700 group-hover:scale-105"'
repl1 = 'className="aspect-[1.15] w-full object-cover object-top transition duration-700 group-hover:scale-105"'
text = re.sub(pattern1, repl1, text)

# Fix ProductCard image
pattern2 = r'className="aspect-\[3/4\] w-full object-cover transition duration-500 group-hover:scale-\[1\.03\]"'
repl2 = 'className="aspect-[3/4] w-full object-cover object-top transition duration-500 group-hover:scale-[1.03]"'
text = re.sub(pattern2, repl2, text)

# Fix Category block image (Editorial)
pattern3 = r'className="aspect-\[\.84\] w-full object-cover transition duration-700 group-hover:scale-\[1\.04\]"'
repl3 = 'className="aspect-[.84] w-full object-cover object-top transition duration-700 group-hover:scale-[1.04]"'
text = re.sub(pattern3, repl3, text)

# Fix Product Detail image
pattern4 = r'className="aspect-\[\.82\] w-full object-cover md:aspect-\[\.78\]"'
repl4 = 'className="aspect-[.82] w-full object-cover object-top md:aspect-[.78]"'
text = re.sub(pattern4, repl4, text)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

print("All missing object-top classes added!")
