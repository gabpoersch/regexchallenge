import re

# Texto original do desafio
texto = "123, 2-234000, ABXD234234 e 23000"

# Separar os tokens
tokens = texto.replace(',', '').split()

# Filtrar por somente tokens que contêm números para excluir o "e" para otimizar o processamento dos dados
tokens_numeros = [token for token in tokens if re.search(r'\d', token)]

# Loop para garantir que todos os tokens numéricos terminem em 000
for i in range(len(tokens_numeros)):
    token = tokens_numeros[i]
    if token.isnumeric() and re.search(r'\d+$', token) and not token.endswith("000"):
        token += "000"
        tokens_numeros[i] = token

# Loop para processar cada token
for token in tokens_numeros:
    if '-' in token:
        # Se o token contiver um hífen, adicione zeros à esquerda do número e à direita do hífen
        parts = token.split('-')
        if len(parts) == 2 and parts[1].isnumeric():
            parts[1] = parts[1].rjust(10, '0')
            token = '-'.join(parts)
        print(token)
    elif token.isnumeric():
        # Se o token for composto apenas por dígitos, adicione zeros à esquerda
        token = token.rjust(10, '0')
        print(f"1-{token}")
    else:
        # Caso contrário, imprima o token sem modificações
        print(f"1-{token}")

# Existe uma validação extra que poderia ser feita para garantir que os tokens tenham 10 caracteres
# sem contar o hífene o que o antecede, mas não a implementei.
