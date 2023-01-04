def calcule(num1, operator, num2):
    if operator =="+":
      return num1 + num2
    elif operator =="-":
      return num1 - num2
    elif operator == "*":
     return num1 * num2
    elif operator =="/":
     return num1 / num2
    elif operator =="%":
     return num1 % num2
    else :
        return "Opération non valide"

print(calcule(11, "+", 8))
print(calcule(10, "-", 8))
print(calcule(10, "*", 8))
print(calcule(10, "/", 8))
print(calcule(10, "%", 8))





