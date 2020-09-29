def suma(a,b):
  return a+b
	
def resta(a,b):
	return a-b

def producto(a,b):
  return a*b

def division(a,b):
  if (b==0):
    print("Selecciona de nuevo un numero diferente de 0")
    return 'n'
  return a/b

def Triangulo(numero):
  ciclo=1
  n='+'
  while (ciclo<=numero):
    print(n)
    n+='+'
    ciclo+=1