import re

filepath = r'artifacts\fatima-wardrobe\src\App.tsx'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update navigation links to be uppercase
nav_pattern = r'<nav\s*className="hidden items-center gap-7 lg:flex"\s*aria-label="Primary navigation"\s*>\s*\{navigation\.links\.map\(\(link\) => \(\s*<div\s*key=\{link\.href\}\s*onMouseEnter=\{\(\) =>\s*setActiveMega\(link\.menu \? link\.label : null\)\s*\}\s*className="relative py-8"\s*>\s*<Link\s*href=\{link\.href\}\s*className=\{`eyebrow transition-colors hover:text-\[#a74636\] \$\{link\.label === "Sale" \? "text-\[#a74636\]" : ""\}`\}\s*data-testid=\{`link-nav-\$\{link\.label\.toLowerCase\(\)\.replaceAll\(" ", "-"\)\}`\}\s*>\s*\{link\.label\}\s*</Link>\s*</div>\s*\)\}\s*</nav>'

nav_replacement = """<nav
            className="hidden items-center gap-8 lg:flex"
            aria-label="Primary navigation"
          >
            {navigation.links.map((link) => (
              <div
                key={link.href}
                onMouseEnter={() => setActiveMega(link.label)}
                className="relative py-8"
              >
                <Link
                  href={link.href}
                  className={`text-[12px] font-medium uppercase tracking-[0.1em] transition-colors hover:text-[#a74636] ${link.label === "Sale" ? "text-[#a74636]" : "text-[#2f2925]"}`}
                  data-testid={`link-nav-${link.label.toLowerCase().replaceAll(" ", "-")}`}
                >
                  {link.label}
                </Link>
              </div>
            ))}
          </nav>"""
text = re.sub(nav_pattern, nav_replacement, text, flags=re.DOTALL)

# 2. Update the Mega Menu to use image thumbnails
mega_pattern = r'\{activeMega && \(\s*<div\s*onMouseLeave=\{\(\) => setActiveMega\(null\)\}\s*className="absolute left-0 right-0 border-t border-\[#ded2c4\] bg-\[#f6f1e8\] shadow-\[0_18px_30px_rgba\(54,36,24,\.08\)\]"\s*>\s*<div className="mx-auto flex max-w-\[1440px\] gap-20 px-12 py-8">.*?</div>\s*</div>\s*\)\}'

mega_replacement = """{activeMega && (
          <div
            onMouseLeave={() => setActiveMega(null)}
            className="absolute left-0 right-0 border-t border-[#ded2c4] bg-[#ffffff] shadow-xl transition-opacity duration-200"
          >
            <div className="mx-auto max-w-[1200px] px-8 py-10">
              <div className="flex items-start justify-center gap-6">
                {(
                  navigation.links.find((x) => x.label === activeMega)?.menu ||
                  ["Ready to wear", "Unstitched", "Accessories", "Sale"]
                ).slice(0, 4).map((item, i) => (
                  <button
                    key={item}
                    onClick={() => navigate(menuHref(activeMega, item))}
                    className="group text-center flex flex-col items-center w-[220px]"
                  >
                    <div className="aspect-square w-full overflow-hidden bg-[#f0e2d4] mb-5">
                      <img 
                        src={allProducts[i * 2 % allProducts.length]?.images[0]} 
                        alt={item} 
                        className="w-full h-full object-cover transition duration-700 group-hover:scale-[1.03]"
                      />
                    </div>
                    <span className="text-[13px] font-medium uppercase tracking-[0.1em] text-[#2f2925] group-hover:text-[#a74636]">
                      {item}
                    </span>
                  </button>
                ))}
              </div>
            </div>
          </div>
        )}"""

text = re.sub(mega_pattern, mega_replacement, text, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

print("Updates applied")
