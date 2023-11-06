frase = 'ola tudo bem?'

# FATIAMENTO
# o ultimo valor sempre é ignorado
frase[3] # mostrar o terceiro
frase[3:9] # mostrar do 3 ao 9
frase[3:9:2] # mostrar do 3 ao 9 pulando de 2 em 2
frase[:9] # do 0 ate o 9
frase[9:] # do 9 ate o final
frase[9::3] # do 9 ate o final pulando de 3 em 3

len(frase)
frase.count('o') # conta quantos 0 possui
frase.count('o', 0, 13) # conta quantos o possui do 0 ao 13 
frase.find('deo') # retorna a posição do caractere
frase.find('Android') # caso nao exista retorna o valor -1
frase.replace('ola', 'hi')
frase.upper() # torna tudo maiusculo
frase.lower() # torna tudo minusculo
frase.capitalize() # tudo pra minusculo e apenas a primeira maiuscula
frase.title() # todas as palavras em capitalize
frase.strip() # remove os espaços no fim e no inicio 
frase.lstrip() # remove os espaços a esquerda
frase.rstrip() # remove os espaços a direita
frase.split() # quebra os espaços em novas strings
'-'.join(frase) # junta as strings colocando espaços nelas

'Curso' in frase # retorna true ou false