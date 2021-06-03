# Instrucciones de instalación

1. Instalar las dependencias del fichero requirements.txt

```
pip install -r requirements.txt
```

2. Crear la variable de entorno `FLASK_APP` con el valor `run.py`
En Linux/Mac se encuentra en env/bin/activate
. Al final del fichero añadimos lo siguiente:
'''
export FLASK_APP="run.py"
'''

3. Lanzar la aplicación

```
flask run
```
