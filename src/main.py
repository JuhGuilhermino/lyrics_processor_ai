from tokenizer import tokenizer
from categorize import categorize
#from src import mask
#from src import difficulty

import pandas as pd

def main():
    data = pd.read_csv("data/test.csv", nrows=1)
    lyrics = data.iloc[0]["lyrics"]

    # PASSO 1: classificar letra
    category, score = categorize(lyrics)

    # PASSO 2: tokenizar versos
    tokens = tokenizer(lyrics)

    # PASSO 3: difinir laculas

    # PASSO 4: definir grau de dificuldade das palavras

    # PASSO 5: salvar mascara

    
    # TESTES RÁPIDOS
    print (category);
    print (score);
    for i in tokens:
        print(i)



if __name__ == "__main__":
    main()
