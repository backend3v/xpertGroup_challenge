# API de Chatbot con OpenAI

Esta es una API RESTful construida con FastAPI que utiliza el modelo de lenguaje GPT-3.5 de OpenAI para simular un chatbot configurable con roles. La API permite a los usuarios interactuar con el modelo de lenguaje y obtener respuestas basadas en el rol asignado.


## Tabla de Contenidos

- [Características](#características)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Instalación](#instalación)
- [Configuración](#configuración)
- [Uso](#uso)
- [Endpoints](#endpoints)


## Características

- Interacción con un chatbot basado en el modelo de lenguaje de OpenAI.
- Soporte para múltiples roles configurables.
- Persistencia de datos utilizando SQLite para almacenar el historial de conversaciones.
- Manejo de errores y excepciones personalizadas.


## Tecnologías Utilizadas
- [FastAPI](https://fastapi.tiangolo.com/) - Framework web para construir APIs.
- [OpenAI](https://openai.com/api/) - API de OpenAI para acceder al modelo de lenguaje.
- [Langchain](https://www.langchain.com/) - Framework de código abierto diseñado para facilitar el desarrollo de aplicaciones basadas en grandes modelos de lenguaje (LLM).
- [SQLAlchemy](https://www.sqlalchemy.org/) - ORM para la gestión de la base de datos.
- [SQLite](https://www.sqlite.org/index.html) - Base de datos ligera para almacenamiento de datos.
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Validación de datos y definición de modelos.
- [pytest](https://pytest.org/) - Framework para pruebas.



## Instalación
1. Clona el repositorio:
```
   git clone https://github.com/backend3v/xpertGroup_challenge.git
   cd xpertGroup_challenge
```


2. Crea un entorno virtual y actívalo:
```
   python -m venv venv
   source venv/bin/activate  # En Windows usa venv\Scripts\activate
```


3. Instala las dependencias:
```
   pip install -r requirements.txt
```


4. Configura las variables de entorno necesarias, incluyendo tu clave de API de OpenAI. Cambia de nombre el archivo `env` por `.env` en la raíz del proyecto y cambia el siguiente contenido:
```
OPENAI_API_KEY=tu_clave_api_aqui
```


## Configuración
Asegúrate de que tu archivo de configuración `config.py` esté correctamente configurado para cargar la clave de API de OpenAI desde las variables de entorno.
## Uso
Abrir al directorio de la aplicacion:
```
cd app
```

Para ejecutar la API, utiliza el siguiente comando:
```
python main.py
```

La API estará disponible en `http://127.0.0.1:8000`.

Para ejecutar las pruebas automatizadas de la API, utiliza el siguiente comando:
```
pytest tests.py
```



## Endpoints
### 1. Inicializar un Usuario
- **Endpoint:** `/init_user`
- **Método:** `POST`
- **Cuerpo de la Solicitud:**
```
json
  {
      "username": "nombre_de_usuario",
      "role": "rol_asignado"
  }
```


  
- **Respuesta:**
```
json
  {
      "Id": "id del usuario",
      "Name": "nombre del usuario",
      "Role":"Rol de usuario"
  }
```



### 2. Preguntar al Chatbot
- **Endpoint:** `/ask`
- **Método:** `POST`
- **Cuerpo de la Solicitud:**
```
json
  {
      "username": "nombre_de_usuario",
      "message": "tu_mensaje"
  }
```


  
- **Respuesta:**
```
json
  {
      "response": "respuesta_del_chatbot"
  }
```


### 3. Consultar Historial
- **Endpoint:** `/history/{username}`
- **Método:** `GET`
- **Respuesta:**
```
json
  [
      {
          "username": "nombre_de_usuario",
          "question": "pregunta",
          "response": "respuesta"
      }
  ]
```


### 4. Verificar Estado del Servicio
- **Endpoint:** `/health`
- **Método:** `GET`
- **Respuesta:**
```
json
  {
      "status": "Healthy"
  }
```
