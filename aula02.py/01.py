# representando uma pessoa como lista
# convenciono a ordem: nome, cidade, ano de nascimento
pessoa = ['Samuel', 'Sao Paulo', 1990]

# para acessar um campo, preciso lembrar sua posição
print('cidade de residencia:', pessoa[1])

# representando pessoa como um dicionário
pessoa = {}

pessoa['nome'] = 'Samuel'
pessoa['cidade'] = 'Sao Paulo'
pessoa['ano_nascimento'] = 1990 # dado int

print('cidade de residencia:', pessoa['cidade'])
