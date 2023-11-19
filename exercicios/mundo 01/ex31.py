km = float(input('Insira a distância da viagem: '))

preço = km * 0.50 if km <= 200 else km * 0.45
print(f'Você irá fazer uma viagem de {km}km.\n\
Ela irá custar R${preço}')