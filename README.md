# fastAPI_Ti41
*Demo FastApi*
## Verificar SO y Kernel 
```bash
$uname -a
```
## Muestra la version de Python
```bash
$python3 -V
```
## Agregar Archivos nuevos al repositorio
```bash
$git add .
```
## Crear un Commit con los cambios
```bash
$git commit -m "UPDATED estructura de Proyecto"
```
## Actualizar el Repositorio de Github
```bash
$git push -u origin main
```
## Requeriments 
```
Sirve para guardar las librerias
```

## Instalar la version mas reciente de Python
```
pip3 install -r requirements.txt
```
## Muestra las versiones instaladas
```
pip3 freeze
```
## Uso de Tuberias para dirigir la salida de un comando
```
pip3 freeze > requirements.txt
```
## Uso de tuberia para abrir o crear una base de datos si no existe
```
sqlite3 base.db < base.sql
```
##
adress already in use: significa que uvicorn se esta ejecutando en el puerto 8000
## Detener proceso en segundo plano
```
kill PID
o kill -9 PID
```
## Ejecuta la API
```
 uvicorn main:app --reload
```