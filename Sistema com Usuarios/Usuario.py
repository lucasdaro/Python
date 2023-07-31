class Usuario: 
    def __init__(self, nome, email, data_nasci, telefone, rua, numero, bairro, cidade, estado):
        self.nome = nome
        self.email = email
        self.data_nasci = data_nasci
        self.telefone = telefone
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado

    def exibir_dados(self):
        print("Nome: {} - E-mail: {} - Data De Nascimento: {} - Telefone: {} - Rua: {} - Numero: {} - Bairro: {} - Cidade: {} - Estado: {}".format(self.nome, self.email, self.data_nasci, self.telefone, self.rua, self.numero, self.bairro, self.cidade, self.estado))

    def retorna_email(self):
        return self.email
    
    def extrair_dados(self):
        return [self.nome, self.email, self.data_nasci, self.telefone, self.rua, self.numero, self.bairro, self.cidade, self.estado]