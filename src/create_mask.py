from sentence_transformers import SentenceTransformer, util
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def create_mask(tokens):
    mask = []

    for line in tokens:
        if not line:
            mask.append([])
            continue

        text = " ".join(line)

        emb_line = model.encode(text, convert_to_tensor=True)

        emb_words = model.encode(line, convert_to_tensor=True)

        scores = util.cos_sim(emb_words, emb_line)

        scores = scores.cpu().numpy().flatten()

        # Monstagem da mascara
        idx_relevante = int(np.argmax(scores))
        mascara = [0] * len(line)
        mascara[idx_relevante] = 1

        mask.append(mascara)

    return mask