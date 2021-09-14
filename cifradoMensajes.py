abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
reiniciar = True
while reiniciar:
  orden = input("\nEscriba 'cifrar' para cifrar un mensaje, o  'descifrar' para descifrarlo:\n")
  while not (orden == 'cifrar' or orden == 'descifrar'):       
    print('\nAcción inválida.')
    orden = input("\nEscriba 'cifrar' para cifrar un mensaje, o  'descifrar' para descifrarlo:\n")
  texto = input("\nEscriba su mensaje:\n").lower()
  valor = int(input("\nEscriba un número clave:\n"))
  if valor > 25:
    valor = round(valor % 25)
  while not (isinstance(valor, int)):
    print('\nError. Por favor ingrese un número.')
    valor = int(input("\nEscriba un número clave:\n"))

  def cifrar(texto, valor):

    lista_texto = list(texto)
    texto_cifrado = ""

    for letra in lista_texto:
      if letra in abecedario:
        letra = abecedario.index(letra) + valor
        if letra > 25:
          letra = letra - 25
        nueva_letra = abecedario[letra]
        texto_cifrado += nueva_letra
      else:
        texto_cifrado += letra
    
    print(f'\nEl texto cifrado es: {texto_cifrado}')


  def descifrar(texto, valor):

    lista_texto = list(texto)
    texto_descifrado = ""

    for letra in lista_texto:
      if letra in abecedario:
        letra = abecedario.index(letra) - valor
        nueva_letra = abecedario[letra]
        if letra < 0:
          nueva_letra = abecedario[letra - 1]
        texto_descifrado += nueva_letra
      else:
        texto_descifrado += letra
    print(f'\nEl texto descifrado es: {texto_descifrado}')

  if orden == 'cifrar':
    cifrar(texto,valor)
  if orden == 'descifrar':
    descifrar(texto,valor)

  nuevamente = input('\n¿Quiere utilizar el programa nuevamente? S/N\n').upper()
  if nuevamente == 'S':
    reiniciar = True
  elif nuevamente == 'N':
    reiniciar = False

