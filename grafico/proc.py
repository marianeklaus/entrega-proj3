import numpy as np
import matplotlib.pyplot as plt

def design(tipo_funcao, coeficientes):
    """
    Determina e desenha o gráfico da função escolhida.

    Parâmetros:
    - tipo_funcao: string representando o tipo da função.
    - coeficientes: lista de coeficientes.

    Retorna uma lista de pontos (x, y) representando a função.
    """
    pontos = []

    if tipo_funcao == "1":
        # Função Afim: y = ax + b
        a, b = coeficientes
        x = np.linspace(-10, 10, 100)
        y = a * x + b
        pontos = list(zip(x, y))
    elif tipo_funcao == "2":
        # Função Quadrática: y = ax^2 + bx + c
        a, b, c = coeficientes
        x = np.linspace(-10, 10, 100)
        y = a * x**2 + b * x + c
        pontos = list(zip(x, y))
    elif tipo_funcao == "3":
        # Função Logarítmica: y = ln(x)
        x = np.linspace(0.1, 10, 100)  # Considerando x > 0 para logaritmo
        y = np.log(x)
        pontos = list(zip(x, y))
    elif tipo_funcao == "4":
        # Função Exponencial: y = e^x
        x = np.linspace(-10, 10, 100)
        y = np.exp(x)
        pontos = list(zip(x, y))

    return pontos