from Dado import Dado
import plotly.express as px


dado1 = Dado(6)
dado2 = Dado(6)
resultado = []
frequencia = []

for roll in range(50000):
    res = dado1.jogar() * dado2.jogar()
    resultado.append(res)

max_resultado = dado1.tipo_do_dado * dado2.tipo_do_dado
quant_valores = range(1, max_resultado + 1)

for valor in quant_valores:
    frequencia_valor = resultado.count(valor)
    frequencia.append(frequencia_valor)


titulo = "Resultado de 2 do Dado D6 Multiplicados 50.000 Vezes"
labels = {"x": "Resultado", "y": "Frequencia"}

fig = px.bar(x=quant_valores, y=frequencia, title=titulo, labels=labels)
fig.update_layout(xaxis_dtick=1)

fig.show()

print(frequencia)



# dado1 = Dado(6)
# dado2 = Dado(6)
# dado3 = Dado(6)
# resultado = []
# frequencia = []

# for roll in range(50000):
#     res = dado1.jogar() + dado2.jogar() + dado3.jogar()
#     resultado.append(res)

# max_resultado = dado1.tipo_do_dado + dado2.tipo_do_dado + dado3.tipo_do_dado
# quant_valores = range(3, max_resultado + 1)

# for valor in quant_valores:
#     frequencia_valor = resultado.count(valor)
#     frequencia.append(frequencia_valor)


# titulo = "Resultado de 3 do Dado D6 50.000 Vezes"
# labels = {"x": "Resultado", "y": "Frequencia"}

# fig = px.bar(x=quant_valores, y=frequencia, title=titulo, labels=labels)
# fig.update_layout(xaxis_dtick=1)

# fig.show()

# print(frequencia)



# dado1 = Dado(8)
# dado2 = Dado(8)
# resultado = []
# frequencia = []

# for roll in range(100000):
#     res = dado1.jogar() + dado2.jogar()
#     resultado.append(res)

# max_resultado = dado1.tipo_do_dado + dado2.tipo_do_dado
# quant_valores = range(2, max_resultado + 1)

# for valor in quant_valores:
#     frequencia_valor = resultado.count(valor)
#     frequencia.append(frequencia_valor)


# titulo = "Resultado de 2 do Dado D8 100.000 Vezes"
# labels = {"x": "Resultado", "y": "Frequencia"}

# fig = px.bar(x=quant_valores, y=frequencia, title=titulo, labels=labels)
# fig.update_layout(xaxis_dtick=1)

# fig.show()

# print(frequencia)


# dado1 = Dado()
# dado2 = Dado(10)
# resultado = []
# frequencia = []

# for roll in range(50000):
#     res = dado1.jogar() + dado2.jogar()
#     resultado.append(res)

# max_resultado = dado1.tipo_do_dado + dado2.tipo_do_dado
# quant_valores = range(2, max_resultado + 1)

# for valor in quant_valores:
#     frequencia_valor = resultado.count(valor)
#     frequencia.append(frequencia_valor)


# titulo = "Resultado de 2 do Dado D6 e D10 50.000 Vezes"
# labels = {"x": "Resultado", "y": "Frequencia"}

# fig = px.bar(x=quant_valores, y=frequencia, title=titulo, labels=labels)
# fig.update_layout(xaxis_dtick=1)

# fig.show()

# print(frequencia)








# dado1 = Dado()
# dado2 = Dado()
# resultado = []
# frequencia = []

# for roll in range(1000):
#     res = dado1.jogar() + dado2.jogar()
#     resultado.append(res)

# max_resultado = dado1.tipo_do_dado + dado2.tipo_do_dado
# quant_valores = range(2, max_resultado + 1)

# for valor in quant_valores:
#     frequencia_valor = resultado.count(valor)
#     frequencia.append(frequencia_valor)


# titulo = "Resultado de 2 do Dado D6 1.000 Vezes"
# labels = {"x": "Resultado", "y": "Frequencia"}

# fig = px.bar(x=quant_valores, y=frequencia, title=titulo, labels=labels)
# fig.update_layout(xaxis_dtick=1)

# fig.show()

# print(frequencia)





# dado = Dado()
# resultado = []
# frequencia = []

# for roll in range(1000):
#     res = dado.jogar()
#     resultado.append(res)

# quant_valores = range(1, dado.tipo_do_dado + 1)

# for valor in quant_valores:
#     frequencia_valor = resultado.count(valor)
#     frequencia.append(frequencia_valor)


# titulo = "Resultado do Dado D6 1.000 Vezes"
# labels = {"x": "Resultado", "y": "Frequencia"}

# fig = px.bar(x=quant_valores, y=frequencia, title=titulo, labels=labels)
# fig.show()

# print(frequencia)

