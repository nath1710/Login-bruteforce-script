# Ataque de fuerza bruta con Python

<p align="center">
<a href="https://portswigger.net/web-security/authentication/password-based/lab-username-enumeration-via-different-responses">Laboratorio: Enumeración de nombres de usuario a través de diferentes respuestas</a>
<p align="center">
  <a href="https://www.youtube.com/watch?v=DEUCRYGt3TY">
    <img src="https://img.youtube.com/vi/DEUCRYGt3TY/hqdefault.jpg" alt="Ataque de Fuerza Bruta con Python">
  </a>
</p>
</p>

### Ejercicio realizado:
- Para desarrollar el script en Python que ejecuta un ataque de fuerza bruta, comenzamos por comprender y resolver el laboratorio de PortSwigger.

1. Instalación y ejecución de BurpSuite:

   https://portswigger.net/burp/communitydownload

2. Instalación de FoxyProxy en el navegador Firefox:

   https://addons.mozilla.org/es/firefox/addon/foxyproxy-standard/

3. Configuración de FoxyProxy y BurpSuite.

### Resolución del laboratorio
Ejecuté Burp y envié credenciales inválidas en la página de inicio de sesión. En **Proxy > HTTP history**, localicé la solicitud **POST /login**, resalté el parámetro **username** y lo envié a **Burp Intruder**.  
Configuré un ataque **Sniper** con una lista de nombres de usuario y, comparando la longitud de las respuestas del servidor, identifiqué el usuario correcto. Luego,  
marqué el parámetro **password** como carga y repetí el proceso con una lista de contraseñas, detectando la correcta de la misma manera. Finalmente,  
inicié sesión con las credenciales obtenidas y accedí a la cuenta para completar el laboratorio.

### Diseño del código
Para diseñar el script, me basé en la metodología utilizada para resolver el laboratorio. Implementé la lectura de archivos **.txt** que contenían los usuarios y contraseñas, generando la solicitud **POST**, cuyo fragmento de código está señalado en los comentarios.  
Hice que el código iterara sobre el contenido de los archivos, obteniendo la longitud de la respuesta del servidor. Primero, probé los nombres de usuario y detecté el correcto al encontrar una respuesta con una longitud diferente. Luego, repetí el proceso  
con las contraseñas. Finalmente, ejecuté el script en la terminal de **VS Code** con `python script.py` para verificar su funcionamiento.

💡 **Nota:** Esto se realizó considerando que para el ejercicio solo se dispondría de un equipo con Python instalado.

✎ **Nota:** Si deseas dejarme un comentario o sugerencia, siéntete libre de hacer un *pull request* a mi código con los cambios o comentarios sugeridos.
