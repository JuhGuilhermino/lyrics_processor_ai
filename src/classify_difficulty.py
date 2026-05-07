from wordfreq import zipf_frequency

def classify_difficulty(tokens, mask):
    classified_mask = []

    for token_line, mask_line in zip(tokens, mask):

        new_mask_line = []

        for word, mask_value in zip(token_line, mask_line):

            # mantém palavras fixas
            if mask_value == 0:
                new_mask_line.append(0)

            # classifica apenas palavras marcadas com  1 (lacunas da atividade)
            elif mask_value == 1:

                freq = zipf_frequency(word, "en")

                if freq > 5:
                    new_mask_line.append(1) # fácil
 
                elif freq > 3:
                    new_mask_line.append(2) # média
 
                else:
                    new_mask_line.append(3) # difícil

        classified_mask.append(new_mask_line)

    return classified_mask