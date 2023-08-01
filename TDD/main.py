from bytebank import Funcionario


nome, data, salario = 'teste', '12/03/2000', 1000
esperado = 'Funcionario(Teste, 12/03/2000, 1000)'

funcionario_teste = Funcionario(nome, data, salario)

print(funcionario_teste.__str__())