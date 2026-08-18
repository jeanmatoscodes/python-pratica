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

# Controle de vendas
# Uso de repetição, condicionais, acumulador e contador

total = 0
atingiram_meta = 0

for numero in range(1, 6):
    nome = input(f"Digite o nome do vendedor {numero}: ")
    valor_vendido = float(input("Digite o valor vendido: "))

    total = total + valor_vendido

    if valor_vendido < 1000:
        print("Abaixo da meta")

    elif valor_vendido <= 3000:
        atingiram_meta = atingiram_meta + 1
        print("Meta atingida")

    else:
        atingiram_meta = atingiram_meta + 1
        print("Meta superada")

print(f"Valor vendido pela equipe: R$ {total:.2f}")
print(f"Vendedores que atingiram a meta: {atingiram_meta}")


# Controle de desempenho de funcionários
# Uso de repetição, condicionais e dois contadores

funcionario_desempenho = 0
funcionario_atencao = 0

for numero in range(1, 7):
    nome = input(f"Digite o nome do funcionário {numero}: ")
    faltas = int(input("Digite a quantidade de faltas mensal: "))

    if faltas == 0:
        funcionario_desempenho = funcionario_desempenho + 1
        print("Excelente")

    elif faltas <= 2:
        print("Regular")

    else:
        funcionario_atencao = funcionario_atencao + 1
        print("Atenção")

print(f"Funcionários com desempenho excelente: {funcionario_desempenho}")
print(f"Funcionários em atenção: {funcionario_atencao}")


# Controle de acesso
# Uso de condição AND e tratamento de texto

setor = input("Digite seu setor: ").strip().upper()
idade = int(input("Digite sua idade: "))

if setor == "TI" and idade >= 18:
    print("Acesso autorizado")

else:
    print("Acesso negado")