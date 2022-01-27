""" Programa calculadora artimética super amigable#
    Realiza las 4 operaciones (+,-,* /)
    dada una entrada una cadena de caracteres 
    Ejemplo:
    45+45
    30-15
    12*8
    Solo dos muneros y una operacion
    """

#---------------- Zona librerias------------
import calculadora_aritmetica as calc

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

#----------Definición de Funciones (Dividir)------------
def preguntar():
  cadena = input("ingrese la operacion (sin espacios) \n")
  return cadena

def parser_cadena(cadena_entrada):
  numero_uno=""
  numero_dos=""
  operando=""
  #TODO: codigo que obtiene los numeros y el operando
  if (cadena_entrada.find("+") != -1):
    ope = cadena_entrada.find("+")
    operando ="sumar_numeros"
  elif (cadena_entrada.find("-") != -1):
    ope = cadena_entrada.find("-")
    operando = "restar_numeros"
  elif (cadena_entrada.find("*") != -1):
    ope = cadena_entrada.find("*")
    operando = "multiplicar_numeros"
  elif (cadena_entrada.find("/") != -1):
    ope = cadena_entrada.find("/")
    operando = "dividir_numeros"

  numero_uno = int(cadena_entrada[0:ope])
  numero_dos = int(cadena_entrada[ope+1:])

  return numero_uno, numero_dos, operando
  #return numero_uno, numero_dos, calc.{operando}(numero_uno,numero_dos)

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================
#TODO: Leer cadena de entrada
#num_1,num_2,op= parser_cadena(cadena_entrada)
#TODO: terminar programa
print("Bienvenido a calculadora realizaremos todas tus operaciones")
print("*******Podra operar continuamente*******")

while(True):

  cadena_entrada = preguntar()

  (n1, n2, fun)= parser_cadena(cadena_entrada)
  #r = calc.+fun
  if fun=="sumar_numeros":
    print(f"El resultado de {cadena_entrada} es", calc.sumar_numeros(n1, n2))
  elif fun=="restar_numeros":
    print(f"El resultado de {cadena_entrada} es", calc.restar_numeros(n1, n2))
  elif fun=="multiplicar_numeros":
    print(f"El resultado de {cadena_entrada} es", calc.multiplicar_numeros(n1, n2))
  elif fun=="dividir_numeros":
    if n2!=0:
      print(f"El resultado de {cadena_entrada} es", calc.dividir_numeros(n1, n2))
    else:
      print("No es posible dividor por cero")
