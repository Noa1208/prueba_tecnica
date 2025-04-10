# Aplicación de Star Wars

Este proyecto es una aplicación web construida con Flask que permite listar personajes del universo de Star Wars utilizando la [API de Star Wars (SWAPI)](https://swapi.dev/). Los usuarios pueden hacer clic en un personaje para ver información detallada sobre él, incluyendo sus características físicas y las películas en las que aparece.

## Estructura del Proyecto

```
star-wars-app
├── src
│   ├── main.py                # Punto de entrada de la aplicación
│   ├── services
│   │   └── swapi_service.py   # Funciones para interactuar con la API de SWAPI
│   ├── templates
│   │   ├── main_screen.html   # Plantilla para la pantalla principal
│   │   └── detail_screen.html # Plantilla para la pantalla de detalles
│   └── utils
│       └── prueba_request.py  # Funciones auxiliares para realizar solicitudes HTTP
├── requirements.txt           # Dependencias del proyecto
└── README.md                  # Documentación del proyecto
```

## Instrucciones de Configuración

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/Noa1208/prueba_tecnica.git
   cd star-wars-app
   ```

2. **Instalar las dependencias necesarias**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar la aplicación**:
   ```bash
   python src/main.py
   ```
4. **Ejecutar la inserción de los datos**
   ```bash
   python src/populate_database.py
   ```
5. **Instalacion de MongoDB shell**
   instalar MongoDB shell por medio del siguiente enlace: https://www.mongodb.com/try/download/shell
    
6. **Abrir la aplicación en el navegador**:
   Accede a la aplicación en tu navegador en la dirección:  
   [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Uso del Aplicativo Web


1. **Pantalla Principal**:
   - Al abrir la aplicación, se mostrará una lista de personajes del universo de Star Wars.
   - Cada personaje estará listado con su nombre. Puedes hacer clic en el nombre de un personaje para ver más detalles.

2. **Pantalla de Detalles**:
   - Al seleccionar un personaje, serás redirigido a una página que muestra información detallada sobre él, incluyendo:
     - Nombre
     - Altura
     - Peso
     - Color de cabello
     - Color de piel
     - Películas en las que aparece (con sus títulos).

3. **Interacción con la API**:
   - La aplicación utiliza la API de SWAPI para obtener información en tiempo real sobre los personajes y las películas.

4. **Visualizar los registros de la base de datos**
   - Luego de realizar la instalacion de mongoDB shell ejecutar:
   ```bash
    use star_wars_db
   ```
   ```bash
   show collections
   ```
   ```bash
   db.characters.find().pretty()
   ```


## Dependencias

El archivo `requirements.txt` incluye todas las librerías necesarias para ejecutar el proyecto. Asegúrate de instalarlas antes de ejecutar la aplicación.

### Contenido de `requirements.txt`:
````plaintext
blinker==1.9.0
certifi==2025.1.31
charset-normalizer==3.4.1
click==8.1.8
colorama==0.4.6
dnspython==2.7.0
Flask==3.1.0
idna==3.10
itsdangerous==2.2.0
Jinja2==3.1.6
MarkupSafe==3.0.2
pymongo==4.12.0
requests==2.32.3
urllib3==2.3.0
Werkzeug==3.1.3