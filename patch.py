import re

with open('app.js', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Remplacer const phrases
match = re.search(r'const phrases = (\{[\s\S]*?\n\});', code)
if match:
    code = code.replace(match.group(0), 'let phrases = { soft: {}, hard: {} };')

# 2. Ajouter fetchPhrasesFromSupabase
fetch_func = """
async function fetchPhrasesFromSupabase() {
    const sb = getSupabase();
    if (!sb) return;

    try {
        const { data, error } = await sb.from('phrases').select('*');
        if (error) throw error;
        
        if (data && data.length > 0) {
            let newPhrases = {
                soft: { tribunal: [], draft: [], boire_action: [], boire_7sec: [] },
                hard: { tribunal: [], draft: [], boire_action: [], boire_7sec: [] }
            };
            
            data.forEach(row => {
                if(newPhrases[row.theme] && newPhrases[row.theme][row.game_mode]) {
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
"""

code = code.replace('function getSupabase() {', fetch_func + '\nfunction getSupabase() {')

# 3. Modifier loadState
old_load_state = """            const savedIndices = localStorage.getItem('voyage_availableIndices');
            if (savedIndices) {
                availableIndices = JSON.parse(savedIndices);
            } else {
                initIndices();
            }"""

new_load_state = """            const cached = localStorage.getItem('voyage_cached_phrases');
            if (cached) {
                phrases = JSON.parse(cached);
                const savedIndices = localStorage.getItem('voyage_availableIndices');
                if (savedIndices) {
                    availableIndices = JSON.parse(savedIndices);
                } else {
                    initIndices();
                }
            }"""

code = code.replace(old_load_state, new_load_state)

# 4. Appeler fetchPhrasesFromSupabase au demarrage
code = code.replace(
    "document.getElementById('sync-modal').style.display = 'flex';",
    "document.getElementById('sync-modal').style.display = 'flex';\n    fetchPhrasesFromSupabase();"
)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(code)

print("app.js patched.")
