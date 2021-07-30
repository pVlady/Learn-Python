``` python
import numpy as np
import pandas as pd
```
## Объект Series
Объект Series представляет _индексированный_ столбец данных.  
Допустимые типы индекса: _int64_, _string_, _RangeIndex_, _DateTimeIndex_, _PeriodIndex_.  
``` pyhon
s = pd.Series([1, 2, 3, 4])             ; создание объекта Series из списка (или другогоиттерируемого объекта)
s = pd.Series([v]*100)                  ; создание объекта Series из 100 одинаковых значений v
s = pd.Series(np.arrange(1, 10))        ; создание объекта Series из numpy-последовательности
s = pd.Series(np.linspace(0, 9, 5))     ; создание объекта Series из numpy-последовательности

np.random.seed(12345)                   ; создание объекта Series из numpy-массива случайных значений
s = pd.Series(np.random.normal(size=5))
```
Если объект Series имеет целочисленный индекс, то в операторе `[ ]` обращение к элементу происходит по значению индекса, например, `s[2]` это элемент, индекс которого равен 2.  
Если тип индекса иной, то при указании в операторе `[ ]` целого числа обращение происходит по позиции элемента (также как для списка или массива).  
Чтобы устранить путаницу рекомендуется для обращения к элементам использовать `.loc[ ]` и `.iloc[ ]`.
```
s[['a', 'd']]   ; элементы объекта Series, для которых индекс равен 'a' и 'd'.
s.loc['a']      ; элемент объекта Series, индекс которого равен 'a' (при указании несуществующего индекса вернет NaN)
s.iloc[0]       ; первый элемент объекта Series (при указании несуществующей позиции возникнет исключение)
```

#### Размер объекта Series
``` python
len(s)
s.size
s.shape   ; вернет кортеж вида (10,)
```

#### Индекс объекта Series
``` python
s.index                                    ; возвращает индекс объекта Series
dates = pd.date_range('2016-01-01',        ; возвращает объект DateTimeIndex (можно указать параметр freq='D'|'M'|'Y')
                      '2019-01-01')
s = pd.Series([21,20,19,25], index=dates)  ; создает объект Series с индексом типа DateTimeIndex - временной ряд (лишние даты индекса отбрасываются)
```

#### Получение значений объекта Series
```
s.values         ; значения объекта Series в виде numpy-массива
s.take([1,3,5])  ; возвращает значения объекта Series в указанных позициях
```

#### Описательные статистики для объекта Series
``` python
s.median()
s.mean()
s.max()
s.min()
```

## Объект DataFrame
Объединяет несколько объектов Series с общим индексом. Если в названии столбца нет пробелов, то обращение к столбцу может осуществляться через вычисляемое свойство: `df.ColName`. В противном случае используется синтаксис `df["ColName"]`.
- Для объекта Series оператор `[ ]` возвращает строки
- Для объекта DataFrame оператор `[ ]` возвращает столбцы данных.

### Чтение данных в DataFrame
```python
df = pd.read_csv('file.csv',          ; число в header указывает номер строки-заголовка,
                 header=0, sep='\t')  ;   а значения True / False его наличие или отсутствие
                 
; прочитать данные в указанной кодировке с преобразованием столбца 'CtrlDate' к типу даты
; и установкой его как индекса DataFrame
df = pd.read_csv('file.csv',                       
                 parse_dates=['CtrlDate'],
                 index_col='CtrlDate',
                 encoding='ISO-8859–1)
```

### Чтение данных из Excel
```python
df = pd.read_excel('file.xls', sheet_name='Sheet1', usecols=[0, 2, 3])  ; чтение заданных столбцов с листа Sheet1
df = pd.read_excel('file.xls', na_values='Missing', skiprows=2)         ; чтение с пропуском первых строк
; вместо skiprows=2 можно использовать header=2

; преобразование данных при импорте
df = pd.read_excel('file.xls', 'Sheet1', converters={'MyBools': bool})    ; способ 1
df = pd.read_excel('file.xls', dtype={'MyInts': 'int64', 'MyText': str})  ; способ 2

; чтение данных из разных листов
with pd.ExcelFile('file.xls') as xls:
    df1 = pd.read_excel(xls, 'Sheet1')
    df2 = pd.read_excel(xls, 'Sheet2')
```

### Чтение из БД SQL
```python
import pyodbc
import pandas.io.sql as psql

cn = pyodbc.connect('DRIVER={SQL Server};SERVER=servername;DATABASE=mydb;UID=username;PWD=password') 
cursor = cn.cursor()
df = psql.frame_query('select * from Books', cn)  ; depricated method
cn.close()

import oursql
cn = oursql.connect(host="localhost", user="me", passwd="mypassword", db="classicmodels")
df = pd.read_sql('select * from Books', cn)
```

### Создание DataFrame из данных
```python
pd.DataFrame(dict)                   ; из dict: ключи словаря = названия столбцов, значения в виде списка = данные для столбца
pd.DataFrame(np.random.rand(20, 5))  ; DataFrame c 5-ю столбцами по 20 random floats

pd.DataFrame([[1,'Bob', 'Builder'],  ; создание из списка списков со столбцами 1,2,3; Bob,Sally.Scott; ...
              [2,'Sally', 'Baker'],
              [3,'Scott', 'Candle Stick Maker']], 
              columns=['id','name', 'occupation'])
```

### Копирование DF
```python
df_copy = df.copy(deep=True)
```

### Просмотр свойств DataFrame
```python
df.columns      ; список столбцов
df.shape        ; размерность DataFrame
df.dtypes       ; типы столбцов

df.info()       ; краткая сводка: типы столбцов и кол-во не NaN значений в каждом из них
df.describe()   ; статистика по числовым столбцам (среднее, медиана, квартили, ...)

df.head(10)     ; вывести первые 10 строк DataFrame
df.tail(10)     ; вывести последние 10 строк DataFrame
```
