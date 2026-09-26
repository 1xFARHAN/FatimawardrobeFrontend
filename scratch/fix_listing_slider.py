import re

filepath = r'artifacts\fatima-wardrobe\src\App.tsx'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace subCategories definition
old_subcats = r'const subCategories = useMemo\(\(\) => \{\n\s*return \[\n\s*\{ name: "Studio: The New Formal".*?\n\s*\].filter\(\(x\) => x\.img\);\n\s*\}, \[\]\);'
new_subcats = """const subCategories = useMemo(() => {
    if (mode !== "new-in" && title !== "New in") return [];
    return [
      { name: "Ready to Wear", href: "/ready-to-wear", img: allProducts.find(p => p.category === "Ready to Wear")?.images[0] || allProducts[0]?.images[0] },
      { name: "Unstitched", href: "/unstitched", img: allProducts.find(p => p.category === "Unstitched")?.images[0] || allProducts[1]?.images[0] },
      { name: "Accessories", href: "/accessories", img: allProducts.find(p => p.category === "Accessories")?.images[0] || allProducts[2]?.images[0] },
      { name: "Sale", href: "/sale", img: allProducts.find(p => p.category === "Sale")?.images[0] || allProducts[3]?.images[0] }
    ].filter((x) => x.img);
  }, [mode, title]);"""

if re.search(old_subcats, text, re.DOTALL):
    text = re.sub(old_subcats, new_subcats, text, flags=re.DOTALL)
    print("Replaced subCategories definition.")
else:
    print("Could not find subCategories definition!")

# Replace subCategories rendering
old_render = r'<div className="w-full overflow-x-auto scrollbar-hide py-4 px-5 md:px-12 mb-6 border-b border-\[#ded2c4\]">\s*<div className="flex items-start justify-center gap-6 md:gap-10 min-w-max mx-auto">\s*\{subCategories.map\(\(sub, idx\) => \(\s*<div key=\{idx\} className="flex flex-col items-center gap-3 w-20 md:w-24 cursor-pointer group">\s*<div className="w-20 h-20 md:w-24 md:h-24 rounded-full overflow-hidden border-2 border-transparent group-hover:border-\[#2f2925\] transition-colors p-\[2px\]">\s*<img src=\{sub\.img\} alt=\{sub\.name\} className="w-full h-full object-cover rounded-full" />\s*</div>\s*<span className="text-\[10px\] md:text-\[11px\] text-center leading-tight text-\[#776b61\] group-hover:text-\[#2f2925\]">\{sub\.name\}</span>\s*</div>\s*\)\)\}\s*</div>\s*</div>'

new_render = """{subCategories.length > 0 && (
        <div className="w-full overflow-x-auto scrollbar-hide py-4 px-5 md:px-12 mb-6 border-b border-[#ded2c4]">
          <div className="flex items-start justify-center gap-6 md:gap-10 min-w-max mx-auto">
            {subCategories.map((sub, idx) => (
              <Link key={idx} href={sub.href || "/"} className="flex flex-col items-center gap-3 w-20 md:w-24 cursor-pointer group">
                <div className="w-20 h-20 md:w-24 md:h-24 rounded-full overflow-hidden border-2 border-transparent group-hover:border-[#2f2925] transition-colors p-[2px]">
                  <img src={sub.img} alt={sub.name} className="w-full h-full object-cover object-top rounded-full" />
                </div>
                <span className="text-[10px] md:text-[11px] text-center leading-tight text-[#776b61] group-hover:text-[#2f2925]">{sub.name}</span>
              </Link>
            ))}
          </div>
        </div>
      )}"""

if re.search(old_render, text, re.DOTALL):
    text = re.sub(old_render, new_render, text, flags=re.DOTALL)
    print("Replaced subCategories rendering.")
else:
    print("Could not find subCategories rendering!")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)
