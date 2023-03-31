import pandas as pd
import numpy as np

archivo=pd.read_csv('Panamericanos_Lima.csv')

def metodo1():
    print(archivo['Oro'].sum())
    print(archivo.Oro.sum())
    print(np.sum(archivo['Oro']))
    print("Suma total de medallas de oro: ",np.sum(archivo.Oro))

def metodo2():
    print(len(archivo['Oro']))
    print(len(archivo.Oro))
    print(archivo['Oro'].count())
    print(archivo.Oro.count())
    print(np.size(archivo['Oro']))
    print("Total de paises participantes: ",np.size(archivo.Oro))

def metodo3():
    print(archivo.Oro.sum()/archivo.Oro.count())
    print(archivo.Oro.mean())
    print("Media de medallas de oro: ",np.mean(archivo.Oro))

def metodo4(redondeo=2):
    media=archivo.Oro.mean()
    media=round(media,redondeo)
    return media

def metodo5():
    nro_item=np.size(archivo.Oro)
    posicion=round(nro_item/2)
    print('Posición mediana: ', posicion)
    mediana=archivo.Oro[posicion-1]
    return mediana

def metodo6():
    moda=archivo.Oro.mode()
    return moda

def metodo7():

    percentil=np.percentile(archivo.Oro,50)
    print("El percentil es: ",percentil)

def metodo8():

    varianza= np.var(archivo.Oro)
    print("Este es el valor de varianza: ", varianza)

metodo1()
metodo2()
metodo3()
res=metodo4()
print("Media de medallas de oro (redondeo): ",res)

print(metodo5())

print("moda: ",metodo6())

metodo7()
metodo8()