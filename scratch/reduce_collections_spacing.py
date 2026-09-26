import re

filepath = r'artifacts\fatima-wardrobe\src\App.tsx'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# Reduce outer padding and gap between collections
text = text.replace(
    'className="mx-auto max-w-[1440px] px-5 py-24 md:px-16 md:py-40 flex flex-col gap-32 md:gap-48"',
    'className="mx-auto max-w-[1440px] px-5 py-12 md:px-12 md:py-20 flex flex-col gap-16 md:gap-24"'
)

# Reduce gap between image and text in each collection
pattern = r'className=\{`group flex flex-col \$\{isEven \? \'md:flex-row\' : \'md:flex-row-reverse\'\} items-center gap-12 md:gap-24`\}'
repl = r'className={`group flex flex-col ${isEven ? \'md:flex-row\' : \'md:flex-row-reverse\'} items-center gap-8 md:gap-16`}'
text = re.sub(pattern, repl, text)

# Reduce image size slightly so it doesn't look too massive with reduced spacing
# Actually, keeping the width the same (w-[55%] md:w-[60%]) is fine, but maybe reduce to 50%?
# Let's leave width alone first, just spacing.

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

print("Spacing reduced!")
