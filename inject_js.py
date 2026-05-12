import re

new_js = """
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

        function playSound(type) {
            if (!audioCtx) return;
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
            showToast(isEcoMode ? "Mode Éco activé 🔋" : "Mode Éco désactivé ⚡", "info");
        }

        // --- Notifications (Toasts) ---
        function showToast(message, type = 'info') {
            const container = document.getElementById('notification-container');
            if (!container) return;
            const toast = document.createElement('div');
            toast.className = `toast ${type}`;
            const icons = { info: 'ℹ️', success: '✅', warning: '⚠️', error: '❌' };
            toast.innerHTML = `<span>${icons[type] || '🔔'}</span> <span>${message}</span>`;
            container.appendChild(toast);
            triggerVibe(type === 'error' ? [50, 100, 50] : 30);
            setTimeout(() => {
                toast.classList.add('toast-exit');
                setTimeout(() => toast.remove(), 400);
            }, 3500);
        }

        function shakeInput(inputId) {
            const el = document.getElementById(inputId);
            if (el) {
                el.classList.add('shake');
                el.style.borderColor = '#ff3b30';
                setTimeout(() => {
                    el.classList.remove('shake');
                    el.style.borderColor = '';
                }, 400);
                el.focus();
            }
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

        // --- DATA QUIZ ---
        const quizQuestions = {
            qcm: [
                { q: "Quelle est la capitale de l'Australie ?", a: ["Sydney", "Melbourne", "Canberra", "Perth"], c: 2 },
                { q: "Quel pays a gagné la Coupe du Monde 2018 ?", a: ["France", "Croatie", "Brésil", "Allemagne"], c: 0 },
                { q: "Combien y a-t-il de continents ?", a: ["5", "6", "7", "8"], c: 2 },
                { q: "Quelle est la monnaie du Japon ?", a: ["Yuan", "Yen", "Won", "Dollar"], c: 1 },
                { q: "Qui a peint la Joconde ?", a: ["Van Gogh", "Picasso", "Da Vinci", "Monet"], c: 2 },
                { q: "Quelle est la planète la plus proche du Soleil ?", a: ["Vénus", "Mars", "Mercure", "Jupiter"], c: 2 },
                { q: "En quelle année est né Internet ?", a: ["1969", "1983", "1995", "2000"], c: 1 },
                { q: "Quel est l'oiseau qui ne vole pas ?", a: ["Aigle", "Autruche", "Pigeon", "Moineau"], c: 1 },
                { q: "Quel est l'élément chimique de symbole O ?", a: ["Or", "Oxygène", "Ozone", "Osmium"], c: 1 },
                { q: "Quelle est la langue la plus parlée au monde ?", a: ["Anglais", "Espagnol", "Mandarin", "Français"], c: 2 }
            ],
            expert: [
                { q: "Quel est le nom du célèbre détective créé par Arthur Conan Doyle ?", a: "Sherlock Holmes" },
                { q: "Quel est le point culminant du monde ?", a: "Everest" },
                { q: "Quel gaz les plantes absorbent-elles pour faire la photosynthèse ?", a: "CO2 / Dioxyde de carbone" },
                { q: "Qui a écrit 'Les Misérables' ?", a: "Victor Hugo" },
                { q: "Quel est l'organe le plus lourd du corps humain ?", a: "Le foie" },
                { q: "Quel fleuve traverse l'Égypte ?", a: "Le Nil" },
                { q: "Combien d'États y a-t-il aux États-Unis ?", a: "50" },
                { q: "Dans quel pays se trouve la ville de Marrakech ?", a: "Maroc" },
                { q: "Quel est l'inventeur de l'ampoule électrique ?", a: "Thomas Edison" },
                { q: "Quel métal est liquide à température ambiante ?", a: "Le mercure" }
            ]
        };

        let currentQuizType = 'qcm';
        let currentQuizIndex = 0;
        let quizAnswersReceived = [];
        let quizTimerInterval = null;

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

            const savedIndices = localStorage.getItem('voyage_availableIndices');
            if (savedIndices) {
                availableIndices = JSON.parse(savedIndices);
            } else {
                initIndices();
            }
            checkDailyQuest();
        }

        function resetMemory() {
            if(confirm("Veux-tu vraiment effacer tous les joueurs, l'inventaire et les coins ?")) {
                localStorage.removeItem('voyage_players');
                localStorage.removeItem('voyage_availableIndices');
                players = [];
                initIndices();
                showToast("Mémoire effacée !", "success");
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
            } else {
                shakeInput('player-input');
                showToast("Veuillez entrer un nom !", "warning");
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
            } else {
                textElement.className = 'text-pop-out';
                cardElement.style.transform = 'scale(0.98)';
                
                setTimeout(() => {
                    textElement.innerText = phrases[activeTheme][activeGame][phraseIndex];
                    textElement.className = 'text-pop-in';
                    cardElement.style.transform = 'scale(1)';
                }, 250);
            }
        }

        // --- LOGIQUE QUIZ ---
        function startQuiz(type) {
            triggerVibe(50);
            if (syncMode !== 'online') {
                showToast("Mode en ligne requis pour le Quiz !", "warning");
                return;
            }
            if (!isRoomAdmin) {
                showToast("Seul l'admin peut lancer le Quiz.", "warning");
                return;
            }

            currentQuizType = type;
            currentQuizIndex = 0;
            quizAnswersReceived = [];
            
            roomChannel.send({
                type: 'broadcast',
                event: 'start_quiz',
                payload: { type: type }
            });

            loadQuizQuestion();
        }

        function loadQuizQuestion() {
            const qData = quizQuestions[currentQuizType][currentQuizIndex];
            const view = 'quiz-view';
            
            document.getElementById('quiz-question-count').innerText = `Question ${currentQuizIndex + 1} / 10`;
            document.getElementById('quiz-question-text').innerText = qData.q;
            document.getElementById('quiz-title').innerText = currentQuizType === 'qcm' ? "⚡ Quiz Rapido" : "🎓 Quiz Expert";
            
            // Reset UI
            document.getElementById('quiz-options').style.display = 'none';
            document.getElementById('quiz-input-zone').style.display = 'none';
            document.getElementById('quiz-wait-message').style.display = 'none';
            document.getElementById('quiz-timer-progress').style.width = '100%';
            document.getElementById('quiz-answer-input').value = '';
            
            if (currentQuizType === 'qcm') {
                const optionsDiv = document.getElementById('quiz-options');
                optionsDiv.style.display = 'grid';
                optionsDiv.innerHTML = qData.a.map((opt, i) => `
                    <button class="btn-vote" style="width: 100%; height: 60px; font-size: 1.1rem; margin: 0; border-radius: 18px; background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.1); color: white; font-weight: 500;" onclick="checkQcmAnswer(${i})">${opt}</button>
                `).join('');
            } else {
                document.getElementById('quiz-input-zone').style.display = 'block';
            }

            switchView(currentViewId, view);
            startQuizTimer();
        }

        function startQuizTimer() {
            let timeLeft = 15;
            const bar = document.getElementById('quiz-timer-progress');
            
            clearInterval(quizTimerInterval);
            quizTimerInterval = setInterval(() => {
                timeLeft -= 0.1;
                bar.style.width = (timeLeft / 15) * 100 + '%';
                
                if (timeLeft <= 0) {
                    clearInterval(quizTimerInterval);
                    handleQuizTimeout();
                }
            }, 100);
        }

        function handleQuizTimeout() {
            if (currentQuizType === 'expert') {
                if (isRoomAdmin) {
                    showValidationScreen();
                } else {
                    document.getElementById('quiz-input-zone').style.display = 'none';
                    document.getElementById('quiz-wait-message').innerText = "Temps écoulé ! En attente du verdict...";
                    document.getElementById('quiz-wait-message').style.display = 'block';
                }
            } else {
                if (isRoomAdmin) nextQuizQuestion();
            }
        }

        function checkQcmAnswer(index) {
            const qData = quizQuestions['qcm'][currentQuizIndex];
            if (index === qData.c) {
                showToast("Bonne réponse ! ⚡", "success");
                triggerVibe(50);
                roomChannel.send({
                    type: 'broadcast',
                    event: 'quiz_fast_winner',
                    payload: { playerId: myPlayerId, playerName: players.find(p => p.id === myPlayerId)?.name || 'Anonyme' }
                });
                if (isRoomAdmin) nextQuizQuestion();
            } else {
                showToast("Faux ! ❌", "error");
                triggerVibe([50, 50]);
            }
        }

        function submitQuizAnswer() {
            const input = document.getElementById('quiz-answer-input');
            const text = input.value.trim();
            if (!text) {
                shakeInput('quiz-answer-input');
                return;
            }
            
            triggerVibe(30);
            document.getElementById('quiz-input-zone').style.display = 'none';
            document.getElementById('quiz-wait-message').style.display = 'block';
            
            roomChannel.send({
                type: 'broadcast',
                event: 'quiz_submit_answer',
                payload: { playerId: myPlayerId, playerName: players.find(p => p.id === myPlayerId)?.name || 'Anonyme', text: text }
            });
        }

        function showValidationScreen() {
            const qData = quizQuestions['expert'][currentQuizIndex];
            document.getElementById('quiz-expected-text').innerText = qData.a;
            
            const list = document.getElementById('quiz-answers-to-validate');
            list.innerHTML = quizAnswersReceived.length ? quizAnswersReceived.map(ans => `
                <div style="background: rgba(255,255,255,0.05); padding: 15px; border-radius: 12px; display: flex; justify-content: space-between; align-items: center; margin-bottom:10px;">
                    <div style="flex: 1;">
                        <small style="opacity: 0.7;">${ans.playerName} :</small><br>
                        <strong>${ans.text}</strong>
                    </div>
                    <div style="display: flex; gap: 5px;">
                        <button class="btn-add" style="background: #30d158; width: 40px; border:none; border-radius:8px; color:white;" onclick="validateQuizPlayer('${ans.playerId}', true, this)">✅</button>
                        <button class="btn-add" style="background: #ff3b30; width: 40px; border:none; border-radius:8px; color:white;" onclick="validateQuizPlayer('${ans.playerId}', false, this)">❌</button>
                    </div>
                </div>
            `).join('') : "<p style='text-align:center; opacity:0.5;'>Aucune réponse reçue...</p>";
            
            switchView('quiz-view', 'quiz-validation-view');
        }

        function validateQuizPlayer(playerId, isCorrect, btn) {
            triggerVibe(30);
            btn.parentElement.innerHTML = isCorrect ? "<span style='color:#30d158;'>Validé ✅</span>" : "<span style='color:#ff3b30;'>Faux ❌</span>";
            
            roomChannel.send({
                type: 'broadcast',
                event: 'quiz_verdict',
                payload: { playerId: playerId, isCorrect: isCorrect }
            });
        }

        function nextQuizQuestion() {
            currentQuizIndex++;
            if (currentQuizIndex < 10) {
                quizAnswersReceived = [];
                roomChannel.send({
                    type: 'broadcast',
                    event: 'quiz_next',
                    payload: { index: currentQuizIndex }
                });
                loadQuizQuestion();
            } else {
                roomChannel.send({ type: 'broadcast', event: 'quiz_end', payload: {} });
                showToast("Quiz terminé ! Bravo à tous 🏆", "success");
                returnToMenu(currentViewId);
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
"""

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace everything from "let currentGame = '';" to the end of script
match = re.search(r'        let currentGame = \'\';\n.*?(?=    </script>)', content, flags=re.DOTALL)
if match:
    content = content[:match.start()] + new_js + content[match.end():]
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(content)
    print("Injected logic successfully!")
else:
    print("Logic anchor not found.")
