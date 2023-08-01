import requests
from AcessoCep import BuscaEndereco

# cnpj = "70526512000171"
# cpf = "43210055822"

# documento = Documento.cria_documento(cnpj)
# print(documento)

# documento = Documento.cria_documento(cpf)
# print(documento)

# telefone = "554126481234"
# telefone_objeto = TelefonesBr(telefone)
# print(telefone_objeto)

# cadastro = DatasBr()
# print(cadastro)

cep = 18654632
novo_cep = BuscaEndereco(cep)
bairro, cidade, uf = novo_cep.via_api()
print(bairro, cidade, uf)