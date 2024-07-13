@echo off
setlocal

:: Verifica que se haya proporcionado un nombre de proyecto
if "%~1"=="" (
    echo Por favor, proporciona un nombre de proyecto.
    echo Uso: create_project_django.bat nombre_proyecto
    exit /b 1
)

set "nombre_proyecto=%~1"
set "nombre_entorno_virtual=%nombre_proyecto%_env"

:: Crear entorno virtual
python -m venv %nombre_entorno_virtual%

:: Activar entorno virtual
call %nombre_entorno_virtual%\Scripts\activate

:: Instalar Django
pip install django

:: Crear proyecto Django
django-admin startproject %nombre_proyecto%

:: Navegar al directorio del proyecto
cd %nombre_proyecto%

:: Ejecutar el servidor de desarrollo
python manage.py runserver

endlocal
