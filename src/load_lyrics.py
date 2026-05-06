import lyricsgenius    # Acessar a API do Genius
import pandas as pd    # Manipulação dos dados e gerar o um dataset
import re              # Limpar texto
import time            # Controla o tempo de execução para evitar o bloqueio da API


GENIUS_API_KEY = "vV29NExJODiDian1SndARe00ZHcfNO6GK_v6826tKBsD2M5_mrspb66HNx1p-D7TBINQZq3ttiNEOG5gcb8baQ"
genius = lyricsgenius.Genius(GENIUS_API_KEY, timeout=15, retries=3)

# Leitura da lista de música a serem pesquisadas
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

"""
def clean_lyrics(texto):
    if not texto:
        return ""
    
    # remove [Chorus], [Verse], etc
    texto = re.sub(r"\[.*?\]", "", texto)
    
    # remove lixo comum do Genius
    texto = re.sub(r"You might also like.*", "", texto)
    
    # remove quebras de linha
    texto = texto.replace("\n", " ")
    
    # lowercase
    texto = texto.lower()
    
    # remove espaços extras
    texto = re.sub(r"\s+", " ", texto)
    
    return texto.strip()

def search_lyrics(lista_musicas):
    dados = []
    
    for titulo, artista in lista_musicas:
        print(f"Buscando: {titulo} - {artista}")
        
        try:
            song = genius.search_song(titulo, artista)
            
            if song and song.lyrics:
                letra_limpa = limpar_letra(song.lyrics)
                
                dados.append({
                    "artist": artista,
                    "title": titulo,
                    "lyrics": letra_limpa
                })
            else:
                print(f"❌ Não encontrada: {titulo}")
        
        except Exception as e:
            print(f"Erro em {titulo}: {e}")
        
        time.sleep(1)  # evita bloqueio da API
    
    return dados


def save_data(dados):
    df = pd.DataFrame(dados)
    
    # salvar CSV
    df.to_csv("data/lyrics_dataset.csv", index=False)
    
    # salvar JSON
    df.to_json("data/lyrics_dataset.json", orient="records", indent=2)
    
    print("✅ Dataset salvo em /data")
"""

def main():
    file_path = "data/songs_list.txt"
    
    list = read_file(file_path)
    #data = search_lyrics(list)
    #save_data(data)

    for i in list:
        print(i)


if __name__ == "__main__":
    main()
