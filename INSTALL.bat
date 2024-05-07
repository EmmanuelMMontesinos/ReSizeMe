@echo off

echo Descargando e instalando Python...
curl -o python-installer.exe https://www.python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe || call :Error "Error al descargar Python"
start /wait python-installer.exe /quiet TargetDir=C:\Python InstallAllUsers=1 PrependPath=1 || call :Error "Error al instalar Python"
del python-installer.exe

echo -------------------------------------------
echo Instalando Pip
python -m ensurepip --upgrade || call :Error "Error al instalar Pip"

echo -------------------------------------------
echo Descargando e Instalando Dependencias: ttkbootstrap, Pillow, Rembg
pip install ttkbootstrap || call :Error "Error al instalar ttkbootstrap"
pip install Pillow || call :Error "Error al instalar Pillow"
pip install Rembg || call :Error "Error al instalar Rembg"
echo -------------------------------------------

echo Instalacción Exítosa!
pause
