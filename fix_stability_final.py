
import os
import re

file_path = r'c:\Users\theoc\OneDrive - Groupe ESIEA\Desktop\jeu_voyage\index.html'

# We read the file in binary mode to ensure we handle the BOM correctly
with open(file_path, 'rb') as f:
    raw_content = f.read()

# Remove UTF-8 BOM if present
if raw_content.startswith(b'\xef\xbb\xbf'):
    raw_content = raw_content[3:]

content = raw_content.decode('utf-8', errors='ignore')

# 1. Fix infinite recursion in beginGame()
old_begin_game_logic = """                if (currentGame === 'chaos') {
                    gameTitle.innerText = "Jeu Surprise ! 🌪️";
                    gameTitle.className = 'txt-boire';
                } else {"""

# The subagent identified a recursive call in beginGame() if syncMode === 'online'
# I need to find that specific block
recursive_pattern = r"if \(syncMode === 'online'\) \{[\s\S]*?beginGame\(\);[\s\S]*?return;[\s\S]*?\}"
new_online_logic = """if (syncMode === 'online') {
                players = roomPlayers.map(p => ({
                    id: p.id || Math.random().toString(36).substr(2, 9),
                    name: p.name,
                    score: 0,
                    coins: 0,
                    inventory: []
                }));
            }"""

content = re.sub(recursive_pattern, new_online_logic, content)

# 2. Fix saveToLocalStorage -> saveState
content = content.replace("saveToLocalStorage();", "saveState();")

# 3. Ensure the script tag starts cleanly (remove any spaces or weird chars after <script>)
content = re.sub(r'<script>\s*', '<script>\n', content)

with open(file_path, 'w', encoding='utf-8-sig') as f:
    f.write(content)

print("Applied stability fixes: removed BOM, fixed recursion, and corrected function names.")
