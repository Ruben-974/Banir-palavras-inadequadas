
similar = ['a', '4', '@'], ['e', '3', '&'], ['i', '1', '!'], ['o', '0'] # Caracteres similares
inadequado = ['4', '@', '3', '&', '1', '!', '0'] # Caracteres inadequados

txt = '@bbe3&&lllhhaaa@4@4a'.lower()

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

if txt_temp[0] == txt_temp[-1] and len(dell) != 0:
    txt_temp = txt_temp.replace(dell, '', 1) # Repetidos = Principal | Ex: 'eeeeee' = 'e'

txt = txt_temp

print(txt)