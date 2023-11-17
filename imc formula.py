#!/usr/bin/env python
# coding: utf-8

# In[6]:


def calcular_imc():
    def imc(peso, estatura):
        return peso / estatura ** 2

    peso = float(input("Ingresa tu peso en kilogramos: "))
    estatura = float(input("Ingresa tu estatura en metros: "))

    resultado_imc = imc(peso, estatura)

    print("Tu índice de masa corporal (IMC) es:", resultado_imc)


calcular_imc()
