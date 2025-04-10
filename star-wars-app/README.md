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
5. **Abrir la aplicación en el navegador**:
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

## Dependencias

El archivo `requirements.txt` incluye todas las librerías necesarias para ejecutar el proyecto. Asegúrate de instalarlas antes de ejecutar la aplicación.

### Contenido de `requirements.txt`:
````plaintext
Flask==2.3.2
requests==2.31.0