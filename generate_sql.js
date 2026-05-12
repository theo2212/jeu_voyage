const fs = require('fs');
const code = fs.readFileSync('app.js', 'utf8');

const phrasesMatch = code.match(/const phrases = (\{[\s\S]*?\n\};)/);
const phrasesStr = phrasesMatch[1];
let phrasesObj;
eval('phrasesObj = ' + phrasesStr);

let sql = 'INSERT INTO public.phrases (theme, game_mode, content) VALUES\n';
let values = [];

for (const theme in phrasesObj) {
    for (const gameMode in phrasesObj[theme]) {
        for (const text of phrasesObj[theme][gameMode]) {
            const escapedText = text.replace(/'/g, "''");
            values.push(`('${theme}', '${gameMode}', '${escapedText}')`);
        }
    }
}

sql += values.join(',\n') + ';';
fs.writeFileSync('insert_phrases.sql', sql);
console.log('Fichier SQL genere.');
