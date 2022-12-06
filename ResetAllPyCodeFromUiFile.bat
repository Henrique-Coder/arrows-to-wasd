@echo off

:: Converting Main Project (.ui > .py)
pyuic5 -x arrowstowasd.ui -o arrowstowasd.py

:: Converting Image File (.qrc > .py)
pyrcc5 images.qrc -o dependencies/imgs.py

exit /b 0
