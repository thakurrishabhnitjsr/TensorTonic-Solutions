def gradient_descent_quadratic(a: float, b: float, c: float, x0: float, lr: float, steps: int) -> float:
    x=x0
    for i in range(steps):
        gradient=2*a*x+b
        x=x-lr*gradient
    return x
    pass