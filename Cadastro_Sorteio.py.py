# Importa a classe 'datetime' do módulo 'datetime'
from datetime import datetime

# Importa o módulo 'random' para geração de valores aleatórios
import random

# Exibe uma mensagem de boas-vindas
print("   Olá, bem-vindo a nossa empresa   ")

# Solicita ao usuário que digite seu nome e armazena na variável 'nome'
nome = input("Digite seu nome:")

# Solicita ao usuário que digite sua idade e converte para um número inteiro, armazenando em 'idade'
idade = int(input("Digite sua idade:"))

# Obtém a data e hora atuais e armazena na variável 'data_cadastro'
data_cadastro = datetime.now()

# Lista de valores de cartões
cartoes = ["R$50,00", "R$250,00", "R$120,00"]

# Escolhe aleatoriamente um valor da lista de cartões e armazena em 'cartao'
cartao = random.choice(cartoes)

# Solicita ao usuário que digite sua data de aniversário e converte para um objeto datetime, armazenando em 'aniversario'
aniversario = datetime.strptime(
    input("Digite sua data de aniversário no formato dd/mm/aaaa:"),
    "%d/%m/%Y")

# Exibe uma mensagem de boas-vindas personalizada com o nome do usuário e a data de cadastro
print(f"Olá {nome}, seu registro foi concluído com sucesso no dia {data_cadastro.day}/{data_cadastro.month}/{data_cadastro.year}.")

# Exibe uma mensagem informando que o usuário ganhou um cartão de compras com valor aleatório
print(f"Parabéns, houve um sorteio e você ganhou um cartão de compras no valor de {cartao}")
