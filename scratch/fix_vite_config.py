import re

filepath = r'artifacts\fatima-wardrobe\vite.config.ts'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace strict port check
pattern_port = r'const rawPort = process.env.PORT;\n\nif \(!rawPort\) \{\n  throw new Error\(\n    \'PORT environment variable is required but was not provided.\',\n  \);\n\}\n\nconst port = Number\(rawPort\);\n\nif \(Number.isNaN\(port\) \|\| port <= 0\) \{\n  throw new Error\(`Invalid PORT value: "\$\{rawPort\}"`\);\n\}'
replacement_port = 'const port = Number(process.env.PORT) || 3000;'

if re.search(pattern_port, text, re.DOTALL):
    text = re.sub(pattern_port, replacement_port, text, flags=re.DOTALL)
else:
    print("Port check not found!")

# Replace strict basePath check
pattern_base = r'const basePath = process.env.BASE_PATH;\n\nif \(!basePath\) \{\n  throw new Error\(\n    \'BASE_PATH environment variable is required but was not provided.\',\n  \);\n\}'
replacement_base = 'const basePath = process.env.BASE_PATH || "/";'

if re.search(pattern_base, text, re.DOTALL):
    text = re.sub(pattern_base, replacement_base, text, flags=re.DOTALL)
else:
    print("BasePath check not found!")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

print("vite.config.ts fixed for Vercel deployment!")
