import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

def newton_method(fx, xi, tolerancia, iteraciones=0):
    x = sp.Symbol('x')
    fx_exp = sp.sympify(fx)
    dx = sp.diff(fx_exp, x)
    dx_x = [xi]
    error = 1
    contador = 0

    print("| Iteración | Valor de xi |")
    print("|-----------|-------------|")
    print(f"| {contador}         | {xi}        |")

    while error > tolerancia and (iteraciones == 0 or contador < iteraciones):
        contador += 1
        xi -= fx_exp.subs(x, xi) / dx.subs(x, xi)
        dx_x.append(xi)
        error = sp.Abs((dx_x[-1] - dx_x[-2]) / dx_x[-1])
        print(f"| {contador}         | {xi} |")

    # Gráfico de la función
    x_vals = np.linspace(float(xi) - 2, float(xi) + 2, 100)
    y_vals = [fx_exp.subs(x, val) for val in x_vals]

    plt.plot(x_vals, y_vals, label='Función')
    plt.scatter(dx_x, [fx_exp.subs(x, val) for val in dx_x], color='red', label='Iteraciones')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Método de Newton')
    plt.legend()
    plt.grid(True)
    plt.show()

    return dx_x[-1].evalf()

dato = newton_method('x**4-2', 1, 0.001)
print(dato)
