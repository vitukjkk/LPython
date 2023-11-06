from random import choice
one = str(input("Insira o nome do primeiro aluno: "))
two = str(input("Insira o nome do segundo aluno: "))
tree = str(input("Insira o nome do terceiro aluno: "))
four = str(input("Insira o nome do quarto aluno: "))

lista = [one, two, tree, four]
print("o aluno escolhido foi: {}".format(choice(lista)))

# choice escolhe um valor