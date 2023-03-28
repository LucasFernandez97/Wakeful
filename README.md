# Challenge tecnico Wakeful 2023

## Requisitos

- Docker
- Postgres==latest
- Python==3.9
- Django~=3.2.18
- djangorestframework~=3.14.0
- psycopg2==2.9.5
- django-phonenumber-field==7.0.2
- django-phonenumbers==1.0.1
- djangorestframework-simplejwt==5.2.2
- django-trench==0.3.1

## Instalación

1. Clona el repositorio
2. Abre una terminal y navega hasta el directorio del proyecto
3. Buildear los contenedores: `docker-compose build`
4. Levantar la base: `docker-compose up db`
5. Levantar la WEB: `docker-compose up web`

## Uso

El objetivo es la de un ABM de usuarios asi como el login securizado del mismo.

## Endpoints

- `GET /auth/mfa/config`: Obtener la configuración actual de los MFAs configurados
- `GET /auth/mfa/user-active-methods`: Obtiene los MFAs activos actualmente
- `GET /users`: Obtener todos los usuarios de la aplicación
- `GET /users/{idUsuario}`: Obtener el usuario por ID
- `PATCH /users/{idUsuario}/`: Modificación parcial del usuario por ID
- `DELETE /users/{idUsuario}`: Borrar usuario por ID
- `POST /auth/login/`: Devuelve el JWT del usuario ingresado en el body del request
- `POST /auth/{MFA}/activate/`: Activa el Multi Factor Authentication elegido siempre y cuando este configurado
- `POST /auth/{MFA}/activate/confirm/`: Confirma la activacion con un codigo de seguridad
- `POST /auth/login/code/`: Obtiene los JWTs para el resto de aplicaciones a traves del codigo proporcionado por el metodo MFA activo
- `POST /users/`: Crea un usuario para logearse a la aplicación

## Contacto

Si tienes alguna pregunta o sugerencia, puedes contactarnos a través del siguiente correo electrónico: lucasferdani@gmail.com

