from random import shuffle

one = str(input("qual o nome do primeiro?"))
two = str(input("qual o nome do segundo?"))
tree = str(input("qual o nome do terceiro?"))
four = str(input("qual o nome do quarto?"))

lista = [one, two, tree, four]
shuffle(lista)

print("a ordem da lista é {}".format(lista))