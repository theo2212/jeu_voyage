import os

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

lobby_html = """
        <!-- Vue : Lobby Multijoueur -->
        <div id="lobby-view" style="display: none; flex-direction: column; align-items: center; justify-content: center; height: 100%;">
            <h1 style="color: #30d158; text-shadow: 0 0 10px rgba(48,209,88,0.5);">🌐 Mode En Ligne</h1>
            <p style="opacity: 0.8; text-align: center; margin-bottom: 30px;">
                Joue avec tes amis en synchronisant vos téléphones !
            </p>
            
            <div id="lobby-controls" style="width: 100%; display: flex; flex-direction: column; gap: 15px; margin-bottom: 30px;">
                <button class="btn-action" style="background: linear-gradient(135deg, #34c759, #30d158); color: white;" onclick="createRoom()">
                    👑 Créer un salon
                </button>
                <div style="text-align: center; font-weight: bold; opacity: 0.5;">OU</div>
                <div class="input-group" style="margin: 0; display: flex;">
                    <input type="text" id="room-code-input" class="input-text" placeholder="Code (ex: ABCD)" maxlength="4" style="text-transform: uppercase; text-align: center; flex: 1;">
                    <button class="btn-action" style="width: auto; padding: 0 20px; margin: 0; border-radius: 0 15px 15px 0;" onclick="joinRoom()">Rejoindre</button>
                </div>
            </div>

            <div id="room-waiting-area" style="display: none; width: 100%; text-align: center; background: rgba(255,255,255,0.05); padding: 20px; border-radius: 15px;">
                <h3 id="room-code-display" style="font-size: 2.5rem; letter-spacing: 5px; color: #ffd700; margin-bottom: 10px;">ABCD</h3>
                <p style="opacity: 0.8; font-size: 0.9rem;">En attente des autres joueurs...</p>
                <div id="room-players-list" style="margin: 15px 0; text-align: left; font-size: 1.1rem; color: #30d158;">
                    <!-- Liste des joueurs -->
                </div>
                <button id="btn-start-room" class="btn-action btn-next" style="display:none;" onclick="beginGame()">Lancer la partie</button>
            </div>

            <button class="btn-action btn-back" style="margin-top: 20px;" onclick="returnToMenu('lobby-view')">Retour au menu</button>
        </div>
"""

html = html.replace('<!-- Vue : Configuration Theme -->', lobby_html + '\n        <!-- Vue : Configuration Theme -->')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Lobby HTML injected.")
