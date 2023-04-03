

def converteRealemDolares(real,dolares):
        realemDolares = real/dolares
        realemDolares = round(realemDolares,2)
        return realemDolares

def converteRealemDolaresouEuroouPeso(real, moeda):
    dolares = 5.26
    euro = 5.60
    peso = 0.24

    if moeda == 1:
        dolaresemDolares = real / dolares
        dolaresemDolares = round(dolaresemDolares, 2)
        print('Seu valor em dolares é: ', dolaresemDolares)
        return dolaresemDolares


    elif moeda == 2:
        realemEuros = real/euro
        realemEuros = round(realemEuros,2)
        print('Seu valor em Euro é: ', realemEuros)
        return realemEuros

    elif moeda == 3:
        realesemPeso = real/peso
        realemPeso = round(realesemPeso,2)
        print('Seu valor em peso é: ', realesemPeso)
        return realesemPeso


def converteValor(valor, moedaOrigem,moedaConvertida ):

    if moedaOrigem == 1:
        dolares = 1
        euro = 1.09
        peso = 0.0047

        if moedaConvertida == 1:
            dolaresemDolares = valor / dolares
            dolaresemDolares = round(dolaresemDolares, 2)
            print('Seu valor em dolares é: ', dolaresemDolares)
            return dolaresemDolares


        elif moedaConvertida == 2:
            dolaresemEuros = valor/euro
            dolaresemEuros = round(dolaresemEuros,2)
            print('Seu valor em Euro é: ', dolaresemEuros)
            return dolaresemEuros

        elif moedaConvertida == 3:
            dolaresemPeso = valor/peso
            realemPeso = round(dolaresemPeso,2)
            print('Seu valor em peso é: ', dolaresemPeso)
            return dolaresemPeso

    elif moedaOrigem == 2:
        dolares2 = 0.91
        euro2 = 1
        peso2 = 0.0043

        if moedaConvertida == 1:
            eurosemDolares = valor / dolares2
            eurosemDolares = round(eurosemDolares, 2)
            print('Seu valor em dolares é: ', eurosemDolares)
            return eurosemDolares


        elif moedaConvertida == 2:
            eurosemEuros = valor / euro2
            eurosemEuros = round(eurosemEuros, 2)
            print('Seu valor em Euro é: ', eurosemEuros)
            return eurosemEuros

        elif moedaConvertida == 3:
            euroemPeso = valor / peso2
            euroemPeso = round(euroemPeso, 2)
            print('Seu valor em peso é: ', euroemPeso)
            return euroemPeso

    elif moedaOrigem == 3:
        dolares3 = 210.29
        euro3 = 229.25
        peso3 = 1

        if moedaConvertida == 1:
            eurosemDolares = valor / dolares3
            eurosemDolares = round(eurosemDolares, 2)
            print('Seu valor em dolares é: ', eurosemDolares)
            return eurosemDolares


        elif moedaConvertida == 2:
            eurosemEuros = valor / euro3
            eurosemEuros = round(eurosemEuros, 2)
            print('Seu valor em Euro é: ', eurosemEuros)
            return eurosemEuros

        elif moedaConvertida == 3:
            euroemPeso = valor / peso3
            euroemPeso = round(euroemPeso, 2)
            print('Seu valor em peso é: ', euroemPeso)
            return euroemPeso

#Crie um método que receba o peso e altura e retorne o IMC.

def imc(peso,alt):
    imc = peso/alt**2
    imc = round(imc,2)
    return imc

#Crie um método que receba as notas e retorne a maior nota do aluno

def maiorNota(nota1, nota2,):

    maior = max(nota1,nota2)
    return maior

#Crie um método que receba as notas e retorne a média de notas do aluno

def mediaNotas(nota1, nota2):
    notas = nota1 + nota2
    media = notas/2
    return media
#Crie um método que receba o valor em celsius e converta a farenheit

def convertaCelsiusemFarenheit(celsius):
    farenheit = (celsius * 1.8)+32
    farenheit = round(farenheit, 2)
    return farenheit

#Crie um método que receba o valor em farenheite converta a celsius

def convertaFarenheitemCelsius(farenheit):
    celsius = (farenheit - 32) /1.8
    celsius = round(celsius,2)
    return celsius

#Crie um método que receba o valor do salario e indique a quantidade de imposto a ser pago
#(se ganhar até 2000, 12%. Acima de 2000,25%)

def impostodeRenda(salario):
    if salario <= 2000:
        imposto = salario* 0.12
        imposto = round(imposto, 2)
        print('Seu imposto de renda é: ', imposto)
        return imposto

    elif salario > 2000:
        imposto = salario* 0.25
        imposto = round(imposto,2)
        print('Seu imposto de renda é: ', imposto)
        return imposto
