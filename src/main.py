from tokenizer import tokenizer
from classify_category import categorize
from create_mask import create_mask
from classify_difficulty import classify_difficulty

import pandas as pd

def main():
    data = pd.read_csv("data/songs_list.csv")

    dataset = []

    for _, row in data.iterrows():
        lyrics = row["lyrics"]

        # PASSO 1: classificar letra
        category, score = categorize(lyrics)

        # PASSO 2: tokenizar versos
        tokens = tokenizer(lyrics)

        # PASSO 3: criar máscara base
        mask = create_mask(tokens)

        # PASSO 4: dificuldade das palavras
        mask2 = classify_difficulty(tokens, mask)

        # transforma em string
        final_mask = "\n".join(
            "".join(map(str, line)) for line in mask2
        )

        # PASSO 5: salvar
        dataset.append({
            "artist": row["artist"],
            "title": row["title"],
            "category": category,
            "category_score": score,
            "lyrics": lyrics,
            "mask": final_mask
        })


    df = pd.DataFrame(dataset)
    df.to_csv("data/lyrics.csv", index=False)

if __name__ == "__main__":
    main()