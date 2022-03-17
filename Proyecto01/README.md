
Proyecto 1 Modelado y Programación 
---
### Contribuidores

-  Mario Letepichia Romero  (MarioLetepichia) 
-  Celic Aislinn Liahut Ley  (Aislinn-Liahut) 
-  Ivette González Mancera   (Ivette612)

---

## Instalaciones y prerequisitos:

1. **Instalar python (version 3+)**
Para verificarlo usa 
```bash
python3 --version
```

2. **Instalar requests en python**

```bash
python -m pip install requests
```
 
 Lo anterior para poder realizar los requests a las APIs 

 3. **Instalar python-dotenv.** 
	 Esto ayuda a ocultar información que no quieres mostrar al subir tu proyecto,como contraseñas,direcciones etc. 
	 Lo que nos permite dotenv hacer es mover esa información delicada en un archivo separado llamado .env

```bash
pip install python-dotenv
```

 4. **Obtener una API key en Open Weather y colocarla dentro del archivo _.env_**
    La API key la puedes conseguir en https://openweathermap.org/api . Lo que debes hacer es sustituir "AQUI_VA_TU_API_KEY" por tu llave
 >   **API_KEY= AQUÍ_VA_TU_API_KEY**

5. **Usar el package manager [pip](https://pip.pypa.io/en/stable/) para instalar pandas y Jupyter Notebook**

```bash
pip install pandas

pip install jupyterlab
```

6. **Usar el package manager https://docs.conda.io/en/latest/miniconda.html** 

```bash
pip install pandas
```

## Instrucciones para compilar y obtener la salida:
1. Ya que realizaste los prerequisitos anteriores colocate en el directorio _Proyecto01_:
```bash
cd Proyecto01
```

2. Ejecuta el siguiente comando para correr el programa

```bash
python3 src/main.py
```
3. Una vez hecho, el programa se procesara los 3000 tickets y generara un documento _output.html_ dentro del directorio docs

4. Este documento se abrira automaticamente en tu navegador predeterminado 🙈🙉.


## Instrucciones para correr pruebas:

Colocate en el directorio del codigo fuente _Proyecto01_ y ejecuta el siguiente comando:

```bash
pytest
```

## Observaciones extras
- Se añadieron las siguientes dos lineas especificamente en el archivo API_calls.py :

>  **from dotenv import load_dotenv**

- - Lo que hace la linea anterior es descargar la libreria env 
>  **load_dotenv()** 


- - Esta linea indica que se quiere que haya un archivo .env  y ahi se crean las variabes de entorno, que estan en tu computadora pero no se establece en el codigo. Las variables que guardes en el .env ahora seran variables de entorno.

- Para comunicarnos con la computadora se usa la siguiente linea:
>  **import os**

- Se utiliza la paqueteria _sys_ para acceder a modulos dentro de distintos directorios
>  **import sys**
