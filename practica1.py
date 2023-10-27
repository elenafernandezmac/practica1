"""
calculo del teorema de la probabilidad total y el teorema de bayes
"""
# recibimos las probabilidades a priori
a_priori1 = float(input("introduzca la probabilidad a priori del primer suceso: "))
a_priori2 = float(input("introduzca la probabilidad a priori del segundo suceso: "))

# recibimos la verosimilitud necesitada
verosimilitud1 = float(input("introduzca la probabilidad condicional del primer suceso: "))
verosimilitud2 = float(input("introduzca la probabilidad condicional del segundo suceso: "))

"""
aplicamos la formula del teorema de la probabilidad total
P(verosimilitud) = P(1)*P(probabilidad condicional de 1)+P(2)*P(probabilidad condicional de 2)
"""
tpt = (a_priori1 * verosimilitud1) + (a_priori2 * verosimilitud2)

# pasamos el valor a porcentaje
tpt_porcentaje = tpt * 100

# imprimimos el resultado
print(f"la probabilidad total del suceso condicional es del {tpt} %")

# recibimos los valores a los que se quiere calcular bayes
a_priori = (float(input("Introduzca la probabilidad a priori a la que quiera calcular Bayes: ")))
verosimilitud = (float(input("Introduzca el suceso condicional de dicha probabilidad: ")))

"""
siguiendo el teorema de bayes: P(A)*P(probabilidad condicional de A)/tpt
sustituimos los valores de la ecuación en la fórmula
"""

bayes = (a_priori*verosimilitud)/tpt

#devolvemos el resultado
print(f"El resultado del teorema de Bayes es {bayes}")