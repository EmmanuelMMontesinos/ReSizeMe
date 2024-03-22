@echo off

echo Desistalando ReSizeMe y sus dependencias.
pip uninstall ttkbootstrap

del resizeme.bat
del resizeme.py
del INSTALL.bat
del Pipfile
del Pipfile.locke

echo Desistalación Exítosa!
pause