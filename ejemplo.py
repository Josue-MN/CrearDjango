'''
djangoproject.com
//instalar django
python
python3
python3 get-pip.py
pip install django

python --version
python -m django -version

//aun no
pip install mysql

//crear projecto django
cd //ruta carpeta
django-admin startproject holaMundoDjango
//este me funciono => py -m django startproject holaMundoDjango
cd //ruta carpeta(holaMundoDjango)
code .

//archivos importantes
settings.py => configuraciones servidor
urls.py => enruta a las paginas

//lanzar proyecto
python manage.py runserver

//apagar el servicio
ctrl + c

//crear aplicacion
python manage.py startapp //nombre app(firstapp)
luego se agrega en el archivo setting.py en my installed apps con una coma y debajo (firstApp)

//vistas con funciones
agregamos lo siguiente en views.py de la app => from django.http import HttpResponse
\\y luego agregamos.
def display(request):
    return HttpResponse("<h1>Hola Mundo</h1>")

//cargar funcuiones
entramos al archivo urls.py y agregar la ruta de la app => from firstApp import views
y en urlpatterns, agregamos => path("hola/", views.display)

//para entrar a la pagina se le agrega a la ip la nueva vista agregada (hola/)
ejemplo(http://127.0.0.1:8000/hola/)

//para una ruta principal en urlpatterns, no se agrega un / con texto para la ruta principal
path("", views.display)

//tarea, agregar una segunda aplicacion con importacion
'''
