# Condicional simples - if e else

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")


# Condicionais - if, elif e else

compra = float(input("Digite o valor da compra: "))

if compra <= 100:
    desconto = 0
elif compra <= 300:
    desconto = compra * 0.05
elif compra <= 500:
    desconto = compra * 0.10
else:
    desconto = compra * 0.15

valor_final = compra - desconto

print(f"Desconto: R$ {desconto:.2f}")
print(f"Valor final: R$ {valor_final:.2f}")


# Condicionais com and e or

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
cargo = input("Digite seu cargo: ").lower()

if idade >= 18 and cargo == "gerente":
    print("Acesso liberado!")
elif cargo == "diretor" or cargo == "administrador":
    print("Acesso liberado!")
else:
    print("Acesso negado!")


# Repetição com for e range

for numero in range(1, 11):
    print(numero)


# For + if - números pares

for numero in range(1, 21):
    if numero % 2 == 0:
        print(numero)


# Acumulador - total de vendas

total = 0

for dia in range(1, 4):
    venda = float(input(f"Digite a venda do dia {dia}: "))
    total = total + venda

print(f"Total vendido: R$ {total:.2f}")