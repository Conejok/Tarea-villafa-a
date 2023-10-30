#!/usr/bin/env python
# coding: utf-8

# In[6]:


def imc(peso, estatura):
    return peso / estatura**2
imc = imc(peso, estatura)
peso = float(input("Ingresa tu peso: "))
estatura = float(input("Ingresa tu estatura "))
print("Tu índice de masa corporal (IMC) es:", imc)

