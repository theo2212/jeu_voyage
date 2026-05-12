
import os
import re

file_path = r'c:\Users\theoc\OneDrive - Groupe ESIEA\Desktop\jeu_voyage\index.html'

with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# 1. Fix the invalid variable names (dashes to underscores)
# Pattern: const el([a-z0-9-]+) = document.getElementById('\1')
def fix_var_names(match):
    full_match = match.group(0)
    var_name = match.group(1)
    new_var_name = var_name.replace('-', '_')
    return full_match.replace(f'el{var_name}', f'el_{new_var_name}')

content = re.sub(r"const el([a-z0-9-]+) = document\.getElementById\('\1'\)", fix_var_names, content)
# Also fix the usages
content = re.sub(r"if\(el([a-z0-9-]+)\) el\1\.style", lambda m: f"if(el_{m.group(1).replace('-', '_')}) el_{m.group(1).replace('-', '_')}.style", content)

# 2. Fix the double if on line 1988
content = content.replace("if (bar) if(bar && bar.style) bar.style.width", "if (bar && bar.style) bar.style.width")

# 3. Final sanity check for any other dashes in variable names starting with el
content = re.sub(r"el([a-z0-9]+)-([a-z0-9-]+)", r"el\1_\2", content)

with open(file_path, 'w', encoding='utf-8-sig') as f:
    f.write(content)

print("Fixed invalid variable names and cleaned up syntax.")
