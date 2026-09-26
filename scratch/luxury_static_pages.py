import re

filepath = r'artifacts\fatima-wardrobe\src\App.tsx'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

new_static_page = """
function StaticPage({ kind }: { kind: string }) {
  const content: Record<
    string,
    { eyebrow: string; title: string; body: string[] }
  > = {
    about: {
      eyebrow: "The house of Fatima",
      title: "Clothes with a life ahead of them.",
      body: [
        "Fatima Wardrobe began with a simple question: what would it mean to make a Pakistani wardrobe that feels as good on its hundredth wear as its first?",
        "We work from Lahore with a small circle of makers, printers and embroiderers. The result is clothing with a sense of place, but no fixed occasion - pieces for the full, ordinary, beautiful span of a day.",
        "We care about cloth you can feel, colour that grows richer with time, and design that leaves room for you in it.",
      ],
    },
    contact: {
      eyebrow: "Come say hello",
      title: "We are here to help.",
      body: [
        "For questions about an order, sizing, styling or simply a piece you cannot stop thinking about, write to us.",
        "hello@fatimawardrobe.pk",
        "Mon-Sat 10:00-18:00 PKT | +92 300 123 4567",
      ],
    },
    shipping: {
      eyebrow: "The practical bit",
      title: "Delivery, considered.",
      body: [
        "Orders are carefully packed in Lahore and delivered across Pakistan within 3-5 working days.",
        "Delivery is PKR 250 on orders below PKR 5,000, and complimentary above that threshold. You will receive a message when your parcel is on its way.",
      ],
    },
    returns: {
      eyebrow: "If it is not quite right",
      title: "Returns made simple.",
      body: [
        "You may request a return within 7 days of delivery, provided the piece is unworn, unwashed and has its original tags attached.",
        "Start a return by writing to hello@fatimawardrobe.pk with your order number. Sale and made-to-order pieces are final sale.",
      ],
    },
    "size-guide": {
      eyebrow: "Find your fit",
      title: "Your shape, your way.",
      body: [
        "Our ready-to-wear pieces follow a relaxed Pakistani fit. If you prefer a closer line, we recommend sizing down.",
        "For specific measurements, write to hello@fatimawardrobe.pk and our team will help you choose. Unstitched sizes are listed as fabric cuts.",
      ],
    },
  };
  const c = content[kind] || content.about;
  return (
    <div className="relative bg-[#f6f1e8] min-h-[100dvh] pb-24">
      {/* Luxurious Hero Header */}
      <div className="w-full h-[35vh] min-h-[300px] relative overflow-hidden">
        <img src="/images/lux_lawn_1_1790430964918.jpg" alt="Client services" className="absolute inset-0 w-full h-full object-cover object-[center_35%]" />
        <div className="absolute inset-0 bg-gradient-to-t from-[#2f2925]/90 to-[#2f2925]/40" />
        <div className="absolute inset-0 flex flex-col items-center justify-center text-[#f8f1e7] z-10 px-5 text-center">
           <h1 className="font-display text-5xl md:text-7xl tracking-wide mb-2 reveal">Client Services</h1>
           <p className="eyebrow tracking-[0.25em] text-[#d2c6ba] reveal" style={{ animationDelay: '0.1s' }}>We are here to assist you</p>
        </div>
      </div>

      <div className="mx-auto max-w-[1200px] px-5 py-12 md:py-20 flex flex-col md:flex-row gap-12 md:gap-20 relative">
        
        {/* Luxury Sticky Sidebar */}
        <aside className="w-full md:w-[260px] shrink-0">
          <div className="md:sticky md:top-[120px]">
            <p className="eyebrow text-[#a74636] mb-8 tracking-[0.2em] border-b border-[#ded2c4] pb-4 uppercase">Help & Info</p>
            <ul className="flex flex-row md:flex-col gap-6 md:gap-5 overflow-x-auto whitespace-nowrap scrollbar-hide pb-4 md:pb-0">
              {[
                { label: "Our Story", href: "/about", key: "about" },
                { label: "Shipping", href: "/shipping", key: "shipping" },
                { label: "Returns", href: "/returns", key: "returns" },
                { label: "Size Guide", href: "/size-guide", key: "size-guide" },
                { label: "Contact", href: "/contact", key: "contact" }
              ].map(link => (
                <li key={link.key}>
                   <Link 
                     href={link.href} 
                     className={`flex items-center gap-3 text-[12px] tracking-[0.15em] uppercase transition-all duration-300 ${kind === link.key ? "text-[#2f2925] font-semibold" : "text-[#9c8c7d] hover:text-[#a74636]"}`}
                   >
                     {kind === link.key && <span className="w-3 h-[2px] bg-[#a74636]" />}
                     {link.label}
                   </Link>
                </li>
              ))}
            </ul>
          </div>
        </aside>
        
        {/* Content Area */}
        <div className="flex-1 max-w-2xl reveal" style={{ animationDelay: '0.2s' }}>
          <p className="eyebrow text-[#9c8c7d] tracking-[0.15em] mb-4">{c.eyebrow}</p>
          <h2 className="font-display text-4xl md:text-5xl text-[#2f2925] leading-[1.1]">
            {c.title}
          </h2>
          <div className="mt-10 space-y-8">
            {c.body.map((p, i) => (
              <p
                key={p}
                className="text-[16px] leading-8 text-[#776b61] font-light"
              >
                {p}
              </p>
            ))}
          </div>
          
          <div className="mt-20 pt-16 border-t border-[#ded2c4] grid grid-cols-1 sm:grid-cols-2 gap-8 md:gap-12 items-center">
            <img
              src="/images/lux_kurta_1_1790430926797.jpg"
              alt="Fatima Wardrobe editorial"
              className="aspect-[3/4] object-cover object-top w-full shadow-soft"
            />
            <div className="flex flex-col">
               <h3 className="font-display text-2xl text-[#2f2925] mb-4">Dedicated Support</h3>
               <p className="text-[#776b61] text-[15px] leading-7 font-light mb-8">
                 Our client care team in Lahore is available to assist with styling advice, detailed product information, and delivery queries.
               </p>
               <Link href="/contact" className="text-[11px] font-medium uppercase tracking-[0.2em] text-[#a74636] border-b border-[#a74636] w-fit pb-1 hover:text-[#2f2925] hover:border-[#2f2925] transition-colors">
                 Get in touch
               </Link>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
"""

pattern = r'function StaticPage\(\{ kind \}: \{ kind: string \}\) \{[\s\S]*?\}\nfunction WishlistPage'
replacement = new_static_page.strip() + '\nfunction WishlistPage'

if re.search(pattern, text):
    text = re.sub(pattern, replacement, text)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)
    print("StaticPage replaced successfully with ultra luxury version!")
else:
    print("Could not find StaticPage component.")
