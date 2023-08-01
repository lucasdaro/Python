from bytebank import Funcionario
import pytest

class TestClass:

    def test_quando_idade_recebe_13_03_2000_deve_retornar_23(self):
        entrada = "13/03/2000"
        esperado = 23

        funcionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = funcionario_teste.idade()

        assert resultado == esperado

    def test_quando_sobrenome_recebe_Lucas_Camargo_deve_retornar_Camargo(self):
        entrada = ' Lucas Camargo '
        esperado = 'Camargo'

        usuario = Funcionario(entrada, '22/11/1995', 5000)
        resultado = usuario.sobrenome()

        assert resultado == esperado

    def test_quando_decrescimo_salario_100000_deve_retornar_90000(self):
        entrada_salario = 100000
        entrada_nome = 'Paulo Bragança'
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, "22/11/1995", entrada_salario)
        funcionario_teste.descrescimo_salario()
        resultado = funcionario_teste.salario
        assert resultado == esperado

    @pytest.mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000
        esperado = 100

        funcionario = Funcionario('Teste', '11/11/1997', entrada)
        resultado = funcionario.calcular_bonus()

        assert resultado == esperado

    @pytest.mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_100000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 100000
            
            funcionario = Funcionario('Teste', '11/11/1997', entrada)
            resultado = funcionario.calcular_bonus()

            assert resultado

    def test_print_classe(self):
        nome, data, salario = 'teste', '12/03/2000', 1000
        esperado = 'Funcionario(Teste, 12/03/2000, 1000)'

        funcionario_teste = Funcionario(nome, data, salario)
        resultado = funcionario_teste.__str__()

        assert resultado == esperado



