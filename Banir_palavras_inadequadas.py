
similar = ['a', '4', '@'], ['e', '3', '&'], ['i', '1', '!'], ['o', '0'] # Caracteres similares
inadequado = ['4', '@', '3', '&', '1', '!', '0'] # Caracteres inadequados


txt = 'Abbe3&&lhaaa@4@4a' # Texto para ser analizado
txt = txt.lower() # Deixando o txt em minusculo 

lista_caracters = []

for c in txt: 
    lista_caracters.append(c) # Adicioando todos caracteres de "txt" na lista "lista_caracters"

for c in range(len(similar)): 
    for c1 in range(len(lista_caracters)): 
        if lista_caracters[c1] in similar[c]: # Se o caracter da "lista_caracters" estiver no item "similar"
            lista_caracters[c1] = similar[c][0] # O caracter similar recebe o caracter original

txt = ''.join(lista_caracters) # "txt" recebe o conteúdo da "lista_caracters" junto

