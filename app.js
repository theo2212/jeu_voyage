let phrases = { soft: {}, hard: {} };

        const gameTitles = {
            tribunal: "Tribunal des Opinions",
            draft: "Draft de l'Absurde",
            prefere: "Tu Préfères... de l'Extrême",
            daube: "Pitch de Daube",
            redflag: "C'est un 10, MAIS...",
            boire_susceptible: "Qui est le plus susceptible",
            boire_jamais: "Je n'ai jamais (Sombre)",
            boire_action: "Action ou Cul Sec",
            boire_dictateur: "Le Dictateur",
            boire_serieux: "Garde ton sérieux",
            boire_7sec: "7 Secondes de l'Enfer",
            boire_roulette: "La Roulette Russe",
            boire_menteur: "Menteur ou Psychopathe",
            boire_kamikaze: "Le Kamikaze",
            boire_dilemme: "Dilemme Mortel"
        };

        const shopItems = [
            // Soft / Amusants
            { name: "Choix de la playlist musicale (30 min)", cost: 10, type: "soft" },
            { name: "Surnom ridicule pour l'autre", cost: 10, type: "soft" },
            { name: "Répondre avec un accent au choix (10 min)", cost: 20, type: "soft" },
            { name: "Droit de veto absolu sur un vote", cost: 30, type: "soft" },
            { name: "Massage des épaules (10 min)", cost: 40, type: "soft" },
            { name: "Action Joker : Petite corvée à l'arrivée", cost: 50, type: "soft" },
            
            // Epicés (Tirés d'Amiocoin)
            { name: "Baiser où tu veux, quand tu veux", cost: 20, type: "spicy" },
            { name: "Manger qqch directement dans la bouche de l'autre", cost: 30, type: "spicy" },
            { name: "Toucher l'autre en public sans se faire capter", cost: 40, type: "spicy" },
            { name: "Droit à une sieste collée-serrée", cost: 50, type: "spicy" },
            { name: "Lancer de dé coquin (6 idées sexy)", cost: 60, type: "spicy" },
            { name: "Massage érotique à l’huile ce soir", cost: 80, type: "spicy" },
            { name: "Gage mystère à exécuter sans le savoir", cost: 100, type: "spicy" },
            { name: "Shooting photo sexy (privé)", cost: 120, type: "spicy" },
            { name: "Nuit de plaisir avec toutes les envies réalisées", cost: 150, type: "spicy" },
            { name: "Fantasme surprise réalisé sans tabou", cost: 200, type: "spicy" }
        ];


        let currentGame = '';
        let currentTheme = 'soft';
        let availableIndices = {};
        let players = [];
        let timerInterval;
        let isEcoMode = false;
        let audioCtx = null;

        // --- Moteur Audio Procédural ---
        function initAudio() {
            if (!audioCtx) {
                audioCtx = new (window.AudioContext || window.webkitAudioContext)();
            }
        }

        let audioUnlocked = false;
        function unlockAudio() {
            if(audioUnlocked) return;
            initAudio();
            if(audioCtx) {
                const buffer = audioCtx.createBuffer(1, 1, 22050);
                const source = audioCtx.createBufferSource();
                source.buffer = buffer;
                source.connect(audioCtx.destination);
                source.start(0);
                audioCtx.resume().then(() => {
                    audioUnlocked = true;
                });
            }
            document.removeEventListener('touchstart', unlockAudio);
            document.removeEventListener('click', unlockAudio);
        }
        document.addEventListener('touchstart', unlockAudio, {once: true});
        document.addEventListener('click', unlockAudio, {once: true});

        function playSound(type) {
            if (!audioCtx) return;
            if (audioCtx.state === 'suspended') audioCtx.resume();
            const osc = audioCtx.createOscillator();
            const gain = audioCtx.createGain();
            osc.connect(gain);
            gain.connect(audioCtx.destination);
            
            const now = audioCtx.currentTime;
            if (type === 'coin') {
                osc.type = 'sine';
                osc.frequency.setValueAtTime(1000, now);
                osc.frequency.exponentialRampToValueAtTime(1500, now + 0.1);
                gain.gain.setValueAtTime(0.3, now);
                gain.gain.exponentialRampToValueAtTime(0.01, now + 0.1);
                osc.start(now);
                osc.stop(now + 0.1);
            } else if (type === 'tick') {
                osc.type = 'square';
                osc.frequency.setValueAtTime(150, now);
                gain.gain.setValueAtTime(0.1, now);
                gain.gain.exponentialRampToValueAtTime(0.01, now + 0.05);
                osc.start(now);
                osc.stop(now + 0.05);
            } else if (type === 'alarm') {
                osc.type = 'sawtooth';
                osc.frequency.setValueAtTime(300, now);
                osc.frequency.linearRampToValueAtTime(400, now + 0.2);
                gain.gain.setValueAtTime(0.4, now);
                gain.gain.linearRampToValueAtTime(0.01, now + 0.5);
                osc.start(now);
                osc.stop(now + 0.5);
            }
        }

        function triggerVibe(pattern) {
            if (navigator.vibrate) navigator.vibrate(pattern);
        }

        function toggleEcoMode() {
            isEcoMode = !isEcoMode;
            if(isEcoMode) document.body.classList.add('eco-mode');
            else document.body.classList.remove('eco-mode');
            triggerVibe(50);
        }

        // --- Quête du Jour ---
        const dailyQuests = [
            "Faites croire à un serveur/vendeur que c'est votre anniversaire de rencontre.",
            "Le premier à se plaindre d'avoir chaud ou d'avoir faim paie un verre.",
            "Réussir à placer le mot 'choucroute' dans une discussion avec un inconnu.",
            "Interdiction de regarder son téléphone pendant le repas. Le premier qui flanche paie l'addition.",
            "Inventez un nom de code pour désigner les personnes que vous trouvez moches dans la rue.",
            "Le perdant du prochain jeu devra porter le sac de l'autre pendant 1h."
        ];

        function checkDailyQuest() {
            const today = new Date().toDateString();
            const savedDate = localStorage.getItem('voyage_quest_date');
            let questIndex = localStorage.getItem('voyage_quest_index');
            
            if (savedDate !== today || questIndex === null) {
                questIndex = Math.floor(Math.random() * dailyQuests.length);
                localStorage.setItem('voyage_quest_date', today);
                localStorage.setItem('voyage_quest_index', questIndex);
            }
            
            document.getElementById('quest-text').innerText = dailyQuests[questIndex];
            document.getElementById('quest-banner').style.display = 'flex';
        }

        function initIndices() {
            availableIndices = {};
            for (let theme in phrases) {
                for (let key in phrases[theme]) {
                    availableIndices[theme + '_' + key] = Array.from({length: phrases[theme][key].length}, (_, i) => i);
                }
            }
            saveState();
        }

        function saveState() {
            localStorage.setItem('voyage_players', JSON.stringify(players));
            localStorage.setItem('voyage_availableIndices', JSON.stringify(availableIndices));
        }

        function loadState() {
            const savedVersion = localStorage.getItem('voyage_version');
            if (savedVersion !== 'v5_gigaupdate') {
                localStorage.clear();
                localStorage.setItem('voyage_version', 'v5_gigaupdate');
            }

            const savedPlayers = localStorage.getItem('voyage_players');
            if (savedPlayers) {
                players = JSON.parse(savedPlayers);
                // Patch pour l'inventaire
                players.forEach(p => { if(!p.inventory) p.inventory = []; });
            }

            const cached = localStorage.getItem('voyage_cached_phrases');
            if (cached) {
                phrases = JSON.parse(cached);
                const savedIndices = localStorage.getItem('voyage_availableIndices');
                if (savedIndices) {
                    availableIndices = JSON.parse(savedIndices);
                } else {
                    initIndices();
                }
            }
            checkDailyQuest();
        }

        function resetMemory() {
            if(confirm("Veux-tu vraiment effacer tous les joueurs, l'inventaire et les coins ?")) {
                localStorage.removeItem('voyage_players');
                localStorage.removeItem('voyage_availableIndices');
                players = [];
                initIndices();
                alert("Mémoire effacée !");
            }
        }

        function handleEnter(event) {
            if (event.key === 'Enter') addPlayer();
        }

        function addPlayer() {
            const input = document.getElementById('player-input');
            const name = input.value.trim();
            if (name) {
                players.push({ name: name, score: 0, coins: 0, inventory: [] });
                input.value = '';
                saveState();
                renderPlayers();
                triggerVibe(50);
            }
        }

        function removePlayer(index) {
            players.splice(index, 1);
            saveState();
            renderPlayers();
            triggerVibe(50);
        }

        function renderPlayers() {
            const list = document.getElementById('players-list');
            list.innerHTML = '';
            players.forEach((p, index) => {
                list.innerHTML += `
                    <div class="player-item">
                        <span>${p.name} <small style="color:#ffd700">(${p.coins} 🪙)</small></span>
                        <button class="btn-remove" onclick="removePlayer(${index})">&times;</button>
                    </div>
                `;
            });
        }

        function switchView(fromId, toId, callback) {
            const fromView = document.getElementById(fromId);
            const toView = document.getElementById(toId);
            
            if (!fromView || !toView) {
                console.error('switchView error: missing element', {fromId, toId, fromView, toView});
                if (!toView && toId !== 'menu-view') {
                    alert('Erreur : La vue \"' + toId + '\" est introuvable. Verifiez que vous avez bien la derniere version.');
                }
                return;
            }
            
            fromView.style.opacity = '0';
            fromView.style.transform = 'scale(0.9)';
            
            setTimeout(() => {
                fromView.style.display = 'none';
                toView.style.display = 'flex';
                
                if(callback) callback();
                
                setTimeout(() => {
                    toView.style.opacity = '1';
                    toView.style.transform = 'scale(1)';
                }, 50);
            }, 300);
        }

        function startGame(gameKey) {
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
        }

        function selectTheme(theme) {
            triggerVibe(50);
            currentTheme = theme;
            switchView('theme-setup-view', 'players-setup-view', () => {
                document.getElementById('player-input').focus();
            });
        }

        function returnToMenu(currentViewId) {
            triggerVibe(50);
            document.body.classList.remove('timer-flash');
            clearInterval(timerInterval);
            switchView(currentViewId, 'menu-view');
        }

        function beginGame() {
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
        }

        // --- Chrono ---
        function startTimer() {
            triggerVibe(50);
            const display = document.getElementById('timer-display');
            const btn = document.getElementById('btn-timer-start');
            let timeLeft = 7;
            
            btn.style.display = 'none';
            display.innerText = timeLeft;
            display.classList.remove('timer-flash');
            document.body.classList.remove('timer-flash');


            clearInterval(timerInterval);
            timerInterval = setInterval(() => {
                timeLeft--;
                display.innerText = timeLeft;
                playSound('tick');
                if (timeLeft <= 3) triggerVibe(100);
                
                if (syncMode === 'online' && isRoomAdmin && roomChannel) {
                    roomChannel.send({ type: 'broadcast', event: 'sync_timer', payload: { timeLeft: timeLeft } });
                }

                
                if (timeLeft <= 0) {
                    clearInterval(timerInterval);
                    display.innerText = "0 ! BOIS !";
                    document.body.classList.add('timer-flash');
                    display.classList.add('timer-flash');
                    btn.innerText = "Relancer ⏱️";
                    btn.style.display = 'block';
                    triggerVibe([200, 100, 200, 100, 200]);
                    playSound('alarm');
                }
            }, 1000);
        }

        // --- Inventaire & Boutique ---
        function openShop() {
            if(players.length === 0) {
                alert("Ajoutez d'abord des joueurs pour ouvrir la boutique !");
                return;
            }
            triggerVibe(50);
            switchView('menu-view', 'shop-view', () => {
                const select = document.getElementById('shop-player-select');
                select.innerHTML = players.map((p, i) => `<option value="${i}">${p.name}</option>`).join('');
                renderShopItems();
            });
        }

        function renderShopItems() {
            const select = document.getElementById('shop-player-select');
            const playerIndex = select.value;
            const player = players[playerIndex];
            
            document.getElementById('shop-balance').innerText = player.coins + " 🪙";
            
            const grid = document.getElementById('shop-grid');
            grid.innerHTML = shopItems.map((item, index) => {
                const canAfford = player.coins >= item.cost;
                return `
                    <div class="shop-item type-${item.type}">
                        <div class="shop-item-info">
                            <div class="shop-item-name">${item.name}</div>
                            <div class="shop-item-cost">${item.cost} 🪙</div>
                        </div>
                        <button class="btn-buy" onclick="buyItem(${index})" ${!canAfford ? 'disabled' : ''}>Acheter</button>
                    </div>
                `;
            }).join('');
        }

        function buyItem(itemIndex) {
            const select = document.getElementById('shop-player-select');
            const playerIndex = select.value;
            const player = players[playerIndex];
            const item = shopItems[itemIndex];
            
            if (player.coins >= item.cost) {
                player.coins -= item.cost;
                player.inventory.push(item.name);
                saveState();
                playSound('coin');
                triggerVibe([50, 50, 100]);
                alert(`🎁 Ajouté à l'inventaire de ${player.name} !`);
                renderShopItems();
            }
        }

        function openInventory() {
            if(players.length === 0) {
                alert("Aucun joueur n'est enregistré !");
                return;
            }
            triggerVibe(50);
            const playerNameSpan = document.getElementById('inv-player-name');
            const invList = document.getElementById('inventory-list');
            
            // On affiche le premier joueur par défaut, idéalement à améliorer avec un select
            let pIndex = 0; 
            const player = players[pIndex];
            playerNameSpan.innerText = player.name;
            
            if (player.inventory.length === 0) {
                invList.innerHTML = `<div style="color:white; opacity:0.6;">Inventaire vide.</div>`;
            } else {
                invList.innerHTML = player.inventory.map((itemName, idx) => `
                    <div class="inventory-item">
                        <span>${itemName}</span>
                        <button class="btn-action" style="padding: 5px 15px; font-size: 0.9rem;" onclick="useItem(${pIndex}, ${idx})">Utiliser</button>
                    </div>
                `).join('');
            }
            document.getElementById('inventory-modal').style.display = 'flex';
        }

        function useItem(pIndex, itemIdx) {
            triggerVibe(50);
            if (confirm("Veux-tu utiliser cet objet maintenant ? Il sera consommé.")) {
                players[pIndex].inventory.splice(itemIdx, 1);
                saveState();
                openInventory();
            }
        }

        function closeInventory() {
            triggerVibe(50);
            document.getElementById('inventory-modal').style.display = 'none';
        }

        // --- Roue de la Punition ---
        const punishments = [
            "Bois 3 gorgées 🍻", "Cul Sec ! 🍺", "Enlève un vêtement 🧦",
            "Masse les épaules d'un joueur (2min) 💆", "-50 BussCoins 🪙",
            "Mime ta position sexuelle 🛏️", "Donne 5 gorgées 🎯", "Révèle un secret 🤫",
            "Fais 10 pompes 💪", "Poste une story gênante 📱"
        ];
        function spinWheel() {
            triggerVibe(50);
            document.getElementById('wheel-modal').style.display = 'flex';
            document.getElementById('wheel-result').innerText = "Prêt à tourner ?";
            document.getElementById('btn-spin').style.display = 'inline-block';
        }
        function closeWheel() {
            triggerVibe(50);
            document.getElementById('wheel-modal').style.display = 'none';
        }
        function executeSpin() {
            const btn = document.getElementById('btn-spin');
            btn.style.display = 'none';
            const resultDiv = document.getElementById('wheel-result');
            let count = 0;
            let maxCount = 20 + Math.floor(Math.random() * 10);
            
            let spinInterval = setInterval(() => {
                resultDiv.innerText = punishments[count % punishments.length];
                triggerVibe(20);
                playSound('tick');
                count++;
                if (count > maxCount) {
                    clearInterval(spinInterval);
                    const finalResult = punishments[count % punishments.length];
                    resultDiv.innerText = `🎯 ${finalResult} !`;
                    triggerVibe([100, 50, 100]);
                    playSound('coin');
                }
            }, 100);
        }

        // --- Logique de Jeu ---
        function updateScoreboard() {
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
        }

        function renderVoteButtons() {
            const container = document.getElementById('vote-controls');
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
        }

        function votePlayer(index) {
            triggerVibe(30);
            players[index].score += 1;
            players[index].coins += 10;
            saveState();
            updateScoreboard();
            nextPhrase();
        }

        function nextPhrase(isFirst = false) {
            triggerVibe(30);
            let activeGame = currentGame;
            let activeTheme = currentTheme;

            if (currentGame === 'chaos') {
                const keys = Object.keys(phrases['soft']);
                activeGame = keys[Math.floor(Math.random() * keys.length)];
                activeTheme = Math.random() > 0.5 ? 'soft' : 'hard';
                document.getElementById('game-title').innerText = `Chaos : ${gameTitles[activeGame]} ${activeTheme === 'hard' ? '🌶️' : ''}`;
            }

            if (!phrases[activeTheme] || !phrases[activeTheme][activeGame]) {
                console.error("Missing phrases for", {activeTheme, activeGame, phrases});
                alert("Oups ! Les phrases pour ce mode ne sont pas encore téléchargées. Patiente 2 secondes ou change de mode.");
                return;
            }
            
            const memKey = activeTheme + '_' + activeGame;
            let list = availableIndices[memKey];
            
            if (!list || list.length === 0) {
                list = Array.from({length: phrases[activeTheme][activeGame].length}, (_, i) => i);
                availableIndices[memKey] = list;
            }
            
            const randomIndexList = Math.floor(Math.random() * list.length);
            const phraseIndex = list.splice(randomIndexList, 1)[0];
            saveState();
            
            const textElement = document.getElementById('game-text');
            const cardElement = document.getElementById('game-card');

            // Timer display logic
            if (activeGame === 'boire_7sec') {
                document.getElementById('timer-container').style.display = 'flex';
                document.getElementById('timer-display').innerText = '7';
                document.getElementById('timer-display').classList.remove('timer-flash');
                document.getElementById('btn-timer-start').style.display = 'block';
                document.getElementById('btn-timer-start').innerText = 'Lancer le Chrono ⏱️';
                document.body.classList.remove('timer-flash');
                clearInterval(timerInterval);
            } else {
                document.getElementById('timer-container').style.display = 'none';
                document.body.classList.remove('timer-flash');
                clearInterval(timerInterval);
            }
            
            if (isFirst) {
                textElement.innerText = phrases[activeTheme][activeGame][phraseIndex];
                textElement.className = 'text-pop-in';
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

            } else {
                textElement.className = 'text-pop-out';
                cardElement.style.transform = 'scale(0.98)';
                
                setTimeout(() => {
                    textElement.innerText = phrases[activeTheme][activeGame][phraseIndex];
                    textElement.className = 'text-pop-in';
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

                    cardElement.style.transform = 'scale(1)';
                }, 250);
            }
        }

        // --- Swipe Events ---
        let touchStartX = 0;
        let touchEndX = 0;
        document.addEventListener('DOMContentLoaded', () => {
            loadState();
            
            const gameCard = document.getElementById('game-card');
            gameCard.addEventListener('touchstart', e => {
                touchStartX = e.changedTouches[0].screenX;
            }, {passive: true});
            
            gameCard.addEventListener('touchend', e => {
                touchEndX = e.changedTouches[0].screenX;
                if (touchStartX - touchEndX > 50) {
                    // Swiped Left
                    nextPhrase();
                } else if (touchEndX - touchStartX > 50) {
                    // Swiped Right
                    nextPhrase();
                }
            }, {passive: true});
            
            if ('serviceWorker' in navigator) {
                navigator.serviceWorker.register('sw.js')
                .then(() => console.log('Service Worker Registered'));
            }
        });

// --- SUPABASE & MULTIJOUEUR ---
const SUPABASE_URL = 'https://pzdbkegmbxsvabkvffdi.supabase.co';
const SUPABASE_ANON_KEY = 'sb_publishable_esYFZqPxzRx24Wh_VrGFqQ_QybEoy_w';
let supabaseClient = null;
let isPremium = localStorage.getItem('voyage_premium') === 'true';
let syncMode = localStorage.getItem('voyage_sync_mode'); // 'online' ou 'offline'


async function fetchPhrasesFromSupabase() {
    const sb = getSupabase();
    if (!sb) return;

    try {
        const { data, error } = await sb.from('phrases').select('*');
        if (error) throw error;
        
        if (data && data.length > 0) {
            let newPhrases = { soft: {}, hard: {} };
            
            data.forEach(row => {
                if (newPhrases[row.theme]) {
                    if (!newPhrases[row.theme][row.game_mode]) {
                        newPhrases[row.theme][row.game_mode] = [];
                    }
                    newPhrases[row.theme][row.game_mode].push(row.content);
                }
            });
            
            phrases = newPhrases;
            localStorage.setItem('voyage_cached_phrases', JSON.stringify(phrases));
            initIndices();
            console.log('Phrases telechargees depuis Supabase !');
        }
    } catch (e) {
        console.error('Erreur lors du telechargement des phrases:', e);
        const cached = localStorage.getItem('voyage_cached_phrases');
        if (cached) {
            phrases = JSON.parse(cached);
            initIndices();
        }
    }
}


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
    list.innerHTML = roomPlayers.map(p => `<div>${p.isAdmin ? '👑 ' : ''}${p.name + (p.id === myPlayerId ? ' (Toi)' : '')}</div>`).join('');
    
    if (isRoomAdmin && roomPlayers.length > 1) {
        document.getElementById('btn-start-room').style.display = 'inline-block';
    } else {
        document.getElementById('btn-start-room').style.display = 'none';
    }
}

async function createRoom() {
    const pseudoInput = document.getElementById('player-pseudo-input');
    if (!pseudoInput) {
        alert("Erreur critique : Votre page (index.html) n'est pas a jour. Veuillez vider le cache Safari (Reglages -> Safari -> Avance -> Donnees de sites -> Supprimer github.io).");
        return;
    }
    const pseudo = pseudoInput.value.trim() || 'Anonyme';
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
    const pseudoInput = document.getElementById('player-pseudo-input');
    if (!pseudoInput) {
        alert("Erreur critique : Votre page (index.html) n'est pas a jour. Veuillez vider le cache Safari (Reglages -> Safari -> Avance -> Donnees de sites -> Supprimer github.io).");
        return;
    }
    const pseudo = pseudoInput.value.trim() || 'Anonyme';
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
                roomPlayers.push({ id: newPlayer.id, name: newPlayer.name, isAdmin: false });
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
    alert("✅ Salon prêt ! Les téléphones de tes amis vont se synchroniser. Choisis un jeu dans le menu pour commencer !");
    switchView('lobby-view', 'menu-view');
}

function getSupabase() {
    if (!supabaseClient && window.supabase) {
        supabaseClient = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);
    }
    return supabaseClient;
}

document.addEventListener('DOMContentLoaded', () => {
    // Le modal s'affiche à chaque lancement d'application comme demandé
    document.getElementById('sync-modal').style.display = 'flex';
    fetchPhrasesFromSupabase();
});

function openSyncModal() {
    triggerVibe(50);
    document.getElementById('sync-modal').style.display = 'flex';
    fetchPhrasesFromSupabase();
}

function chooseSync(mode) {
    syncMode = mode;
    localStorage.setItem('voyage_sync_mode', mode);
    document.getElementById('sync-modal').style.display = 'none';
    if(mode === 'online') {
        switchView('menu-view', 'lobby-view');
    }
}

// --- UGC (Proposer une phrase) ---
function openUGC() {
    triggerVibe(50);
    document.getElementById('ugc-modal').style.display = 'flex';
}

function closeUGC() {
    triggerVibe(50);
    document.getElementById('ugc-modal').style.display = 'none';
}

async function submitUGC() {
    triggerVibe(50);
    const theme = document.getElementById('ugc-theme').value;
    const game = document.getElementById('ugc-game').value;
    const text = document.getElementById('ugc-text').value.trim();
    const author = document.getElementById('ugc-author').value.trim() || 'Anonyme';

    if(!text) {
        alert("La phrase ne peut pas être vide !");
        return;
    }

    const sb = getSupabase();
    if (!sb) {
        alert("Le système n'est pas encore prêt, veuillez patienter quelques secondes et réessayer.");
        return;
    }

    try {
        const { error } = await sb.from('pending_phrases').insert([
            { theme: theme, game_mode: game, content: text, submitted_by: author }
        ]);
        
        if (error) throw error;
        
        playSound('coin');
        alert("Merci ! Ta phrase a été envoyée et sera ajoutée après validation. 🚀");
        document.getElementById('ugc-text').value = '';
        closeUGC();
    } catch (e) {
        alert("Erreur lors de l'envoi. Vérifie ta connexion internet.");
        console.error(e);
    }
}

// --- FREEMIUM ---
function requirePremium(callback) {
    if (isPremium) {
        callback();
    } else {
        triggerVibe(50);
        document.getElementById('paywall-modal').style.display = 'flex';
    }
}

function closePaywall() {
    triggerVibe(50);
    document.getElementById('paywall-modal').style.display = 'none';
}

function simulatePurchase() {
    triggerVibe([50, 100, 50]);
    playSound('coin');
    isPremium = true;
    localStorage.setItem('voyage_premium', 'true');
    closePaywall();
    alert("🎉 Achat validé ! Vous avez maintenant accès à tout le contenu Premium.");
}

// Hook Premium into selectTheme and startGame
const originalSelectTheme = selectTheme;
selectTheme = function(theme) {
    if (theme === 'hard') {
        requirePremium(() => originalSelectTheme(theme));
    } else {
        originalSelectTheme(theme);
    }
};

const originalStartGame = startGame;
startGame = function(gameKey) {
    if (gameKey === 'chaos') {
        requirePremium(() => originalStartGame(gameKey));
    } else {
        originalStartGame(gameKey);
    }
};
