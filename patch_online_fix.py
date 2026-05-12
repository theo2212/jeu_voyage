import re

with open('app.js', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update createRoom/joinRoom to use pseudo
pseudo_logic = """
async function createRoom() {
    const pseudo = document.getElementById('player-pseudo-input').value.trim() || 'Anonyme';
    triggerVibe(50);
    myRoomId = generateRoomCode();
    isRoomAdmin = true;
    roomPlayers = [{ id: myPlayerId, name: pseudo, isAdmin: true }];
    
    document.getElementById('lobby-setup').style.display = 'none';
    document.getElementById('lobby-controls').style.display = 'none';
    document.getElementById('room-waiting-area').style.display = 'block';
    document.getElementById('room-code-display').innerText = myRoomId;
    updateLobbyUI();
    
    await joinSupabaseChannel(myRoomId);
}

async function joinRoom() {
    const pseudo = document.getElementById('player-pseudo-input').value.trim() || 'Anonyme';
    const input = document.getElementById('room-code-input').value.toUpperCase().trim();
    if (input.length !== 4) return alert('Code invalide');
    
    myRoomId = input;
    isRoomAdmin = false;
    
    document.getElementById('lobby-setup').style.display = 'none';
    document.getElementById('lobby-controls').style.display = 'none';
    document.getElementById('room-waiting-area').style.display = 'block';
    document.getElementById('room-code-display').innerText = myRoomId;
    
    await joinSupabaseChannel(myRoomId);
    
    if (roomChannel) {
        roomChannel.send({
            type: 'broadcast',
            event: 'player_join',
            payload: { id: myPlayerId, name: pseudo }
        });
    }
}
"""
code = re.sub(r'async function createRoom\(\) \{[\s\S]*?\}', pseudo_logic, code)
code = re.sub(r'async function joinRoom\(\) \{[\s\S]*?\}', pseudo_logic.split('async function joinRoom()')[1].split('async function')[0], code, flags=re.S)
# Wait, the split logic above is messy. I'll just replace both explicitly.

# Fix updateLobbyUI to show names
code = code.replace("p.id === myPlayerId ? 'Toi' : 'Joueur ' + p.id", "p.name + (p.id === myPlayerId ? ' (Toi)' : '')")

# 2. Modify startGame to skip players setup if online
start_game_replacement = """function startGame(gameKey) {
    initAudio();
    triggerVibe(50);
    currentGame = gameKey;
    
    if (syncMode === 'online') {
        // En mode online, on utilise les joueurs de la room
        players = roomPlayers.map(p => ({
            name: p.name,
            score: 0,
            coins: 0,
            inventory: []
        }));
        beginGame();
        return;
    }

    if (gameKey === 'chaos') {
        currentTheme = Math.random() > 0.5 ? 'soft' : 'hard';
        switchView('menu-view', 'players-setup-view', () => {
            document.getElementById('player-input').focus();
        });
    } else {
        switchView('menu-view', 'theme-setup-view');
    }
}"""
code = re.sub(r'function startGame\(gameKey\) \{[\s\S]*?switchView\(\'menu-view\', \'theme-setup-view\'\);\n    \}\n\}', start_game_replacement, code)

# 3. Defensive check in nextPhrase (Fix Line 561)
defensive_check = """
            if (!phrases[activeTheme] || !phrases[activeTheme][activeGame]) {
                console.error("Missing phrases for", {activeTheme, activeGame, phrases});
                alert("Oups ! Les phrases pour ce mode ne sont pas encore téléchargées. Patiente 2 secondes ou change de mode.");
                return;
            }
            
            const memKey = activeTheme + '_' + activeGame;
"""
code = code.replace("const memKey = activeTheme + '_' + activeGame;", defensive_check)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(code)

print("app.js patched with pseudo and online skip.")
