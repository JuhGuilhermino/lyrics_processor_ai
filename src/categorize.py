from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")
categories = ["study", "work", "travel"]
emb_categories = model.encode(categories, convert_to_tensor=True)


def categorize(lyrics):

    emb_lyrics = model.encode(lyrics, convert_to_tensor=True)
    
    scores = util.cos_sim(emb_lyrics, emb_categories)
  
    idx = scores.argmax()
    
    return categories[idx], scores.tolist()