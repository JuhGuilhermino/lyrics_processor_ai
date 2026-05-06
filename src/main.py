from tokenizer import tokenizer
from classify_category import categorize
from create_mask import create_mask
from classify_difficulty import classify_difficulty

import pandas as pd
import json

def main():
    data = pd.read_csv("data/test.csv", nrows=1)
    lyrics = data.iloc[0]["lyrics"]

    # PASSO 1: classificar letra
    category, score = categorize(lyrics)

    # PASSO 2: tokenizar versos
    tokens = tokenizer(lyrics)

    # PASSO 3: difinir laculas
    mask = create_mask(tokens)

    # PASSO 4: definir grau de dificuldade das palavras
    final_mask = classify_difficulty(tokens, mask)

    # PASSO 5: salvar mascara
    dataset = []
    dataset.append({
            "artist": data.iloc[0]["artist"],
            "title": data.iloc[0]["title"],
            "category": category,
            "category_score": score,
            "lyrics": data.iloc[0]["lyrics"],
            "mask": final_mask
        })
        

    df = pd.DataFrame(dataset)

    df.to_csv("data/test_with_mask.csv", index=False)
    
    # TESTES RÁPIDOS
    #print (category);
    #print (score);
    #for i in tokens:
    #    print(i)
    #
    #for i in final_mask:
    #    print(i)



if __name__ == "__main__":
    main()
