
import os
import re

file_path = r'c:\Users\theoc\OneDrive - Groupe ESIEA\Desktop\jeu_voyage\index.html'

with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# 1. Regex to catch document.getElementById('...').something
# We replace it with (document.getElementById('...') || {}).something
def safety_wrap_get_element(match):
    el_id = match.group(1)
    prop = match.group(2)
    return f"(document.getElementById('{el_id}') || {{}}).{prop}"

# Pattern for simple property access like .style, .innerText, .className, .innerHTML, .value
content = re.sub(r"document\.getElementById\(['\"](.*?)['\"]\)\.(style|innerText|className|innerHTML|value|focus|classList|onclick|src)", safety_wrap_get_element, content)

# 2. Safety wrap common variables already defined
vars_to_guard = ['gameTitle', 'scoreboard', 'container', 'btn', 'display', 'bar', 'timerProg', 'optionsDiv', 'inputZone', 'validZone', 'waitMsg', 'spinBtn', 'toView', 'fromView']
for v in vars_to_guard:
    # Only replace if followed by .something and not already guarded
    content = re.sub(rf"(?<!\()(?<!\w){v}\.(style|innerText|className|innerHTML|value|focus|classList|onclick|src)", rf"({v} || {{}}).\1", content)

# 3. Specific fix for transition logic in switchView
content = content.replace("toView.style.opacity = '1';", "(toView.style || {}).opacity = '1';")
content = content.replace("toView.style.transform = 'scale(1)';", "(toView.style || {}).transform = 'scale(1)';")
content = content.replace("fromView.style.opacity = '0';", "(fromView.style || {}).opacity = '0';")
content = content.replace("fromView.style.transform = 'scale(0.9)';", "(fromView.style || {}).transform = 'scale(0.9)';")

with open(file_path, 'w', encoding='utf-8-sig') as f:
    f.write(content)

print("Nuclear safety wrap applied to all UI elements.")
