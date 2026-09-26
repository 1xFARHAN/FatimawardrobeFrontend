import re

filepath = r'artifacts\fatima-wardrobe\src\App.tsx'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# Make image boxes smaller (w-[45%] lg:w-[40%]) and text boxes slightly larger to balance
pattern = r'<div className="w-full md:w-\[55%\] lg:w-\[60%\] overflow-hidden relative bg-\[#ebe1d5\]">\s*<img\s*src=\{c\.image\}\s*alt=\{c\.name\}\s*className="aspect-\[4/5\] md:aspect-\[3/4\] w-full object-cover object-top transition duration-\[1\.5s\] group-hover:scale-105"\s*/>'

repl = """<div className="w-full md:w-[45%] lg:w-[40%] overflow-hidden relative bg-[#ebe1d5]">
                <img
                  src={c.image}
                  alt={c.name}
                  className={`aspect-[4/5] md:aspect-[3/4] w-full object-cover transition duration-[1.5s] group-hover:scale-105 ${c.image.includes('courtyard') ? 'object-right' : 'object-top'}`}
                />"""

text = re.sub(pattern, repl, text, flags=re.DOTALL)

# Update text block width from md:w-[45%] lg:w-[40%] to md:w-[45%] lg:w-[50%] to take up the remaining space
pattern2 = r'<div className=\{`w-full md:w-\[45%\] lg:w-\[40%\] flex flex-col justify-center text-center'
repl2 = r'<div className={`w-full md:w-[45%] lg:w-[50%] flex flex-col justify-center text-center'
text = re.sub(pattern2, repl2, text)

# Also reduce the overall width of the content a bit by adding max-w-[1200px] instead of 1440px to make things feel more compact
pattern3 = r'<div className="mx-auto max-w-\[1440px\] px-5 py-12 md:px-12 md:py-20 flex flex-col gap-16 md:gap-24">'
repl3 = r'<div className="mx-auto max-w-[1200px] px-5 py-12 md:px-12 md:py-20 flex flex-col gap-16 md:gap-24">'
text = re.sub(pattern3, repl3, text)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

print("Image sizes reduced and crop fixed!")
