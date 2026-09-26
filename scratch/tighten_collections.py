import re

filepath = r'artifacts\fatima-wardrobe\src\App.tsx'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

pattern = r'\{/\* Editorial Layout \*/\}(.*?)\}\)\}\s*</div\>'

repl = """{/* Clean Grid Layout */}
      <div className="mx-auto max-w-[1440px] px-5 py-12 md:px-12 md:py-24">
        <div className="grid gap-x-8 gap-y-16 md:grid-cols-2 lg:grid-cols-3">
          {collections.map((c, i) => (
            <Link
              href={`/collection/${c.slug}`}
              className="group flex flex-col"
              key={c.slug}
              data-testid={`link-collection-${c.slug}`}
            >
              <div className="overflow-hidden relative bg-[#ebe1d5]">
                <img
                  src={c.image}
                  alt={c.name}
                  className={`aspect-[3/4] w-full object-cover transition duration-[1.5s] group-hover:scale-105 ${c.image.includes('courtyard') ? 'object-right' : 'object-top'}`}
                />
                <div className="absolute inset-0 bg-black/0 group-hover:bg-black/5 transition duration-700" />
              </div>
              
              <div className="mt-6 flex flex-col text-left">
                <p className="eyebrow text-[#a74636] mb-3 tracking-[0.2em]">{c.kicker}</p>
                <h2 className="font-display text-4xl text-[#2f2925] mb-4 group-hover:text-[#a74636] transition-colors">{c.name}</h2>
                <div className="w-12 h-[1px] bg-[#a74636] mb-5 transition-all duration-500 group-hover:w-24" />
                <p className="text-sm leading-6 text-[#776b61] mb-6 line-clamp-2">
                  {c.description}
                </p>
                <div className="inline-flex items-center gap-3 text-[11px] uppercase tracking-[0.2em] text-[#2f2925] group-hover:text-[#a74636] transition-colors">
                  <span>Explore</span>
                  <ArrowRight size={14} strokeWidth={1.5} className="transform transition-transform duration-500 group-hover:translate-x-1" />
                </div>
              </div>
            </Link>
          ))}
        </div>"""

if re.search(pattern, text, re.DOTALL):
    text = re.sub(pattern, repl, text, flags=re.DOTALL)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Collections page grid layout applied!")
else:
    print("Pattern not found!")
