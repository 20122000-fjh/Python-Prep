print('Hoal')

class Numero:
    def __init__(self,lista):
        self.lista = lista

    def factorial_lista(self):
        for i in self.lista:
            print('El factorial del elemento ',i,' es: ',self.factorial(i))
    
    def primo_lista(self):
        for i in self.lista:
            if self.primo == True:
                print('El elemento ',self.lista[i],' es primo')
            if self.primo == False:
                print('El elemento ',self.lista[i],' no es primo')

    def convertir_temperatura_lista(self,medida_origen,medida_destino):
        for i in self.lista:
            print(i, 'grados ',medida_origen,' son ',self.convertir_temperatura(self.lista[i],medida_origen,medida_destino),' grados ', medida_destino)


    def factorial(self,valor):
        if type(valor)!= int:
            print('El numero debe ser un numero entero')
        if valor < 0:
            print('El numero debe ser un numero positivo')
        if (valor > 1):
            valor = valor * self.factorial(valor - 1)
        return valor
    
    def primo(self,valor):
        esprimo = True
        for i in range(2,valor):
            if valor % i == 0:
                esprimo = False
                break
        return esprimo
    
    def max_repetido(self):
        lista_unicos = []
        lista_repeticiones = []
        for i in self.lista:
            if i in lista_unicos:
                r = lista_unicos.index(i)
                lista_repeticiones[r] += 1
            else:
                lista_unicos.append(i)
                lista_repeticiones.append(1)
        repetido = lista_unicos[0]
        maximo = lista_repeticiones[0]
        for i,e in enumerate(lista_unicos):
            if lista_repeticiones[i] > maximo:
                repetido = lista_unicos[i]
                maximo = lista_repeticiones[i]
        return repetido,maximo
    
    def convertir_temperatura(self,valor,medida_origen,medida_destino):
        temperatura = valor
        if medida_origen == 'celsius':
            if medida_destino == 'farenheit':
                temperatura = (valor * 9/5) + 32
            if medida_destino == 'kelvin':
                temperatura = valor + 273.15
        if medida_origen == 'kelvin':
            if medida_destino == 'celsius':
                temperatura = valor - 273.15
            if medida_destino == 'farenheit':
                temperatura = ((valor -273.15)*1.8)+32
        if medida_origen == 'farenheit':
            if medida_destino == 'celsius':
                temperatura = (valor - 32)/(9/5)
            if medida_destino == 'kelvin':
                temperatura = ((valor -32)/1.8)+273.15
        return temperatura
    
