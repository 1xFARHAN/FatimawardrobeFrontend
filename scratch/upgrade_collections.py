import re

filepath = r'artifacts\fatima-wardrobe\src\App.tsx'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

pattern = r'function CollectionsPage\(\) \{.*?(?=function StaticPage)'

repl = """function CollectionsPage() {
  return (
    <>
      <div className="relative min-h-[450px] md:min-h-[550px] overflow-hidden text-[#f8f1e7] bg-[#2f2925]">
        <img
          src="/images/ready-to-wear-editorial.png"
          alt="The Collections"
          className="absolute inset-0 h-full w-full object-cover object-top opacity-60"
        />
        <div className="absolute inset-0 bg-gradient-to-t from-[#2f2925]/90 via-[#2f2925]/30 to-transparent" />
        <div className="relative flex min-h-[450px] md:min-h-[550px] items-end px-5 pb-14 md:px-12 md:pb-20">
          <div className="max-w-2xl reveal">
            <p className="eyebrow text-[#f0e2d4] mb-4">Stories in cloth</p>
            <h1 className="font-display text-5xl md:text-7xl lg:text-[80px] leading-[0.9]">
              The Collections
            </h1>
            <p className="mt-6 text-sm tracking-wide text-[#cfc1b1] md:text-base leading-relaxed max-w-xl">
              Explore our curated editorials. From quiet everyday essentials to the opulence of our festive wear, each collection is a celebration of Pakistani heritage and meticulous craftsmanship.
            </p>
          </div>
        </div>
      </div>
      
      <div className="mx-auto max-w-[1440px] px-5 py-16 md:px-12 md:py-28">
        <div className="grid gap-x-8 gap-y-20 md:grid-cols-2">
          {collections.map((c, i) => (
            <Link
              href={`/collection/${c.slug}`}
              className={`${i % 2 ? "md:mt-32" : ""} group reveal`}
              key={c.slug}
              data-testid={`link-collection-${c.slug}`}
            >
              <div className="overflow-hidden relative bg-[#ebe1d5]">
                <img
                  src={c.image}
                  alt={c.name}
                  className="aspect-[4/5] w-full object-cover object-top transition duration-1000 group-hover:scale-[1.03]"
                />
                <div className="absolute inset-0 bg-black/0 group-hover:bg-black/5 transition duration-700" />
              </div>
              <div className="mt-6 flex flex-col md:flex-row md:items-baseline md:justify-between border-b border-[#ded2c4] pb-5 group-hover:border-[#2f2925] transition-colors">
                <div>
                  <p className="eyebrow text-[#a74636] mb-2">{c.kicker}</p>
                  <h2 className="font-display text-4xl text-[#2f2925] group-hover:text-[#a74636] transition-colors">{c.name}</h2>
                </div>
                <div className="mt-4 md:mt-0 opacity-0 transform translate-x-[-10px] group-hover:opacity-100 group-hover:translate-x-0 transition-all duration-500">
                  <ArrowRight size={20} className="text-[#a74636]" strokeWidth={1.5} />
                </div>
              </div>
              <p className="mt-5 max-w-md text-sm leading-7 text-[#776b61]">
                {c.description}
              </p>
            </Link>
          ))}
        </div>
      </div>
    </>
  );
}
"""

if re.search(pattern, text, re.DOTALL):
    text = re.sub(pattern, repl, text, flags=re.DOTALL)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Collections page updated successfully!")
else:
    print("Pattern not found!")
