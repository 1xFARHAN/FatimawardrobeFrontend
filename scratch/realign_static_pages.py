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
    <div className="mx-auto max-w-[1200px] px-5 py-20 md:px-12 md:py-32 flex flex-col md:flex-row gap-12 md:gap-24">
      <aside className="w-full md:w-48 shrink-0 border-b border-[#ded2c4] md:border-b-0 pb-10 md:pb-0">
        <p className="eyebrow text-[#a74636] mb-8">Help & Info</p>
        <ul className="flex flex-row md:flex-col gap-6 md:gap-5 overflow-x-auto whitespace-nowrap scrollbar-hide">
          {[
            { label: "Our Story", href: "/about", key: "about" },
            { label: "Shipping", href: "/shipping", key: "shipping" },
            { label: "Returns", href: "/returns", key: "returns" },
            { label: "Size Guide", href: "/size-guide", key: "size-guide" },
            { label: "Contact", href: "/contact", key: "contact" }
          ].map(link => (
            <li key={link.key}>
               <Link href={link.href} className={`block text-[14px] transition-colors hover:text-[#2f2925] ${kind === link.key ? "font-semibold text-[#2f2925]" : "text-[#776b61]"}`}>
                 {link.label}
               </Link>
            </li>
          ))}
        </ul>
      </aside>
      
      <div className="flex-1 max-w-2xl">
        <p className="eyebrow text-[#776b61]">{c.eyebrow}</p>
        <h1 className="mt-5 font-display text-5xl leading-[1.05] md:text-7xl">
          {c.title}
        </h1>
        {c.body.map((p, i) => (
          <p
            key={p}
            className={`max-w-xl text-[17px] leading-8 text-[#776b61] ${i === 0 ? "mt-10" : "mt-6"}`}
          >
            {p}
          </p>
        ))}
        
        <div className="mt-20 grid grid-cols-2 gap-3">
          <img
            src="/images/lux_kurta_1_1790430926797.jpg"
            alt="Fatima Wardrobe editorial"
            className="aspect-[.8] object-cover object-top w-full"
          />
          <img
            src="/images/lux_lawn_1_1790430964918.jpg"
            alt="Fatima Wardrobe detail"
            className="aspect-[.8] object-cover object-top w-full md:mt-16"
          />
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
    print("StaticPage replaced successfully!")
else:
    print("Could not find StaticPage component.")
