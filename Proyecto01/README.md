#Proyecto 01 WEB SERVICE

Proyecto 1 Modelado y Programación 
---
### Contribuidores

-  Mario Letepichia Romero  (MarioLetepichia) 
-  Celic Aislinn Liahut Ley  (Aislinn-Liahut) 
-  Ivette González Mancera   (Ivette612)

---

## Instalaciones y prerequisitos:

1. **Tener instalado python version 3 +**
Para verificarlo usa 
```bash
python3 --version
```

2. **Tener instalado requests en python**

```bash
python -m pip install requests
```
 
 Lo anterior para poder realizar los requests a las APIs 

 3. **Tener instalado dotenv.** 
	 Esto ayuda a ocultar información que no quieres mostrar al subir tu proyecto,como contraseñas,direcciones etc. 
	 Lo que nos permite dotenv hacer es mover esa información delicada en un archivo separado llamado .env

```bash
pip install python-dotenv
```

 4. **Tener una API key en Open Weather y colocarla en archivo .env**
    La API key la puedes conseguir en https://openweathermap.org/api . Lo que debes hacer es sustituir "AQUI_VA_TU_API_KEY" por tu llave
 >   **API_KEY= AQUÍ_VA_TU_API_KEY**

5. **Usar el package manager [pip](https://pip.pypa.io/en/stable/) para instalar pandas y Jupyter Notebook**

```bash
pip install pandas

pip install jupyterlab
```

5. **Usar el package manager https://docs.conda.io/en/latest/miniconda.html** 

```bash
pip install pandas
```

## Instrucciones para compilar y obtener la salida:
1.Ya que realizaste los prerequisitos anteriores, colocate en el directorio del código fuente en este caso en Proyecto01 y ejecuta lo siguiente:

```bash
python3 src/main.py
```
2.Una vez hecho lo anterior abre la carpeta del codigo fuente Proyecto01 y te aparecera un nuevo archivo llamado output.html , seleccionalo y ponle en abrir con navegador.

3.Contempla la salida 🙈🙉.


## Instrucciones para correr pruebas:

colocate en el directorio del codigo fuente y ejecuta el siguiente comando:

```bash
pytest
```

## Algunas observaciones 
también Se añadieron las siguientes dos lineas especificamente en el archivo Api_calls.py :


>  **from dotenv import load_dotenv**

Lo que hace la linea anterior es descargar la libreria env 
>  **load_dotenv()** 


Esta linea indica que se quiere que haya un archivo .env  y ahi se crean las variabes de entorno, que estan en tu computadora pero no se establece en el codigo. Las variables que guardes en el .env ahora seran variables de entorno.

Para comunicarnos con la computadora se usa la siguiente linea:
>  **import os**


