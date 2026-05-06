import lyricsgenius    # Acessar a API do Genius
import pandas as pd    # Manipulação dos dados e gerar o um dataset
import re              # Limpar texto
import time            # Controla o tempo de execução para evitar o bloqueio da API


GENIUS_API_KEY = "kEml8x3ZF1xNdrhcU_LjcWaMKQq2JmguXcUkkZrKwxEhMrOJGnYu4DQahDQRheQ8"
genius = lyricsgenius.Genius(GENIUS_API_KEY, timeout=15, retries=3)

# Leitura da lista de músicas a serem pesquisadas e formata dados ára consulta na API
def read_file(path):
    songs = []
    
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            
            if not line:
                continue
            
            try: # separa as informações em (título, artista)
                title, artist = line.split(" - ") 
                songs.append((title.strip(), artist.strip()))
            except:
                print(f"[ERRO - invalid format]: {line}")
    
    return songs

# Buscar música na API
def search_lyrics(list):
    data = []
    
    for title, artist in list:
        print(f"Buscando: {title} - {artist}")
        
        try:
            song = genius.search_song(title, artist)
            
            if song and song.lyrics:
                lyrics = clean_lyrics(song.lyrics)
                
                data.append({
                    "artist": artist,
                    "title": title,
                    "lyrics": lyrics
                })
            else:
                print(f"[ERRO]: Música {title} não encontrada")
        
        except Exception as e:
            print(f"Erro em {title}: {e}")
        
        time.sleep(1)  # evita bloqueio da API
    
    return data

# Padronização da letra da música
def clean_lyrics(text):
    if not text:
        return ""
    
    text = re.sub(r"\[.*?\]", "", text)
    text = re.sub(r"You /might also like.*", "", text)
    text = text.lower()
    #text = re.sub(r"\s+", " ", text)
    text = re.sub(r"\n\s*\n+", "\n", text)
    
    return text.strip()

# Salvar dados em um dataset
def save_data(data):
    df = pd.DataFrame(data)
    
    # salvar CSV
    df.to_csv("data/test.csv", index=False)


def main():
    file_path = "data/test.txt"
    
    list = read_file(file_path)
    data = search_lyrics(list)
    save_data(data)

    #for i in list:
    #    print(i)

    #print(data[0])

    
    # teste da chave da API
    #song = genius.search_song("Yellow", "Coldplay")
    #lyrics = clean_lyrics(song.lyrics)
    #if song:
    #    print(lyrics)
    #else:
    #    print("ERRO")
    

if __name__ == "__main__":
    main()
