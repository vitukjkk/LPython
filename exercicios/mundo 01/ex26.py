frase = str(input('Digite uma frase: ')).upper()

print(f'A letra A aparece {frase.count("A")} vezes na frase.\n\
A primeira letra A aparece na posição {frase.find("A") + 1}.\n\
A última letra A aparece na posição {frase.rfind("A") + 1}')