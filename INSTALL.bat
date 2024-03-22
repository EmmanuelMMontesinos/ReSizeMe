@echo off

echo Descargando e instalando Python...
curl -o python-installer.exe https://www.python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe || call :Error "Error al descargar Python"
python-installer.exe /quiet TargetDir=C:\Python || call :Error "Error al instalar Python"
del python-installer.exe

echo Descargando e Instalando Dependencias: ttkbootstrap
pip install ttkbootstrap || call :Error "Error al instalar ttkbootstrap"

echo Instalacción Exítosa!
pause
