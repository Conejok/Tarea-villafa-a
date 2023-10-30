#!/usr/bin/env python
# coding: utf-8

# In[ ]:


inicio_r = int(input("Ingresa el inicio del rango"))
final_r = int(input("ingresa el final del rango"))

inicio_t = int(input("Ingresa el inicio de la tabla"))
final_t = int(input("ingresa el final de la tabla"))

for i in range(inicio_r,final_r + 1):
    print (f"La tabla del {i}")
    for j in range(inicio_r,final_r+1):
        print(f"{i}x {j} = {i*j}")
        

