
import os
import json

# Chemins des fichiers
file_path = 'games.json'
output_file = 'steam_raw_selection.json'

dataset = {}
if os.path.exists(file_path):
    with open(file_path, 'r', encoding='utf-8') as fin:
        text = fin.read()
        if len(text) > 0:
            dataset = json.loads(text)

final_list = []

print("Extraction des colonnes stratégiques...")

for appID in dataset:
    game = dataset[appID]
    
    # On construit l'objet en ne gardant que l'essentiel pour Power BI
    entry = {
        "AppID": appID,
        "Name": game.get('name'),
        "ReleaseDate": game.get('release_date'),
        "EstimatedOwners": game.get('estimated_owners'),
        "Price": game.get('price', 0.0),
        "ScoreRank": game.get('score_rank', ''),
        "DLCCount": game.get('dlc_count', 0),
        "MetacriticScore": game.get('metacritic_score', 0),
        "UserScore": game.get('user_score', 0),
        "Positive": game.get('positive', 0),
        "Negative": game.get('negative', 0),
        "AveragePlaytime": game.get('average_playtime_forever', 0),
        "MedianPlaytime": game.get('median_playtime_forever', 0),
        "PeakCCU": game.get('peak_ccu', 0),
        "RequiredAge": game.get('required_age', 0),
        "Publisher": game.get('publishers', ["Unknown"])[0] if game.get('publishers') else "Unknown",
        "Developer": game.get('developers', ["Unknown"])[0] if game.get('developers') else "Unknown",
        # Listes pour les dimensions Power BI
        "Genres": game.get('genres', []),
        "Tags": list(game.get('tags', {}).keys()) if isinstance(game.get('tags'), dict) else game.get('tags', []),
        "Languages": game.get('supported_languages', []),
        "FullAudio": game.get('full_audio_languages', []),
        
        # Plateformes
        "Windows": game.get('windows', True),
        "Mac": game.get('mac', False),
        "Linux": game.get('linux', False)
    }
    
    final_list.append(entry)

# Exportation en JSON
with open(output_file, 'w', encoding='utf-8') as fout:
    json.dump(final_list, fout, indent=4, ensure_ascii=False)

print(f"Extraction terminée : {len(final_list)} entrées exportées dans {output_file}")