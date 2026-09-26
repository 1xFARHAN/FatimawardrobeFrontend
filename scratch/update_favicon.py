import re

filepath = r'artifacts\fatima-wardrobe\index.html'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace favicon
text = re.sub(r'<link rel="icon".*?>', '<link rel="icon" type="image/png" href="/Fatima_logo.png" />', text)

# Replace description
text = re.sub(r'Fatima Wardrobe \\?" built on Replit. Update this description to reflect the app.', 'A modern Pakistani label for clothes with a life ahead of them.', text)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

print("Favicon and metadata updated!")
