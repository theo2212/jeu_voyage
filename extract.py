import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract CSS
style_match = re.search(r'<style>(.*?)</style>', html, flags=re.DOTALL)
if style_match:
    css_content = style_match.group(1)
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(css_content.strip() + '\n')
    # Replace in HTML
    html = html[:style_match.start()] + '<link rel="stylesheet" href="style.css">\n' + html[style_match.end():]

# Extract JS
script_match = re.search(r'<script>(.*?)</script>', html, flags=re.DOTALL)
if script_match:
    js_content = script_match.group(1)
    with open('app.js', 'w', encoding='utf-8') as f:
        f.write(js_content.strip() + '\n')
    # Replace in HTML
    html = html[:script_match.start()] + '<script src="app.js"></script>\n' + html[script_match.end():]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Extraction complete!')
