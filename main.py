
import sympy as sp
import matplotlib

def newton_method(fx, xi, tolerancia, iteraciones = 0):
    x = sp.Symbol('x')
    fx_exp = sp.sympify(fx)
    dx = sp.diff(fx_exp, x)
    dx_x = [xi]
    error = 1
    contador = 0
    while error > tolerancia and (iteraciones == 0 or contador < iteraciones):
        contador +=1
        xi -= fx_exp.subs(x,xi)/dx.subs(x,xi)
        dx_x.append(xi)
        print("DX: ", dx_x)
        error = sp.Abs((dx_x[-1]-dx_x[-2])/dx_x[-1])

    return dx_x[-1].evalf()


dato = newton_method('x**4-2', 1, 0.001)
print(dato)


