# Lyrics Dataset Generator with NLP e ML
Este projeto foi desenvolvido por Júlia Guilhermino para disiciplina DIM0162 - Engenharia de Software, no ano de 2026.
O objetivo era gerar a base de dados para oum sistema de aprendizado de inglês com música, chamado [LyricsFlow](https://github.com/JuhGuilhermino/lyricsflow_backend). Dada uma letra de entrada, esse programa gera uma máscara que será usada como gabarito para as atividades do sistema e consequêntemente nas demais funcionalidades.

## Funcionalidades
1. Coletar de forma automática letras de música, usando a [Genius API](https://docs.genius.com/#/resources-h1)
2. Limpar ruídos das letras
3. Gerar da máscara da atividade de cada letra
    1. Classifição do vocabulário (study, leisure, travel), usando [sentence-transformers](https://sbert.net)
    2. Tokenização dos versos
    3. Identificação das palavras mais relevantes por verso, usando [sentence-transformers](https://sbert.net)
    4. Identificação do grau de dificuldade das palavras relevantes, usando [wordfreq](https://pypi.org/project/wordfreq/)
4. Salvar os dados em uma dataset.

## Máscara
Cada símbolo da máscara corresponde a uma palavra da letra da música:
    0 =  palavras fixas;
    1 = lacuna para atividades do nível fácil.
    2 = lacuna para atividades do nível intermediário.
    3 = lacuna para atividades do nível difícil.
#### Exemplo    
```
Verso: ['any', 'way', 'the', 'wind', blows']
Máscara: [0 ,0 ,0 ,2, 0]
```

## Melhorias
- [ ] Filtrar melhro as categorias das músicas.
- [ ] Refinar processo de criação de lacunas.
- [ ] Extrair outros dados relevantes sobre as músicas.

