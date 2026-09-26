import re

filepath = r'artifacts\fatima-wardrobe\src\App.tsx'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

old_render = r'<div className="mx-auto max-w-\[1440px\] px-5 md:px-12 py-6 overflow-x-auto scrollbar-hide">\s*<div className="flex items-start justify-center gap-6 md:gap-10 min-w-max mx-auto">\s*\{subCategories.map\(\(sub, idx\) => \(\s*<div key=\{idx\} className="flex flex-col items-center gap-3 w-20 md:w-24 cursor-pointer group">\s*<div className="w-20 h-20 md:w-24 md:h-24 rounded-full overflow-hidden border-2 border-transparent group-hover:border-\[#2f2925\] transition-colors p-\[2px\]">\s*<img src=\{sub\.img\} alt=\{sub\.name\} className="w-full h-full object-cover rounded-full" />\s*</div>\s*<span className="text-\[10px\] md:text-\[11px\] text-center leading-tight text-\[#776b61\] group-hover:text-\[#2f2925\]">\{sub\.name\}</span>\s*</div>\s*\)\)\}\s*</div>\s*</div>'

new_render = """{subCategories.length > 0 && (
        <div className="mx-auto max-w-[1440px] px-5 md:px-12 py-6 overflow-x-auto scrollbar-hide">
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
