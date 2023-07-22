import os
import time


#usuario = ""
saldo = 1000.00
n_saques_do_dia = 0

def loga_usuario(name,senha):
    usuario = name
    senha = senha # sem considerar por enquanto
    linha = usuario + " logou" 
    print("Logado com sucesso")
    armazenar_operacao(linha, usuario)



def armazenar_operacao(linha, usuario):
    try:
        # Verifica se a pasta "Registros" existe, se não, cria a pasta
        if not os.path.exists("Registros"):
            os.makedirs("Registros")

        data_hora = time.strftime("%Y-%m-%d %H:%M:%S")

        # Formata a linha com a data e hora e o conteúdo fornecido
        linha_formatada = f"{data_hora}: {linha}"

        # Abre o arquivo na pasta "Registros" em modo de escrita ('w' para sobrescrever ou 'a' para acrescentar)
        with open(os.path.join("Registros", usuario + '.txt'), 'a') as arquivo:
            arquivo.write(linha_formatada + '\n')
        print("Operação registrada")
    except Exception as e:
        print(f"Ocorreu um erro ao armazenar a operação: {e}")




def saque(saque,usuario):
    global saldo
    if saque > 500.00:
        print("Operação não pode ser realizada pois temos um limite de R$500,00 por saque")
    if saque > saldo:
        print("Operação não pode ser realizada pois limite de saldo é menor que o saque")
    if saque < saldo:
        saldo -= saque
        print("Sacando {:.2f}".format(saque))
        linha = "Foi sacado {:.2f} da conta de ".format(saque) + usuario
        armazenar_operacao(linha, usuario)

def verSaldo(usuario):
    armazenar_operacao("consultou o saldo " , usuario)
    print("Usuario " + usuario + "Tem de saldo: "  + str(saldo))

def depositar(valor,usuario):
    global saldo
    if valor > 0:
        print("Realizando deposito")
        saldo = saldo + valor
        linha = "Adicionado deposito de de R$" + str(valor) + " na conta. Valor atual: R$" + str(saldo)
        armazenar_operacao(linha, usuario)

def extrato(usuario):
    try:
        # Abre o arquivo do usuário em modo leitura ('r')
        with open(os.path.join("Registros", usuario + '.txt'), 'r') as arquivo:
            # Lê todas as linhas do arquivo
            linhas = arquivo.readlines()

        # Pega as últimas 5 linhas (ou menos, se houver menos de 5 linhas no arquivo)
        ultimas_linhas = linhas[-5:]

        # Imprime as últimas linhas
        print("Extrato do usuário", usuario)
        for linha in ultimas_linhas:
            print(linha.strip())  # Utiliza strip() para remover a quebra de linha
        armazenar_operacao("Consultou extrato", usuario)

    except Exception as e:
        print(f"Ocorreu um erro ao listar o extrato: {e}")
