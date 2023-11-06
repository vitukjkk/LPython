var = input('insira algum valor:')
print('Qual o tipo?',type(var)) # tipo
print('Tem espaços?',var.isspace()) # tem espaços?
print('É um número?',var.isnumeric()) # tem números?
print('É alfabético?',var.isalpha()) # é alfabético?
print('É alfanumérico?',var.isalnum()) # é alfanumerico?
print('É maiúscula?',var.isupper()) # é maiúscula?
print('É minúscula?',var.islower()) # é minúscula?
print('Está capitalizada?',var.istitle()) # está capitalizada (tem minúsculas e minúsculas)
