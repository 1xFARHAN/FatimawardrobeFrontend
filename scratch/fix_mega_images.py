import re

filepath = r'artifacts\fatima-wardrobe\src\App.tsx'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# We need to change the Mega Menu img src logic.
# Current: src={allProducts[i * 2 % allProducts.length]?.images[0]}
# We want to find a product that matches the current mega menu category and subcategory.

new_img_logic = """
                    <div className="aspect-square w-full overflow-hidden bg-[#f0e2d4] mb-5">
                      <img 
                        src={
                          (allProducts.find(p => 
                            p.category.toLowerCase().replace(/-/g, ' ') === activeMega.toLowerCase().replace(/-/g, ' ') && 
                            p.subcategory.toLowerCase() === item.toLowerCase()
                          ) || allProducts.find(p => 
                            p.category.toLowerCase().replace(/-/g, ' ') === activeMega.toLowerCase().replace(/-/g, ' ')
                          ) || allProducts[i % allProducts.length])?.images[0]
                        } 
                        alt={item} 
                        className="w-full h-full object-cover object-top transition duration-700 group-hover:scale-[1.03]"
                      />
"""

# Replace the block
pattern = r'<div className="aspect-square w-full overflow-hidden bg-\[#f0e2d4\] mb-5">\s*<img\s*src=\{allProducts\[i \* 2 % allProducts\.length\]\?\.images\[0\]\}\s*alt=\{item\}\s*className="w-full h-full object-cover transition duration-700 group-hover:scale-\[1\.03\]"\s*/>'

if re.search(pattern, text):
    text = re.sub(pattern, new_img_logic.strip(), text)
else:
    print("Pattern not found! Trying a more relaxed pattern...")
    # fallback
    pattern = r'<div className="aspect-square w-full overflow-hidden bg-\[#f0e2d4\] mb-5">[\s\S]*?/>'
    text = re.sub(pattern, new_img_logic.strip(), text, count=1)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

print("Mega menu images now respect the category and subcategory!")
