def tokenizer(data):
    lyrics = data.split("\n")
    all_tokens = []

    for line in lyrics:
        line = line.strip().lower()
        
        if not line:
            continue
        
        tokens = line.split()
        all_tokens.append(tokens)

    return all_tokens
  

