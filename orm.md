# ORM Django

**Por defecto Django viene con baterias incluidas como por ejemplo un sistema de autenticación**

[Documentation sobre los tipos de campos en los modelos de django](https://docs.djangoproject.com/en/5.0/ref/models/fields/)

## Configuración de base de datos

**En settings.py, tenemos una lista llamada DATABASES, esta lista, nos permite gestionar la base de datos que va a utilizar el proyecto.**

Por defecto Django, viene configurado con sqlite, por lo tanto al crear un proyecto nos crea por defecto en la raiz principal un archivo de sqlite llamado sqlite3.

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```


## Ejecutar las migraciones

Para ejecutar las migraciones ya creadas, utilizamos el sgt comando:

```
python3 manage.py migrate
```

## Crear una migración

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

## Base de datos

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

## Agregar nuevos campos a una migración

1. Agregamos el nuevo campo en el modelo

    ```
    class Car(models.Model):
        title = models.TextField(max_length=250)
        year = models.TextField(max_length=4, null=True)
    
    ```

    **Es necesario agregar un valor por defecto o que este sea nulleable.**
    
2. Ejecutamos el comando makemigrations, para crear el archivo de migración

    ```
    python3 manage.py makemigrations
    ```

    En este punto no crea un archivo con los cambios realizados en los modelos

    Para este caso en vez de usar **CreateModel**, usa **AddField** por que estamos agregando un campo a una tabla

    ```
    operations = [
        migrations.AddField(
            model_name='car',
            name='year',
            field=models.TextField(max_length=4, null=True),
        ),
    ]
    ```
    
3. Ejecutamos las migraciones para actualizar nuestra base de datos

    ```
    python3 manage.py migrate
    ```

    El resultado será

    ```
    Running migrations:
        Applying my_first_app.0002_car_year... OK
    ```


## Insertar datos a una tabla

Utilizamos el metodo .save(), para guardar una instancia nuevo de una modelo.

```
>>> from my_first_app.models import Car

>>> my_car = Car(title="BMW", year="2023")

>>> print(my_car)
BMW - 2023

>>> my_car.save()
```

## Actualizar datos de un registro

Utilizamos el metodo .save(), para actalizar una instancia modificada de una modelo.


```
>>> from my_first_app.models import Car

>>> my_car = Car(title="BMW", year="2023", color="dark")

>>> print(my_car)
BMW - 2023

>>> my_car.save() #Guardamos por primera vez
>>> my_car.title = "Mazda"  #Modificamos un dato

>>> print(my_car)
Mazda - 2023

>>> my_car.save() #Actualzamos en la base de datos
```


## Eliminar un registro

Utilizamos el metodo .delete(), para eliminar un registro.


```
>>> from my_first_app.models import Car

>>> car = Car(title="Aston Martin", year="2019", color="Red")

>>> car.save()

>>> car.delete()
(1, {'my_first_app.Car': 1})
```

EL delete siempre devuelve una tupla, el primero seria la cantidad y la segundo el objecto.