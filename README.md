# Ejemplo Docker-Compose con Microservicios  
## Instalación de Docker-Compose  
1. Descargar el instalador desde la página oficial (https://docs.docker.com/get-started/get-docker/)  
2. Ejecutar y reiniciar una vez terminada la instalación.  
## Ejecutar el proyecto  
1. Desde la terminal de comandos, nos dirigimos al directorio raíz del proyecto (/Dockerizacion)  
2. Ejecutamos el comando docker-compose up -d  
3. Podemos revisar los contenedores activos mediante 'docker-compose ps'  
El proyecto utiliza el puerto 5000 para ejecutarse, en caso de estar ocupado, este puede ser editado en el archivo docker-compose.yaml    
## Estructura del proyecto
La carpeta **backend-data** contiene un código sencillo para devolver un mensaje.
La carpeta **frontend-api** contiene el código de una aplicación sencilla donde al ingresar se verifica que haya contenido en  
el cache Redis, en caso de no obtener el dato se llama al servicio backend-data, donde se obtiene el mensaje antes mencionado.  
Si se recarga la página, se mostrará el mismo mensaje, pero en este caso la fuente será cache de Redis, debido a que se guardó  
el mensaje en la primer ejecución.  
El archivo **Dockerfile** define reglas para ser ejecutadas para el microservicio  
El archivo **requirements** define los paquetes necesarios para la ejecución.  
El archivo **docker-compose.yaml** define los servicios e indica desde donde se construyen, también define que el servicio *frontend-api* depende de los servicios: '*backend-data*' y '*db-cache*'
El servicio backend-data usa el puerto **5001** y frontend-api el **5000**. 
