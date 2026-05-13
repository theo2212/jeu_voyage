
import os

file_path = r'c:\Users\theoc\OneDrive - Groupe ESIEA\Desktop\jeu_voyage\index.html'

with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# 1. Fix updateScoreboard
old_scoreboard = """        function updateScoreboard() {
            const scoreboard = document.getElementById('scoreboard');
            if (players.length === 0) {
                scoreboard.style.display = 'none';
                return;
            }
            scoreboard.style.display = 'flex';
            scoreboard.innerHTML = players.map(p => `
                <div class="score-badge">
                    <span>${p.name}</span>
                    <span class="score-value">${p.score} pts</span>
                    <span class="coin-value">${p.coins} 🪙</span>
                </div>
            `).join('');
        }"""

new_scoreboard = """        function updateScoreboard() {
            const scoreboard = document.getElementById('scoreboard');
            if (!scoreboard) return;
            if (players.length === 0) {
                scoreboard.style.display = 'none';
                return;
            }
            scoreboard.style.display = 'flex';
            scoreboard.innerHTML = players.map(p => `
                <div class="score-badge">
                    <span>${p.name}</span>
                    <span class="score-value">${p.score} pts</span>
                    <span class="coin-value">${p.coins} 🪙</span>
                </div>
            `).join('');
        }"""

content = content.replace(old_scoreboard, new_scoreboard)

# 2. Fix renderVoteButtons (add the missing if check for container)
old_render_votes = """        function renderVoteButtons() {
            const container = document.getElementById('vote-controls');
            if (players.length === 0) {
                container.innerHTML = `<button class="btn-action btn-next" onclick="nextPhrase()">Suivant</button>`;
                ((container && container.style) ? container.style : {}).display = 'flex';
                return;
            }
            ((container && container.style) ? container.style : {}).display = 'grid';
            let html = players.map((p, index) => `
                <button class="btn-vote" onclick="votePlayer(${index})">
                    <span>+1 Point pour ${p.name}</span>
                    <small>Gagne 10 🪙</small>
                </button>
            `).join('');
            html += `<button class="btn-vote btn-skip" onclick="nextPhrase()">Passer la manche</button>`;
            container.innerHTML = html;
        }"""

new_render_votes = """        function renderVoteButtons() {
            const container = document.getElementById('vote-controls');
            if (!container) return;
            if (players.length === 0) {
                container.innerHTML = `<button class="btn-action btn-next" onclick="nextPhrase()">Suivant</button>`;
                container.style.display = 'flex';
                return;
            }
            container.style.display = 'grid';
            let html = players.map((p, index) => `
                <button class="btn-vote" onclick="votePlayer(${index})">
                    <span>+1 Point pour ${p.name}</span>
                    <small>Gagne 10 🪙</small>
                </button>
            `).join('');
            html += `<button class="btn-vote btn-skip" onclick="nextPhrase()">Passer la manche</button>`;
            container.innerHTML = html;
        }"""

content = content.replace(old_render_votes, new_render_votes)

with open(file_path, 'w', encoding='utf-8-sig') as f:
    f.write(content)

print("Scoreboard and Vote Buttons secured.")
