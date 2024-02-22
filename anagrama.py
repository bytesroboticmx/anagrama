#from obtener_definicion import obtener_definicion
def generar_anagramas(palabra, longitud):
  """
  Genera todos los anagramas posibles de una palabra.

  Args:
    palabra: La palabra a partir de la cual se generan los anagramas.
    longitud: La longitud máxima de los anagramas.

  Returns:
    Una lista con todos los anagramas posibles.
  """
  anagramas = []
  for i in range(len(palabra)):
    for j in range(i + 1, len(palabra)):
      if palabra[i] != palabra[j]:
        anagrama = palabra[i] + palabra[j]
        if len(anagrama) <= longitud:
          anagramas.append(anagrama)
  return anagramas

def main():
    """
    Función principal del programa.
    """
    palabra = input("Introduzca una palabra: ")
    longitud = int(input("Introduzca la longitud máxima de los anagramas: "))

    anagramas = generar_anagramas(palabra, longitud)

    for anagrama in anagramas:
        #print(anagrama, "-", obtener_definicion(anagrama))
        print(anagrama)

"""def obtener_definicion(palabra):
    """
   # Obtiene la definición de una palabra.

  #  Args:
    #    palabra: La palabra de la cual se desea obtener la definición.

   # Returns:
       # La definición de la palabra.
    #"""
    # Implement your logic here to obtain the definition of the word
    #return "Definicion de la" + palabra"""
#""
if __name__ == "__main__":
    main()
