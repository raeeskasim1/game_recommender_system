# import pandas as pd
# import numpy as np
# import difflib
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# import pickle

# df=pd.read_csv(r"C:\Users\HP\OneDrive\Desktop\project\recommend system\model\imdb-videogames.csv")

# genre_cols = ['Action', 'Adventure', 'Comedy', 'Crime', 'Family','Fantasy', 'Mystery', 'Sci-Fi', 'Thriller']

# df['genres'] = df.apply(lambda row: ' '.join([genre for genre in genre_cols if row[genre] == True]), axis=1)

# df = df[['name', 'plot', 'genres', 'rating', 'certificate']]

# selected_features=['plot','genres','rating','certificate']
# for feature in selected_features:
#   df[feature]=df[feature].fillna('')
#   df[feature] = df[feature].astype(str)
# combined_features=df['plot']+' '+df['genres']+' '+df['rating']+' '+df['certificate']

# vectorizer = TfidfVectorizer()
# feature_vectors= vectorizer.fit_transform(combined_features)
# similarity=cosine_similarity(feature_vectors)

# # with open('model/similarity.pkl', 'wb') as f:
# #     pickle.dump(similarity, f)

# # with open('model/df.pkl', 'wb') as f:
# #     pickle.dump(df, f)

# df.to_feather("model/df.feather")

# print("✅ Saved similarity and df to pickle.")