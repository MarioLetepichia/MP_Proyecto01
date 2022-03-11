import sys

###Archivo para hacer pruebas sobre python
sys.path.insert(0, '/home/marius/Documents/Modelado&Programacion/GitHub_repo/MyP_2022-2/Proyecto01/tests')

import test_cache as ca
import cache

print(ca.Example.cache1)
print(len(ca.Example.cache1))

c = cache.Cache()
c.addValue("APT",{'Hola': 2, 'Adios':3})

print(c.getValue('APT'))
