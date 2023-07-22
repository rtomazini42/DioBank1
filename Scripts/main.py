import operacoesBasicas as op 

op.saldo = 1000.00
op.n_saques_do_dia = 0
usuario = ""

sair = False


def menu():
    global sair
    global usuario
    print("Escolha a opção")
    print("1 - Saque")
    print("2 - Ver saldo")
    print("3 - deposito")
    print("4 - ver extrato")
    print("5 - sair")
    escolha = input()
    try:
        escolha = int(escolha)
    except:
        print("Ocorreu um erro, por favor, digite um numero")

    if escolha == 5:
        print("Saindo")
        op.armazenar_operacao("Logout feito", usuario)
        sair = True
    if escolha == 1:
        print("Digite o valor do saque: ")
        valorSaque = input()
        try:
            valorSaque = float(valorSaque)
            print("Sacando")
            op.saque(valorSaque, usuario)
        except:
            print("operação não realizada, você digitou um numero?")
    if escolha == 2:
        op.verSaldo(usuario)
    if escolha == 3:
        print("Digite o valor do deposito: ")
        valorDeposito= input()
        try:
            valorDeposito = float(valorDeposito)
            print("Depositando")
            op.depositar(valorDeposito, usuario)
        except:
            print("operação não realizada, você digitou um numero?")
    if escolha == 4:
        op.extrato(usuario)
        




def __main__():
    global usuario
    nome = input("Digite seu usuario: ")
    senha = input("Digite seu senha: ")
    op.loga_usuario(nome,senha)
    usuario = nome
    while sair == False:
        menu()
    

__main__()


