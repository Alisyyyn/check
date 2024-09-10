# Импорт модулей для работы с операционной системой и файловой системой
import os
import platform
# Получение информации о текущей операционной системе
system = platform.system()
# Определение команды для сборки исполняемого файла
if (system == 'Windows'):
    os.system('pyinstaller -F -w -i icon.ico main.py --hidden-import="PIL._tkinter_finder" && xcopy /Y /I "assets\\" "dist\\assets\\" && xcopy /Y "icon.png" "dist\\"')
elif (system == 'Linux'):
    os.system('pyinstaller -F -w -i icon.png main.py --hidden-import="PIL._tkinter_finder" && /bin/cp -rf assets/ dist/ && /bin/cp -f icon.png dist/')

