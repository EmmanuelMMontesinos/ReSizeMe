@echo off

echo Desistalando ReSizeMe y sus dependencias.
pip uninstall -y -r requirements.txt || call :Error "Error al desinstalar dependencias"

del resizeme.bat
del resizeme.py
del INSTALL.bat
del Pipfile
del Pipfile.locke
del requirements.txt


echo Desistalación Exítosa!
pause