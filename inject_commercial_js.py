import re

commercial_js = """
// --- SUPABASE & MULTIJOUEUR ---
const SUPABASE_URL = 'https://pzdbkegmbxsvabkvffdi.supabase.co';
const SUPABASE_ANON_KEY = 'sb_publishable_esYFZqPxzRx24Wh_VrGFqQ_QybEoy_w';
let supabase = null;
let isPremium = localStorage.getItem('voyage_premium') === 'true';
let syncMode = localStorage.getItem('voyage_sync_mode'); // 'online' ou 'offline'

if (window.supabase) {
    supabase = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);
}

document.addEventListener('DOMContentLoaded', () => {
    if (!syncMode) {
        document.getElementById('sync-modal').style.display = 'flex';
    }
});

function chooseSync(mode) {
    syncMode = mode;
    localStorage.setItem('voyage_sync_mode', mode);
    document.getElementById('sync-modal').style.display = 'none';
    if(mode === 'online') {
        alert("Le multijoueur sera bientôt activé ! Pour l'instant, profitez de la sauvegarde en ligne.");
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

    if (!supabase) {
        alert("Erreur de connexion à la base de données.");
        return;
    }

    try {
        const { error } = await supabase.from('pending_phrases').insert([
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
"""

with open("app.js", "a", encoding="utf-8") as f:
    f.write(commercial_js)

print("Commercial logic injected into app.js")
