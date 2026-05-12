
import os
file_path = r'c:\Users\theoc\OneDrive - Groupe ESIEA\Desktop\jeu_voyage\index.html'
with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# 1. Fix the terrible syntax errors created by the previous script
# Pattern: if((document.getElementById('...')) document.getElementById('...') ? document.getElementById('...')) document.getElementById('...').style : {}).display = '...'
# We replace with a clean version: const el = document.getElementById('...'); if(el) el.style.display = '...';

# I'll use a regex to catch these messed up lines
import re
pattern = r"if\(\(document\.getElementById\('(.*?)'\)\)\s*document\.getElementById\('\1'\)\s*\?\s*document\.getElementById\('\1'\)\)\s*document\.getElementById\('\1'\)\.style\s*:\s*\{\}\)\.display\s*=\s*'(.*?)';"
content = re.sub(pattern, r"const el\1 = document.getElementById('\1'); if(el\1) el\1.style.display = '\2';", content)

# Also fix the one for timerProg and others
content = re.sub(r"if\(\((.*?)\s*&&\s*\1\.style\)\s*\?\s*\1\.style\s*:\s*\{\}\)\.display\s*=\s*'(.*?)';", r"if(\1 && \1.style) \1.style.display = '\2';", content)
content = re.sub(r"\(\((.*?)\s*&&\s*\1\.style\)\s*\?\s*\1\.style\s*:\s*\{\}\)\.width\s*=\s*(.*?);", r"if(\1 && \1.style) \1.style.width = \2;", content)

# 2. Fix the specific corrupted line in showQuizPodium seen by the subagent
content = re.sub(r"\(document\.getElementById\('(.*?)'\)\s*\?\s*document\.getElementById\('\1'\)\.style\s*:\s*\{\}\)\.display\s*=\s*'(.*?)';", r"const el\1 = document.getElementById('\1'); if(el\1) el\1.style.display = '\2';", content)

with open(file_path, 'w', encoding='utf-8-sig') as f:
    f.write(content)

print("Cleaned up syntax errors.")
