
import pandas as pd
import pickle
import difflib


import time
start = time.time()

# Load from pickle
with open('model/similarity.pkl', 'rb') as f:
    similarity = pickle.load(f)
print("✅ df loaded in", time.time() - start)

# start = time.time()
# df = pd.read_feather("model/df.feather")
# # with open('model/df.pkl', 'rb') as f:
# #     df = pickle.load(f)
# print("✅ similarity loaded in", time.time() - start)


# Load from pickle instead of feather
with open("model/df.pkl", "rb") as f:
    df = pickle.load(f)

print("✅ similarity loaded in", time.time() - start)
    
def recommend_games(game_name,max_results=300):
    list_of_all_titles = df['name'].tolist()
    find_close_match = difflib.get_close_matches(game_name, list_of_all_titles)
    if not find_close_match:
        return []
    close_match=find_close_match[0]
    index_of_the_games=df[df.name==close_match].index[0]
    similarity_score=list(enumerate(similarity[index_of_the_games]))
    sorted_similar_games=sorted(similarity_score,key=lambda x:x[1],reverse = True)
    
    recommended_games=[]
    seen=set([close_match])

    for i in sorted_similar_games:
        index=i[0]
        game_name=df.iloc[index]['name']
        if game_name not in seen:
            recommended_games.append(game_name)
            seen.add(game_name)
        if len(recommended_games)>=max_results:
            break
    return close_match,recommended_games

