## 	Sobre las instalaciones y prerequisitos  para que la llamada de la API funcione:


1. **Tener instalado requests en python**
>   **python -m pip install requests**
 
 Lo anterior para poder realizar los requests a las APIs 

 2. **Tener instalado dotenv.** 
	 Esto ayuda a ocultar información que no quieres mostrar al subir tu proyecto,como contraseñas,direcciones etc. 
	 Lo que nos permite dotenv hacer es mover esa información delicada en un archivo separado llamado .env

>   **pip install python-dotenv**

 3. **Tener una API key en Open Weather y colocarla en archivo .env**
    La API key la puedes conseguir en https://openweathermap.org/api . Lo que debes hacer es sustituir "AQUI_VA_TU_API_KEY" por tu llave
 >   **API_KEY= AQUÍ_VA_TU_API_KEY**

## Algunas observaciones 
también Se añadieron las siguientes dos lineas especificamente en el archivo Api_calls.py :


>  **from dotenv import load_dotenv**

Lo que hace la linea anterior es descargar la libreria env 
>  **load_dotenv()** 


Esta linea indica que se quiere que haya un archivo .env  y ahi se crean las variabes de entorno, que estan en tu computadora pero no se establece en el codigo. Las variables que guardes en el .env ahora seran variables de entorno.

Para comunicarnos con la computadora se usa la siguiente linea:
>  **import os**

**Nota:** Para ocultar el archivo .env que contiene información delicada, se crea un archivo llamado gitignore donde se colocan los archivos a ignorar y cuando se sube a github tales archivos no se suben. 

Fuente:  https://www.youtube.com/watch?v=YdgIWTYQ69A

Para documentarte de las APIs : https://www.dataquest.io/blog/python-api-tutorial/

