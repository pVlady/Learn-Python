## Установка, настройка, обновление python
Какие пакеты python установлены в системе (Windows):
```bash
py -m pydoc modules  ; список всех установленных модулей — то же, что и >>> help("modeles")
pip freeze           ; список модулей, установленных через pip
```
Обновление пакета `pip` и установка основных пакетов
```bash
py -m pip install --upgrade pip
py -m install numpy
py -m install scipy
py -m install statsmodels
py -m install -U scikit-learn
py -m pip install pandas          ; подтянет numpy, если не был установлен
py -m pip install pyodbc
py -m pip install pywin32
py -m pip install xlrd
py -m pip install xlwt
py -m pip install openpyxl
```

## Создание виртуальных окружений
Начиная с версии python 3.3 нет необходимости устанавливать `virtialenv`, поскольку модуль `venv` входит в начальную установку.\
Чтобы создать виртуальное окружение, необходимо перейти в каталог проекта и выполнить команду, которая создаст его в папке *env_folder_name*:
```bash
python3 -m venv env_folder_name
```
>*Каталог виртуальной среды необходимо исключить из системы контроля версий.*

>*Перед установкой пакетов в виртуальное окружение, необходимо его активировать.*

Действие                              | Windows                               | Linux
:--                                   |:--                                    |:--
Активация окружения                   | `.\env\Scripts\activate`              | `source env/bin/activate`
Проверка активации окружения          | `where pyrhon`                        |`which python`
Расположение интерпретатора           | *...\env\Scripts\python.exe*          | *.../env/bin/python*
Установить пакет numpy                |`py -m pip install numpy`              |`python3 -m pip install numpy`
Установить указанную версию numpy     |`py -m pip install numpy==1.24.1`      |`python3 -m pip install requests==1.24.1`
Установить последнюю версию           |`py -m pip install --upgrade numpy`    |`python3 -m pip install --upgrade numpy`
Установка из файла *[requirements.txt](https://pip.pypa.io/en/latest/reference/requirements-file-format/#requirements-file-format)* |`py -m pip install -r requirements.txt`|`python3 -m pip install -r requirements.txt`
Просмотр установленных пакетов        |`py -m pip freeze`                     |`python3 -m pip freeze`
Покинуть окружение                    |`deactivate`                           |`deactivate`

>Чтобы установить последнюю версию пакета заданного выпуска, нужно использовать `numpy>=1.0.0,<2.0.0`
