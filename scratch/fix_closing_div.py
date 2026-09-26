import re

filepath = r'artifacts\fatima-wardrobe\src\App.tsx'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace(
"""          ))}
        </div>
    </div>
  );
}
function StaticPage""",
"""          ))}
        </div>
      </div>
    </div>
  );
}
function StaticPage"""
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

print("Added missing closing div")
