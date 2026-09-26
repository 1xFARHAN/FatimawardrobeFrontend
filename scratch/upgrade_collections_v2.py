import re

filepath = r'artifacts\fatima-wardrobe\src\App.tsx'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

pattern = r'function CollectionsPage\(\) \{.*?(?=function StaticPage)'

repl = """function CollectionsPage() {
  return (
    <div className="bg-[#fcfbf9]">
      {/* Hero Section - No Model, Fabric Flatlay */}
      <div className="relative min-h-[500px] md:min-h-[700px] overflow-hidden bg-[#2f2925] flex items-center justify-center">
        <img
          src="/images/luxury_unstitched_flatlay_1790427695988.jpg"
          alt="The Collections"
          className="absolute inset-0 h-full w-full object-cover opacity-50 mix-blend-overlay"
        />
        <div className="absolute inset-0 bg-[#2f2925]/40" />
        <div className="relative text-center px-5 reveal z-10">
          <p className="eyebrow text-[#cfc1b1] mb-6 tracking-[0.3em]">The Archives</p>
          <h1 className="font-display text-6xl md:text-8xl lg:text-[110px] text-[#f8f1e7] leading-none">
            Collections
          </h1>
          <div className="w-16 h-[1px] bg-[#cfc1b1] mx-auto mt-10 mb-8" />
          <p className="text-xs tracking-[0.25em] text-[#cfc1b1] uppercase">
            Stories Woven In Cloth
          </p>
        </div>
      </div>
      
      {/* Editorial Layout */}
      <div className="mx-auto max-w-[1440px] px-5 py-24 md:px-16 md:py-40 flex flex-col gap-32 md:gap-48">
        {collections.map((c, i) => {
          const isEven = i % 2 === 0;
          return (
            <Link
              href={`/collection/${c.slug}`}
              className={`group flex flex-col ${isEven ? 'md:flex-row' : 'md:flex-row-reverse'} items-center gap-12 md:gap-24`}
              key={c.slug}
              data-testid={`link-collection-${c.slug}`}
            >
              {/* Image Block */}
              <div className="w-full md:w-[55%] lg:w-[60%] overflow-hidden relative bg-[#ebe1d5]">
                <img
                  src={c.image}
                  alt={c.name}
                  className="aspect-[4/5] md:aspect-[3/4] w-full object-cover object-top transition duration-[1.5s] group-hover:scale-105"
                />
              </div>
              
              {/* Text Block */}
              <div className={`w-full md:w-[45%] lg:w-[40%] flex flex-col justify-center text-center ${isEven ? 'md:text-left' : 'md:text-right'} reveal`}>
                <p className="eyebrow text-[#a74636] mb-5 tracking-[0.25em]">{c.kicker}</p>
                <h2 className="font-display text-5xl md:text-7xl lg:text-[80px] text-[#2f2925] mb-8 leading-[0.9]">{c.name}</h2>
                <div className={`w-12 h-[1px] bg-[#a74636] mx-auto ${isEven ? 'md:mx-0' : 'md:ml-auto md:mr-0'} mb-10 transition-all duration-700 group-hover:w-24`} />
                <p className={`text-base leading-8 text-[#776b61] mb-12 max-w-md mx-auto ${isEven ? 'md:mx-0' : 'md:ml-auto md:mr-0'}`}>
                  {c.description}
                </p>
                <div className={`inline-flex items-center gap-4 text-xs uppercase tracking-[0.2em] text-[#2f2925] group-hover:text-[#a74636] transition-colors justify-center ${isEven ? 'md:justify-start' : 'md:justify-end'}`}>
                  <span>Explore Collection</span>
                  <ArrowRight size={16} strokeWidth={1} className={`transform transition-transform duration-500 ${isEven ? 'group-hover:translate-x-2' : 'group-hover:-translate-x-2 rotate-180'}`} />
                </div>
              </div>
            </Link>
          );
        })}
      </div>
    </div>
  );
}
"""

if re.search(pattern, text, re.DOTALL):
    text = re.sub(pattern, repl, text, flags=re.DOTALL)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Collections page upgraded to ultra-luxury successfully!")
else:
    print("Pattern not found!")
