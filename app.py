from flask import Flask, render_template,jsonify,request
from model.logic import recommend_games,df,similarity
import os
import re

app=Flask(__name__)

IMAGE_DIR = 'static/game_images'


# Cache all game image folders and images at startup
def build_image_lookup():
    image_lookup = {}
    for game_folder in os.listdir(IMAGE_DIR):
        folder_path = os.path.join(IMAGE_DIR, game_folder)
        if os.path.isdir(folder_path) and os.listdir(folder_path):
            clean_name = re.sub(r'[^A-Za-z0-9_]', '', game_folder.replace(" ", "_"))
            image_lookup[clean_name] = os.listdir(folder_path)[0]
    return image_lookup

image_map = build_image_lookup()

def get_games_with_images():
    games = []
    for folder, image_file in image_map.items():
        games.append({
            "name": folder.replace("_", " "),
            "folder": folder,
            "image": f"{IMAGE_DIR}/{folder}/{image_file}".replace("\\", "/")
        })
    return games

@app.route('/suggest')
def suggest():
    from flask import request, jsonify
    q = request.args.get('q', '').lower()
    if not q:
        return jsonify([])

    seen = set()
    valid_names_with_images = []

    for name in df['name'].tolist():
        folder = re.sub(r'[^A-Za-z0-9_]', '', name.replace(" ", "_"))
        if name.lower().startswith(q) and folder in image_map and name not in seen:
            valid_names_with_images.append(name)
            seen.add(name)

    return jsonify(valid_names_with_images[:10])




@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/games')
def games():
    games=get_games_with_images()
    return render_template('games.html',games=games)


@app.route('/game/<game_name>')
def game_detail(game_name):

    matched_name, recommended_names = recommend_games(game_name, max_results=300)
    if not matched_name:
        return "Game not found", 404

    game_row = df[df['name'] == matched_name]
    game = game_row.iloc[0]
    

    image_folder = re.sub(r'[^A-Za-z0-9_]', '', game['name'].replace(" ", "_"))
    image_file = image_map.get(image_folder)
    if not image_file:
        image_path = "/static/no-image.png"  # fallback
    else:
        image_path = f"/static/game_images/{image_folder}/{image_file}"
    
    recommended_games = []
    seen = set()
    count = 0
    max_needed = 5
    i = 0

    # Loop through more than needed to ensure we get 10 with images
    while count < max_needed and i < len(recommended_names):
        name = recommended_names[i]
        i += 1

        if name in seen:
            continue
        seen.add(name)

        folder = re.sub(r'[^A-Za-z0-9_]', '', name.replace(" ", "_"))
        image_file = image_map.get(folder)
        if image_file:
            image_url = f"/static/game_images/{folder}/{image_file}"
            recommended_games.append({"name": name, "image": image_url})
            count += 1
    return render_template("game_detail.html", game=game.to_dict(), image=image_path, recommended=recommended_games)






if __name__ == "__main__":
    app.run(debug=False)
