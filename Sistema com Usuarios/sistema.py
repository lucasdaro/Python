from Usuario import Usuario

def busca_banco():
    with open("bancodedados.txt", encoding = "utf-8") as dados_banco: #referenciando arquivo
        lista_usuarios = []
        for linha in dados_banco:
            dados_usuario = linha.strip().split(',')
            if len(dados_usuario) < 9:
                print(f"Linha problemática: {linha}")
            else:
                novo_usuario = Usuario(dados_usuario[0], dados_usuario[1], dados_usuario[2], dados_usuario[3], dados_usuario[4], dados_usuario[5], dados_usuario[6], dados_usuario[7], dados_usuario[8])
                lista_usuarios.append(novo_usuario)
    return lista_usuarios 

def ver_cadastro(lista_usuarios):
    print("Entrou Para Ver Cadastro")
    for usuario in lista_usuarios:
       usuario.exibir_dados()

def cadastrar(lista_usuarios):
    print("Entrou Para Cadastrar")
    form_cadastro = formulario_cadastro()
    lista_email = []
    for usuario in lista_usuarios:
        lista_email.append(usuario.retorna_email().strip().lower())
    
    email = form_cadastro[1]
    if email in lista_email:
        print("Usuario Já Cadastrado")
    else:
        novo_usuario = Usuario(form_cadastro[0], form_cadastro[1], form_cadastro[2], form_cadastro[3], form_cadastro[4], form_cadastro[5], form_cadastro[6], form_cadastro[7], form_cadastro[8])
        with open("bancodedados.txt", 'a', encoding = "utf-8") as dados_banco:
            dados_usuario = novo_usuario.extrair_dados()
            dados_banco.write(','.join(dados_usuario) + '\n')

        dados_banco.close()
        print("Usuário cadastrado com sucesso!")
    

def formulario_cadastro():
    nome = input("Digite o Nome: ")
    email = input("Digite o Email: ")
    data_nasci = input("Digite a Data de Nascimento: ")
    telefone = input("Digite o Telefone: ")
    rua = input("Digite a Rua: ")
    numero = input("Digite o Numero: ")
    bairro = input("Digite o Bairro: ")
    cidade = input("Digite a Cidade: ")
    estado = input("Digite o Estado: ")
    form_cadastro = [nome, email, data_nasci, telefone, rua, numero, bairro, cidade, estado]
    return form_cadastro


def excluir(lista_usuarios):
    print("Entrou Para Excluir")
    lista_email = []
    for usuario in lista_usuarios:
        lista_email.append(usuario.retorna_email().strip().lower())
    
    email = input("Digite o Email: ")
    if email in lista_email:
        # Abrir o arquivo no modo leitura
        with open("bancodedados.txt", 'r', encoding = "utf-8") as dados_banco:
            linhas = dados_banco.readlines()

        # Reabrir o arquivo no modo escrita e escrever todas as linhas, exceto a que contém o email
        with open("bancodedados.txt", 'w', encoding = "utf-8") as dados_banco:
            for linha in linhas:
                if email not in linha:
                    dados_banco.write(linha)
        print("Usuário excluído com sucesso!")
    else:
        print("Email não encontrado.")
    
        
    



def opcao_selecionada(opcao): 
    lista_usuarios = busca_banco()

    if opcao == 1:
        ver_cadastro(lista_usuarios)
    elif opcao == 2:
        cadastrar(lista_usuarios)
    else:
        excluir(lista_usuarios)