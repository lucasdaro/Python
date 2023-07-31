from sistema import opcao_selecionada

print("*" * 50)
print("=" * 50)
print(" " * 15, "SEJA BEM VINDO")
print("=" * 50)
print("*" * 50)
print("-" * 50)
print("[1] Para Ver Clientes Cadastrados")
print("[2] Para Cadastrar Novo Cliente")
print("[3] Para Excluir um Cadastro")
print("[4] Para Sair")
print("-" * 50)

while True:
    opcao = input()

    if not opcao.isdigit() or int(opcao) > 4 or int(opcao) < 1:
        print("Opção Invalida, Tenta Novamente")
    else:
        opcao = int(opcao) 
        break


opcao_selecionada(opcao)