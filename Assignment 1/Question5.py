import math as m

def evaluate_advanced_piecewise(x):
    if x > 0:
        result = m.sqrt(m.log10(x) + m.exp(x)) * m.cos(m.radians(x))
    elif x == 0:
        result = 0.0
    else:  
        result = m.log(m.fabs(x)) + m.pow(m.fabs(x), 3)
    return result
print(evaluate_advanced_piecewise(float(input("Enter a value for x: "))))