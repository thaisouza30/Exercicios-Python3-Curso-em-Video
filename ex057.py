sexo = str(input('Informe o seu sexo : [F/M] ')).strip().upper()[0]
while sexo not in 'FM':
    sexo = str(input('Opção inválida, digite novamente:')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
