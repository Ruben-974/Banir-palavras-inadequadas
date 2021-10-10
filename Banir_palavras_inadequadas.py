
similar = ['a', '4', '@'], ['e', '3', '&'], ['i', '1', '!'], ['o', '0'], [' ', '-', '_', '/', '|'] # Caracteres similares
inadequado = ['4', '@', '3', '&', '1', '!', '0'] # Caracteres inadequados
indesejadas = ['abelhas', 'gosto'] # palavras indesejadas

txt = '----Eeee333uuu-ggoostt00oo___dde| @bbe3&&lllhhasssss///'.lower().strip()

print(txt)

lista_caracters = []

# Irá Substituir os caracteres similares | Ex: '3' = 'e'

for c in txt: 
    lista_caracters.append(c)

for c in range(len(similar)): 
    for c1 in range(len(lista_caracters)): 
        if lista_caracters[c1] in similar[c]:
            lista_caracters[c1] = similar[c][0] # Similar = Original | Ex: @ = a

txt = ''.join(lista_caracters)

txt_temp, dell = txt, ''

# Irá substituir os caracteres repetidos em apenas um | Ex: 'aaaaaaa' = 'a'

for c in range(len(txt)):

    if c+1 < len(txt):
        if txt[c] == txt[c+1]:
            dell += txt[c]

        elif txt[c] != txt[c+1] and len(dell) != 0:
            txt_temp= txt_temp.replace(dell+dell[0], dell[0], 1) # Repetidos = Principal | Ex: 'eeeeee' = 'e'
            dell = ''

# Susbstitui os ultimos caracteres se necessario

if len(dell) > 0 and dell[0] == dell[-1]:
    txt_temp = txt_temp.replace(dell, '', 1) # Repetidos = Principal | Ex: 'eeeeee' = 'e'

txt = txt_temp.strip()

lista_palavras, palavra = [], []

# Criando uma lista só com as palavras

for c in txt:

    if c not in ' ':
        palavra.append(c)
    else:
        lista_palavras.append(''.join(palavra[:]))
        palavra = []

lista_palavras.append(''.join(palavra[:]))

# Modificando a palavra se ele for indesejada

print(txt)

for c in range(len(lista_palavras)):
    if lista_palavras[c] in indesejadas:
        lista_palavras[c] = f'{lista_palavras[c][0]}{(len(lista_palavras[c])-1)*"*"}'

txt = ' '.join(lista_palavras)

print(txt)

# Frase inicial     = ----eeee333uuu-ggoostt00oo___dde| @bbe3&&lllhhasssss///
# Frase sem censura = eu gosto de abelhas
# Frase com censura = eu g**** de a******
