import requests

class BuscaEndereco:
    def __init__(self, cep):
        self.cep = str(cep)

        if self.cep_valido(self.cep):
            self.cep = str(cep)
        else:
            raise ValueError("CEP Invalido!")
        
    def __str__(self):
        return self.format_cep()

    def cep_valido(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def format_cep(self):
        return "{}-{}".format(self.cep[:5], self.cep[4:])
    
    def via_api(self):
        url = "https://viacep.com.br/ws/{}/json".format(self.cep)
        r = requests.get(url)
        dados = r.json()
        return (
            dados['bairro'],
            dados['localidade'],
            dados['uf']
        )