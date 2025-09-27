# Game Recommendation System

A **Flask-based game recommendation system** that suggests video games based on plot, genre, rating, and certificate. Users can search for games, view game details, and explore recommended games with images.

## Features

- **Search with suggestions**: Autocomplete search bar for quick game lookup.
- **Game listing**: Browse all available games with images.
- **Game details page**: View detailed information, plot, genre, rating, and recommended games.
- **Image handling**: Automatic fallback for missing images.
- **Recommendation engine**: Uses **TF-IDF vectorization** and **cosine similarity** for content-based recommendations.

## Project Structure
project/  
│  
├─ model/  
│   ├─ df.feather              # Preprocessed game dataframe   
│   ├─ similarity.pkl          # Cosine similarity matrix (generated)  
│   └─ logic.py                # Recommendation logic  
│  
├─ static/  
│   └─ game_images/            # Game images folders  
│   
├─ templates/   
│   ├─ welcome.html            # Landing page   
│   ├─ games.html              # Game listing page  
│   └─ game_detail.html        # Game detail page  
│  
├─ app.py                      # Flask application  
├─ pickle.py                    # Generates df.pkl and similarity.pkl  
└─ requirements.txt            # Python dependencies  
