import json

phrases = {'soft': {}, 'hard': {}}
try:
    with open('insert_phrases.sql', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if not line.startswith("('"): continue
            
            # Simplified parsing for the specific SQL format
            # Format: ('theme', 'game', 'content'),
            parts = line.strip("(),;").split("', '")
            if len(parts) < 3: continue
            
            theme = parts[0].strip("'")
            game = parts[1].strip("'")
            content = parts[2].strip("'").replace("''", "'")
            
            if theme not in phrases: phrases[theme] = {}
            if game not in phrases[theme]: phrases[theme][game] = []
            phrases[theme][game].append(content)

    all_count = sum(len(games) for theme in phrases.values() for games in theme.values())
    print(f"Extraction réussie : {all_count} catégories trouvées.")
    
    # Calculate total phrases
    total = sum(len(p_list) for theme in phrases.values() for p_list in theme.values())
    print(f"Total phrases : {total}")

    with open('phrases_dump.json', 'w', encoding='utf-8') as f:
        json.dump(phrases, f, ensure_ascii=False, indent=4)
except Exception as e:
    print(f"Erreur : {e}")
