def separador_de_palabras(string):
    dic = {}

    lista_separada = string.split()

    for i in lista_separada:
        dic[i] = i[0]
    
    return dic


def funcion(tupla):
    for i in diccionario:
        tupla = (i, diccionario[i])
    return tupla

frase = "Universidad del Desarrollo Innovacion y Creatividad"
diccionario = separador_de_palabras(frase)



print(funcion(diccionario))