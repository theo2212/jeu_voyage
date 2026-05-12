import re

with open('app.js', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Variables globales pour le multijoueur
multiplayer_vars = """
// --- MULTIJOUEUR VARIABLES ---
let roomChannel = null;
let isRoomAdmin = false;
let myRoomId = null;
let myPlayerId = Math.random().toString(36).substr(2, 9);
let roomPlayers = [];

function generateRoomCode() {
    const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    let code = '';
    for(let i=0; i<4; i++) code += chars.charAt(Math.floor(Math.random() * chars.length));
    return code;
}

function updateLobbyUI() {
    const list = document.getElementById('room-players-list');
    list.innerHTML = roomPlayers.map(p => `<div>${p.isAdmin ? '👑 ' : ''}${p.id === myPlayerId ? 'Toi' : 'Joueur ' + p.id}</div>`).join('');
    
    if (isRoomAdmin && roomPlayers.length > 1) {
        document.getElementById('btn-start-room').style.display = 'inline-block';
    } else {
        document.getElementById('btn-start-room').style.display = 'none';
    }
}

async function createRoom() {
    triggerVibe(50);
    myRoomId = generateRoomCode();
    isRoomAdmin = true;
    roomPlayers = [{ id: myPlayerId, isAdmin: true }];
    
    document.getElementById('lobby-controls').style.display = 'none';
    document.getElementById('room-waiting-area').style.display = 'block';
    document.getElementById('room-code-display').innerText = myRoomId;
    updateLobbyUI();
    
    await joinSupabaseChannel(myRoomId);
}

async function joinRoom() {
    triggerVibe(50);
    const input = document.getElementById('room-code-input').value.toUpperCase().trim();
    if (input.length !== 4) {
        shakeInput('room-code-input');
        showToast('Code invalide (4 lettres)', 'warning');
        return;
    }
    
    myRoomId = input;
    isRoomAdmin = false;
    
    document.getElementById('lobby-controls').style.display = 'none';
    document.getElementById('room-waiting-area').style.display = 'block';
    document.getElementById('room-code-display').innerText = myRoomId;
    
    await joinSupabaseChannel(myRoomId);
    
    if (roomChannel) {
        roomChannel.send({
            type: 'broadcast',
            event: 'player_join',
            payload: { id: myPlayerId }
        });
    }
}

async function joinSupabaseChannel(roomId) {
    const sb = getSupabase();
    if (!sb) {
        alert("Supabase non connecté.");
        return;
    }
    
    if (roomChannel) {
        await sb.removeChannel(roomChannel);
    }
    
    roomChannel = sb.channel('room-' + roomId);
    
    roomChannel.on('broadcast', { event: 'player_join' }, payload => {
        if (isRoomAdmin) {
            const newPlayer = payload.payload;
            if (!roomPlayers.find(p => p.id === newPlayer.id)) {
                roomPlayers.push({ id: newPlayer.id, isAdmin: false });
                updateLobbyUI();
                roomChannel.send({
                    type: 'broadcast',
                    event: 'room_state',
                    payload: { players: roomPlayers }
                });
            }
        }
    });
    
    roomChannel.on('broadcast', { event: 'room_state' }, payload => {
        if (!isRoomAdmin) {
            roomPlayers = payload.payload.players;
            updateLobbyUI();
            document.getElementById('btn-start-room').style.display = 'none'; // Only admin can start
        }
    });

    roomChannel.on('broadcast', { event: 'start_game' }, payload => {
        if (!isRoomAdmin) {
            switchView('lobby-view', 'game-view');
            // Hide admin buttons
            const voteGrid = document.getElementById('vote-controls');
            if(voteGrid) voteGrid.style.display = 'none';
            document.querySelectorAll('.controls .btn-action').forEach(b => {
                if(b.innerText.includes('Quitter')) b.style.display = 'inline-block';
                else b.style.display = 'none';
            });
            document.getElementById('btn-timer-start').style.display = 'none';
        }
    });

    roomChannel.on('broadcast', { event: 'sync_phrase' }, payload => {
        if (!isRoomAdmin) {
            const data = payload.payload;
            
            const gameTitle = document.getElementById('game-title');
            if (data.currentGame === 'chaos') {
                gameTitle.innerText = "Jeu Surprise ! 🌪️";
                gameTitle.className = 'txt-boire';
            } else {
                gameTitle.innerText = gameTitles[data.currentGame] + (data.currentTheme === 'hard' ? ' 🌶️' : '');
                gameTitle.className = 'txt-' + data.currentGame.replace('boire_', 'boire'); 
            }
            
            const textElement = document.getElementById('game-text');
            const cardElement = document.getElementById('game-card');
            
            if (data.currentGame === 'boire_7sec') {
                document.getElementById('timer-container').style.display = 'flex';
                document.getElementById('timer-display').innerText = '7';
                document.getElementById('timer-display').classList.remove('timer-flash');
                document.body.classList.remove('timer-flash');
            } else {
                document.getElementById('timer-container').style.display = 'none';
                document.body.classList.remove('timer-flash');
            }
            
            textElement.className = 'text-pop-out';
            cardElement.style.transform = 'scale(0.98)';
            
            setTimeout(() => {
                textElement.innerText = data.phraseText;
                textElement.className = 'text-pop-in';
                cardElement.style.transform = 'scale(1)';
            }, 250);
        }
    });
    
    roomChannel.on('broadcast', { event: 'sync_timer' }, payload => {
        if (!isRoomAdmin) {
            const data = payload.payload;
            const display = document.getElementById('timer-display');
            display.innerText = data.timeLeft;
            if (data.timeLeft === 0) {
                document.body.classList.add('timer-flash');
                display.classList.add('timer-flash');
                display.innerText = "0 ! BOIS !";
                triggerVibe([200, 100, 200]);
                playSound('alarm');
            } else {
                document.body.classList.remove('timer-flash');
                display.classList.remove('timer-flash');
                playSound('tick');
            }
        }
    });
    
    await roomChannel.subscribe((status) => {
        if(status === 'SUBSCRIBED') {
            console.log('Connecté au salon ' + roomId);
        }
    });
}

function startOnlineGame() {
    triggerVibe(50);
    showToast("✅ Salon prêt ! Amis synchronisés.", "success");
    switchView('lobby-view', 'menu-view');
}
"""

if "function generateRoomCode()" not in code:
    code = code.replace("function getSupabase() {", multiplayer_vars + "\nfunction getSupabase() {")

# 2. Modifier chooseSync
choose_sync_replacement = """function chooseSync(mode) {
    syncMode = mode;
    localStorage.setItem('voyage_sync_mode', mode);
    document.getElementById('sync-modal').style.display = 'none';
    
    // Afficher/Masquer Gartic dans le menu
    const garticBtn = document.getElementById('btn-menu-gartic');
    if (garticBtn) {
        garticBtn.style.display = (mode === 'online') ? 'block' : 'none';
    }

    if(mode === 'online') {
        switchView('menu-view', 'lobby-view');
    }
}"""
code = re.sub(r'function chooseSync\(mode\) \{[\s\S]*?\}', choose_sync_replacement, code)

# 3. Hook beginGame for start_game broadcast
begin_game_replacement = """        function beginGame() {
            triggerVibe([50, 50, 50]);
            players.forEach(p => p.score = 0); 
            
            switchView('players-setup-view', 'game-view', () => {
                const gameTitle = document.getElementById('game-title');
                
                if (currentGame === 'chaos') {
                    gameTitle.innerText = "Jeu Surprise ! 🌪️";
                    gameTitle.className = 'txt-boire';
                } else {
                    gameTitle.innerText = gameTitles[currentGame] + (currentTheme === 'hard' ? ' 🌶️' : '');
                    gameTitle.className = 'txt-' + currentGame.replace('boire_', 'boire'); 
                    if (currentGame.includes('boire')) gameTitle.className = 'txt-boire';
                    if (currentGame === 'tribunal') gameTitle.className = 'txt-tribunal';
                    if (currentGame === 'draft') gameTitle.className = 'txt-draft';
                    if (currentGame === 'prefere') gameTitle.className = 'txt-prefere';
                    if (currentGame === 'daube') gameTitle.className = 'txt-daube';
                    if (currentGame === 'redflag') gameTitle.className = 'txt-redflag';
                }
                
                updateScoreboard();
                renderVoteButtons();
                
                if (syncMode === 'online' && isRoomAdmin && roomChannel) {
                    roomChannel.send({ type: 'broadcast', event: 'start_game', payload: {} });
                }
                
                nextPhrase(true);
            });
        }"""
code = re.sub(r'        function beginGame\(\) \{[\s\S]*?nextPhrase\(true\);\n            \}\);\n        \}', begin_game_replacement, code)

# 4. Hook nextPhrase for sync_phrase broadcast
next_phrase_hook = """
            if (syncMode === 'online' && isRoomAdmin && roomChannel) {
                roomChannel.send({
                    type: 'broadcast',
                    event: 'sync_phrase',
                    payload: {
                        currentGame: activeGame,
                        currentTheme: activeTheme,
                        phraseText: textElement.innerText
                    }
                });
            }
"""
code = code.replace("textElement.innerText = phrases[activeTheme][activeGame][phraseIndex];\n                    textElement.className = 'text-pop-in';", "textElement.innerText = phrases[activeTheme][activeGame][phraseIndex];\n                    textElement.className = 'text-pop-in';" + next_phrase_hook)
# Also for the isFirst block
code = code.replace("textElement.innerText = phrases[activeTheme][activeGame][phraseIndex];\n                textElement.className = 'text-pop-in';", "textElement.innerText = phrases[activeTheme][activeGame][phraseIndex];\n                textElement.className = 'text-pop-in';" + next_phrase_hook)

# 5. Hook startTimer for sync_timer broadcast
timer_hook = """
            clearInterval(timerInterval);
            timerInterval = setInterval(() => {
                timeLeft--;
                display.innerText = timeLeft;
                playSound('tick');
                if (timeLeft <= 3) triggerVibe(100);
                
                if (syncMode === 'online' && isRoomAdmin && roomChannel) {
                    roomChannel.send({ type: 'broadcast', event: 'sync_timer', payload: { timeLeft: timeLeft } });
                }
"""
code = code.replace("""            clearInterval(timerInterval);
            timerInterval = setInterval(() => {
                timeLeft--;
                display.innerText = timeLeft;
                playSound('tick');
                if (timeLeft <= 3) triggerVibe(100);""", timer_hook)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(code)

print("Multiplayer logic injected.")
