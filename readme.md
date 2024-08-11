# Django

## Requerimientos

1. Python
2. Programación orientada a objectos


## Entornos virtuales (VENV)

los entornos virtuales nos permiten tener un paquete en diferentes versiones en nuestro computador.

1. En Linux es requerido instalar el paquete de venv, para esto usamos el siguiente comando 

    ```
    sudo apt install python3-venv
    ```


2. Para crear un entorno virtual, usamos el siguiente comando

    ```
    python3 -m venv /home/.envs/my-first-env
    ```

    con esto indicamos que se va a crear en una carpeta home, una carpeta ocultar con el entorno virtual my-first-env. En esta carpeta estara todo el entorno necesario para que nuestra aplicación funciones correctamente

3. Para activar un comando virtual, necesitamos el comando

    ```
    source /home/.envs/my-first-env/bin/activate
    ```

    Debemos ir dentro del paquete instalado del entorno a la carpeta bin y luego al archivo activate, con este deberiamos ver en la consola que se antepone el nombre del paquete antes del directorio sobre el cual estamos.


## Instalación de Django

1. Debemos activar nuestro entorno virual
2. Instalamos PIP con el sgt comando
 
    ```
    pip install Django
    ```

## Crear un nuevo proyecto

Para crear el proyecto escribimos el siguiente comando:

```
django-admin startproject my_frist_project
```

Es importante tener en cuenta que no podemos usar guiones. Dado que python lo interpreta como una resta.

Esto nos va a crear una carpeta dentro del directorio sobre el que estamos parados.

En esta vamos a ver un archivo llamada manage.py, el cual nos va a ayudar a ejecutar comandos que solo se aplicaran a nuestro proyecto.


## Archivo manage.py

manage.py, es el archivo el cual nos va a ayudar a ejecutar comandos que solo se aplicaran a nuestro proyecto.

### Iniciar un servidor

Para iniciar un servidor ejecutamos el comando 

```
python3 my_frist_project/manage.py runserver
```

Con esto veremos información en consola. Tanto como errores, warnings y que se inicio el servidor en un puerto especifico por ejm: 

```
Starting development server at http://127.0.0.1:8000/
```

### Para crear una app

Con el siguiente comando vamos a crear una app, la cual contrandrá los archivos inicales del proyecto.

**(En este caso queremos estar dentro de la carpeta donde se encuentra manage.py, para que nos cree el proyecto dentro de este directorio)**

```
python3 manage.py startapp my_first_app
```

Este comando nos crea archivos de:

- model.py
- views.py

### Crear una migración

Para crear una migración utilizamos el comando:

```
python3 manage.py makemigrations
```

El resultado de esto seria:

```
my_first_app/migrations/0001_initial.py
 - Create model Car
```


Este comando nos va a crear un archivo dentro de la carpeta migrations con los modelos creados dentro del archivo models.py

**Al crear un modelo, a este le dicimos el tipo de dato y la longitud, por lo tanto esos seran los campos que serán creados en la tabla.**


```
class Car(models.Model):
    title = models.TextField(max_length=250)
```


Por defecto Django te crea el campo ID, pero si se quisiera modificar el tipo de dato, lo que hacemos al crear la clase, le decimos el tipo de dato que seria el ID.

Debemos tener en cuenta que al crear la migración el nombre de nuestra tabla será el nombre de  la aplicación + el nombre del modelo en minuscula, como resultado la tabla se va a llamar **my_first_app_car**


### Ejecutar las migraciones

Para ejecutar las migraciones ya creadas, utilizamos el sgt comando:

```
python3 manage.py migrate
```



### Para usar una base de datos

Con este comando nos conectamos a la base de datos:

```
./manage.py dbshell
```


Para ver las tablas usamos el comando:

```
.tables
```

Para ver una tabla, usamos .schema y nombre de la tabla:

```
schema my_first_app_car
```


### Para usar la terminal de Python

Con este comando utilizamos la terminal de Django.

```
python3 manage.py shell
```

Podemos interactuar con los modelos, funciones etc..

```
>>> from my_first_app.models import Car
>>> my_car = Car(title="BMW", year="2023")
>>> print(my_car)
BMW - 2023
>>> 
```



## MVT

- M : Model
- V : View
- T : Template


1. El modelo es donde guardamos los datos, la logica del negicio
2. La vista es un conector tiene acceso a los datos y define a donde van a llegar
3. El template es la parte grafica


La forma de uso es que la vista funciona como un controlador, enviando la informacion del modelo a la template y recibiendo informacion de la template para enviar al modelo y retornar informacion a la template.


# Ejecutando nuestra primera vista


1. Creamos nuestra primera app

    Creamos la aplicacion con el comando

    ```
    python3 manage.py startapp my_first_app
    ```
   
1. Vamos al archivo model y creamos una nueva clase, que hereda de la clase models.Model

    ```
    class Car(models.Model):
        title = models.TextField(max_length=250)
    ```

    En este caso dentro de la clase, decimos que tenemos un TextField con una longitud maxima de 250 caracteres

2. Creamos en la raiz de la app creada una carpeta llamada template, dentro la cual creamos otra carpeta con el mismo nombre a la app y dentro de esta creamos un archivo html, en este caso con el nombre de car_list.html
   
3. Una vez creada la template (Archivo html), debemos definir en my_view.py donde se encuentra ese archivo:
   
    Para esto creamos una función donde que recibe un parametro llamado request, y usamos render para renderizar el contenido, dentro de render, necesitamos dos parametros, el request y la ruta del archivo que vamos a mostrar.

    ```
    def my_view(request):
        return render(request, "my_firts_app/car_list.html")
    ```

    Django en ese caso interpreta que se encuentra dentro de template, por lo tanto no es necesario usar template/my_first_app/car_list.html. Solo vamos a usar la carpeta donde se encuentra la vista y el nombre de la vista (my_first_app/car_list.html) 

4. Debemos registrar en el archivo de configuración nuestra aplicación creada, por lo tanto, vamos a settings.py y en la lista INSTALLED_APP, vamos agregar el nombre de nuestra aplicacion (my_first_app)

    ```
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'my_first_app'
    ]

    ```

5. Por ultimo vamos al archivo urls.py y en la lista urlpatterns, vamos a registrar la URL de la vista que buscamos redenrizar.

    - Para esto primero, debemos importar la función creada en views, en este caso llamada my_view
    - En urlpatterns, tenemos una funcion llamada path, la cual recibe dos parametros, la primera es la ruta que escribimos en el navegador y la segunda es la funcion que importamos anteriormente

    ```
    from my_first_app.views import my_view

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('car-list', my_view)
    ]

    ```

**Con estos pasos ya podemos ejecutar el servidor y agregar a la ulr nuestra ruta para ver el contenido del archivo html**

- Ejecutamos el servidor con el comando: python3 manage.py runserver

```
http://127.0.0.1:8000/car-list
```

# Enviar parametros a una template

1. Para esto usamos un contexto (context), que es uno de los parametros de render


    ```
    def my_view(request):
        car_list = [
            {"title": "BMW"},
            {"title": "Manza"},
        ]
        
        context = {
            "car_list" : car_list
        }
        return render(request, "my_firts_app/car_list.html", context)

    ```

2. Para iterar sobre el contenido recibido en html:

    ```
    <body>
        <h1>Lista de carros</h1>
        <ul>
        {% for car in car_list %}
            <li>{{ car.title }}</li>
        {% endfor %}
        </ul>
    </body>

    ```

    Podemos envidencia que para usar un for, debemos iniciar con {% y cerrar con %}

    Y el contenido de un dato lo debemos encerar dentro de doble corchete, esto lo imprime para visualizarlo en la vista actuomaticamente {{ }}



# Crear un archivo de URLS

1. En el raiz de nuestra aplicación, creamos un archivo llamado urls.py y dentro de el importamos HttpResponse y path, creamos una lista ulrpatterns y en este declaramos nuestra rutas.

    ```
    from django.http import HttpResponse
    from django.urls import path


    def my_view(request, *args, **kwargs):
        print(args)
        print(kwargs)
        return HttpResponse("")


    urlpatterns = [
        path("listado", my_view),
        path("detalle/<int:id>", my_view)
    ]
    ```


2. Ahora vamos a agregar nuestro nuevo archivo de rutas, para esto vamos al archivo urls.py del proyecto pricipal:
   
   1. Importamos de django.urls el metodo llamado include

        ```
        from django.urls import path, include
        ```

   2. En urlpatterns, dentro del metodo path, agregamos como primer parametro nuestra ruta del modúlo en este caso "carros", como segundo parametro, vamos a incluir el archivo nuevo de rutas, que seria el nombre de la aplicación y el archivo que contiene las nuevas URLS. (**aplicacion.archivo_urls**)

        ```
        urlpatterns = [
            path('admin/', admin.site.urls),
            path('carros/', include('my_first_app.urls'))
        ]
        ```


3. Con esto ya deberiamos poder ingresar a las rutas declaradas en el punto 1 por ejm:

    - url_server/carros/listado
    - url_server/carros/detalle/1



# Vistas basadas en clases

1. En la aplicacion vamos al archivo llamado views.py, dentro de esta vamos a importar TemplateView
2. Creamos una clase y heredamos de TemplateView
3. Esta clase requiere de dos pasos para poder renderizar las vistas
    
   1. La vista a la cual vamos a redirigir, para esto declaramos una variable llamada template_name
   
   2. el contexto que se va a enviar a la vista, para esto creamos una funcion get_context_data y retornamos el valor deseado.
   
4. Para este punto el archivo views.py se deberia ver de esta manera

    ```
    from django.shortcuts import render
    from django.http import HttpResponse
    from django.views.generic.base import TemplateView

    # Create your views here.
    from django.shortcuts import render
    from django.http import HttpResponse
    from django.views.generic.base import TemplateView

    class CarListView(TemplateView):
        template_name = "my_firts_app/car_list.html"

        def get_context_data(self):
            car_list = [
                {"title": "BMW"},
                {"title": "Manza"},
            ]

            return {
                "car_list": car_list
            }

    ```

5. Finalmente debemos decirle a nuestra ruta que va a usar una vista basada en clases

   - Importamos desde .views la clase CarListView
   - en nuestra ruta, debemos agregar como segundo parametro la clase, pero esta debe tener .as_view() para que django interprete que va hacer una respuesta http

    ```
    from .views import my_test_view, my_view, CarListView

    urlpatterns = [
        path("listado", CarListView.as_view()),
    ]

    ```

# Django Templates

1. **Mostrar una variable** en una vista html

    Para esto debemos poner nuestra variable en doble llaves {{ variable }}

2. **Filtros** nos permite modificar el valor de una variable

    **Para usar usar filtros debemos usar un pipelie (|)** 

    Por ejemplo en este caso queremos modificar una fecha y solo mostrar el mes y día

    **{{ "2023-12-05" | date: "M/d" }}**

    Los filtros tambien se pueden concatener, en este caso le vamos a decir que nos muestre el resultado en minuscula.

    {{ "2023-12-05" | date: "M/d" | lower }}

3. **Tags** Los tags permiten agregar una funcionalidad en el codigo html por ejm recorrer una lista, mostrar una url dinamica, condiccionales... etc

    El sintaxis es **{% %}**, dentro de estos podemos usar if, for, url


