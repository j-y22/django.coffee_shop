# Crear entorno
python -m venv [ruta]
python3 -m venv ~/.envs/[nombre_nuevo_entorno]
# activar el entorno
se tiene que hacer cada vez que quiero hacer algo al comezar
en la terminal al lado del nombre aparece en parentesis el nombre del entorno
source  ~/.envs/my-first-envs/bin/activate
# instalar paquetes y dependencias
solo al principio, cuando se crea el entorno
pip install django
pip install ipython (para las sugerencias inteligentes en la shell de python)
pip install Pillow (sirve para subir imagenes?)
Otra opción es tener un archivo txt donde ponga las dependencias (django==[version]) y ejecutar pip -r install [nombre].txt
que debería poner en cada projecto cada dependencia para llevar un registro
# Comenzar nuevo proyecto Django
django-admin startproject [nombre_del_proyecto]
# Select interpreter
En la versión de python en vscode, seleccionar la versión que está dentro de la ruta del entorno, dentro de bin.
mientras que para html seleccionar el que viene por defecto, el de django va mal
# Añadir el gitignore
Hay una web que lo genera
https://www.toptal.com/developers/gitignore
buscar django
# Comenzar una app
./manage.py startapp [nombre]
# Añadir nombre de app a settings 
En INSTALLED_APPS
# Activar servidor(ver pagina web)
python manage.py runserver

./manage.py dbshell shell de la db(hacer select …)
.tables
.schema _nombre-de-la-tabla
selects


# Pasar los datos de python shell al DB
python manage.py makemigrations
python manage.py migrate

# crear/modificar/eliminar datos del dbshell
python manage.py shell 
from my_first_app.models import Car
my_car = Car(title="BMW", year = "2023")
print(my_car)
my_car.save
Car.objects.filter()
get()
delete()

#Forms
creo un archivo nuevo para esto (forms.py)
son clases
importar forms y usar el modulo forms en vez de modules.algo