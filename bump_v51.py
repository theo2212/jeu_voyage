
import os
import re

file_path = r'c:\Users\theoc\OneDrive - Groupe ESIEA\Desktop\jeu_voyage\index.html'

with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# 1. Simplify over-engineered style accesses
# Handle ((obj && obj.style) ? obj.style : {}).prop = val  WITH  if(obj) obj.style.prop = val
content = re.sub(r"\(\((.*?) && \1\.style\) \? \1\.style : \{\}\)\.(\w+) = (.*?);", r"if(\1) \1.style.\2 = \3;", content)
# Handle ((obj && (obj || {}).style) ? (obj || {}).style : {}).display = 'flex';
content = re.sub(r"\(\((.*?) && \(\1 \|\| \{\}\)\.style\) \? \(\1 \|\| \{\}\)\.style : \{\}\)\.(\w+) = (.*?);", r"if(\1) \1.style.\2 = \3;", content)

# 2. Fix corrupted emojis
replacements = {
    "à¢Â Å’": "❌",
    "à°Å¸Å’ÂªïÂ¸Â ": "🌪️",
    "à°Å¸Å’Â¶ïÂ¸Â ": "🌶️",
    "à°Å¸â€ â€ ": "🔔",
    "à¢Â Â±ïÂ¸Â ": "🔄",
    "ðŸŽ“": "🎓"
}
for old, new in replacements.items():
    content = content.replace(old, new)

# 3. Bump version to V51
if "V50 ✨" in content:
    content = content.replace("V50 ✨", "V51 💎")
elif "V51 💎" not in content:
    # Just in case
    content = re.sub(r"V\d+ [^\s]+", "V51 💎", content, count=1)

with open(file_path, 'w', encoding='utf-8-sig') as f:
    f.write(content)

# Update sw.js as well
sw_path = r'c:\Users\theoc\OneDrive - Groupe ESIEA\Desktop\jeu_voyage\sw.js'
with open(sw_path, 'r', encoding='utf-8', errors='ignore') as f:
    sw_content = f.read()
if 'voyage-cache-v50' in sw_content:
    sw_content = sw_content.replace('voyage-cache-v50', 'voyage-cache-v51')
elif 'voyage-cache-v51' not in sw_content:
    sw_content = re.sub(r"voyage-cache-v\d+", "voyage-cache-v51", sw_content)

with open(sw_path, 'w', encoding='utf-8') as f:
    f.write(sw_content)

print("Project bumped to V51 and cleaned up properly.")
