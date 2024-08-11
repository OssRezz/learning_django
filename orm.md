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

## Relaciones entre tablas

### Uno a muchos

Para relacionar una tabla usamos la sgt sintaxis en el modelo que se quiere relacionar

```
class Book(models.Model):
    name = models.TextField(max_length=255)
    date = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.DO_NOTHING)
```
**ForeignKey**, recibe dos parametros, uno es la clase con la que se relaciona y el segundo es que se va hacer cuando ese registro no existe (on_delete)

- DO_NOTHING: Significa que si se elimina el publisher no pasa nada
- PROTECT: No te permite borrar, por que a existe un registro con el publisher
- CASCADE: Elimina en cascada todos los registros que tenga el recurso a eliminar

### Muchos a muchos

```
class Author(models.Model):
    name = models.TextField(max_length=255)
    birth_date = models.DateField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.TextField(max_length=255)
    date = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author, related_name="authors")

    def __str__(self):
        return self.title
```

**ManyToManyField** recibe dos parametros, uno es el modelo con el cual va a interactuar y el segundo es el nombre con el cual se va a relacionar cuando queramos acceder desde el modelo que se relaciona.

Al ejecutar la migracion el sistema nos crea una tabla automaticamente llamada **book_authors**

```
>>> from my_first_app.models import Author, Book, Publisher

>>> james = Author(name="James", birth_date="1996-06-15")

>>> caro = Author(name="Carolina", birth_date="1992-08-01")

>>> james.save()

>>> caro.save()

>>> book = Book.objects.first()

>>> book.authors

<django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object at 0x7fdb9c771670>

>>> book.authors.set([james,caro])
```

Como podemos ver en el ejemplo anterior para relacionar un libro con un authors y poblar la relacion de muchos a muchos, usamos set, para esto es importante que la informacion llegue en una lista.

### Uno a uno

La sintaxis para crear una relacion de uno a uno es la sgt:


```
class Profile(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    website = models.URLField()
    biography = models.TextField(max_length=500)
```

**OneToOneField** requiere de dos parametros, el cual es el modelo con el que se va a relacionar y el segundo es que va a suceder con ese registro si se elimina

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

## Managers

Los managers son una parte fundamental del sistema de consultas.

**Definición**: Un manager es la interfaz a través de la cual Django proporciona operaciones de consulta a la base de datos para un modelo.

**Función principal**: Actúa como un intermediario entre el modelo y la base de datos, proporcionando métodos para realizar consultas.

**Manager por defecto:** Cada modelo de Django tiene al menos un manager, llamado objects por defecto.

```
todos_los_libros = Book.objects.all() libros_filtrados = Book.objects.filter(autor="Tolkien")
```

**Métodos comunes**:

- all(): Recupera todos los objetos.
  
- filter(): Filtra objetos según criterios.
  
- get(): Obtiene un objeto único
  
- create(): Crea un nuevo objeto.
  
- update(): Actualiza objetos.

- count(): Cuenta los registros

- first(): Obtiene el primer registro
  
- last(): Obtiene el ultimo registro
  
- Managers personalizados: Puedes crear managers personalizados para añadir métodos específicos o modificar el comportamiento de las consultas.
  
- Chaining: Los métodos de los managers se pueden encadenar para construir consultas complejas.
  
- Lazy evaluation: Las consultas no se ejecutan hasta que realmente se necesitan los resultados, lo que permite una construcción eficiente de consultas complejas.


**Ejemplos**:

1. Al filtro le enviamos un paraemtro y esto nos va a retornar el registro en una lista

    ```
    Author.objects.filter(id=1)
    ```

2. Concatener diferentes managers, en este caso filtramos y borramos

    ```
    Author.objects.filter(id=1).delete()
    ```

3. Concatener maganers, para obtener una lista con todos registros y ordenarla por un parametro

    ```
    Author.objects.all().order_by("name")
    ```