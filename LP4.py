soma = 0
quantidade_numeros = 0

while True:
    numero = int(input("Digite um número ou 0 para sair: "))
    if numero == 0:
        break
    soma += numero
    quantidade_numeros += 1
if quantidade_numeros > 0:
    media = soma / quantidade_numeros
    print(f"Quantidade de números digitados: {quantidade_numeros}")
    print(f"Soma dos números: {soma}")
    print(f"Média dos números: {media:.2f}")
else:
    print("SAIR.")