>[Объект Series](#series)  
>[Объект DataFrame](#dataframe)  
>[Операции над объектами DataFrame](#operations)  

``` python
import numpy as np
import pandas as pd
```
## Объект Series <a name="series"></a>
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

#### Размеробъекта Series
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

## Объект DataFrame <a name="dataframe"></a>
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

### Копирование DataFrame
```python
df_copy = df.copy(deep=True)
```

### Просмотр свойств DataFrame
```python
len(df)                   ; количество строк в DataFrame
df.columns                ; столбцы DataFrame (для получения списка столбцов использовать to_list())
df.shape                  ; размерность DataFrame
df.dtypes                 ; типы столбцов

df.info()                 ; краткая сводка: типы столбцов и кол-во не NaN значений в каждом из них
df.describe()             ; статистика по числовым столбцам (среднее, медиана, квартили, ...)
df['col_1'].describe()    ; статистика для указанного столбца

df.head(10)               ; вывести первые 10 строк DataFrame
df.tail(10)               ; вывести последние 10 строк DataFrame

df.columns.to_list()      ; список названий столбцов
df.Col_2.to_list()        ; преобразование значений столбца в список
df['Col_2'].unique()      ; уникальные значения в столбце
df.Сol_2.value_counts()   ; количества каждого из значений в столбце
df.index.to_list()        ; список значений индекса
```

## Операции над объектами DataFrame <a name="operations"></a>
### Обращение к строкам и столбцам
Функции `.iloc()` и `.loc()` возвращают объект Series, если результат содержит 1 столбец или 1 строку, и эта строка задана явно номером или текстовым индексом (заголовком). Во всех других случаях, возвращается объект DataFrame, например, если единственный столбец задан списком [col_name].
```
df.iloc[:, 1]            ; обращение ко второму столбцу по номеру
df.iloc[:, -1]           ; обращение к последнему столбцу
df.iloc[0]               ; первая строка DataFrame
df.iloc[1]               ; вторая строка DataFrame
df.iloc[-1]              ; последняя строка DataFrame

df.loc[<rows>, <cols>]   ; получение строк DataFrame по индексам строк или названиям столбцов
df.iloc[<rows>, <cols>]  ; обращение к указанным строкам заданных столбцов (rows и cols могут быть числами|списками|bool-значениями)

; фильтрация строк
df.loc[df['email'].str.endswith("mail.ru")]   ; все строки, заканчивающиеся на 'mail.ru'
df.loc[df['name'].isin(['Bob', 'Alice'])]     ; все строки с указанными именами
df.loc[df.Col4 =='May', 'Col1':'Col2']          ; отбор строк столбцов по условию

; составные условия фильтра
df.loc[df['email'].str.endswith("gmail.com") & (df['name'] == 'Anna')] 
df.loc[df['company_name'].apply(lambda x: len(x.split(' ')) == 4)] 
df.loc[(df['id'] > 100) & (df['id'] <= 200), ['postal', 'web']] 
```

### Преобразование типа столбцов

### Переименование столбцов
```python
df.columns = ['Col_1','Col_2','Col_3']               ; изменить названия ВСЕХ столбцов
df.rename(columns={'ColOld_1':'ColNew_1',            ; переименовать указанные столбцы
                   'ColOld_2':'ColNew_2'}, 
                    inplace=True)
df.rename(columns=lambda x: x +1)                    ; mass renaming of columns
d.rename(columns=lambda x: x.replace(' ', '_'))   ; замена пробелов в названиях столбцов на подчеркивания
```

### Добавление строк
```python
new_line = {'id':3000, 'ShopName':'КЛ-98', 'DateOpen':pd.datetime(2020,1,1) }
df.append([new_line, new_line2], ignore_index=True)   ; добавляет строки в конец; возвращает новый DataFrame
df1.append(df2)                                       ; добавляет строки df1 в конец df2 (у df1 и df2 столбцы должны быть одинаковыми)
df.append(df.sum(axis=0), ignore_index=True)          ; добавляет строку с суммой значений для каждого столбца
pd.concat([df1, df2], ignore_index=True)              ; объединение строк двух DataFrame'ов
```

### Добавление столбцов
```python
df['Sales'] = 0                                       ; добавить столбец 'Sales', заполненный нулями
df['Competitor'] = [True]*7 + [False*2]               ; добавить столбец из 5 значений True и 2 значений False

pd.concat([df1, df2],axis=1)       ; добавляет столбцы DF df1 в конец DF df2 (число строк должны быть одинаковым)
df1.join(df2,on=col1,how='inner')  ; соединение столбцов df1 и df2, где совпадают значения для столбца col1 (may use 'left', 'right', 'outer', 'inner')
df2.merge(df1, left_on=’Col_id’, right_on=’Col_id’, suffixes=(‘_left’, ‘_right’))  ; аналог LEFT JOIN
```

### Удаление строк
```python
df.iloc[5:,]               ; удалитье первые 5 строк, используя iloc() и слайсинг
df.drop([7,8], axis=0)     ; удалить 7-ю и 8-ю строки DF; возвращает новый DF (можно указать inplace=True)
df.drop('USA', axis=0)     ; удаление строки с индексом USA


```

### Удаление столбцов
```python
df.drop('Col_2r', axis=1, inplace=True)             ; удаление одного стобца
df.drop(['Col_1', 'Col_4'], axis=1, inplace=True)   ; удаление нескольких столбцов
```

### Применение функции apply и applymap
```python
df.loc[:,'Col2':'Col4'].apply(max, axis=0)        ; получить максимальные значения в столбцах
df.loc[:,'Col2':'Col4'].apply(np.argmax, axis=1)  ; получить название столбца с максимальным значением в строках
df.loc[:,'Col2':'Col4'].applymap(float)           ; применить float ко всем значениям в таблице - ИЗМЕНЯЕТ DataFrame !!
```
### Объединение нескольких DataFrame
[Merge and Join DataFrames with Pandas](https://www.shanelynn.ie/merge-join-dataframes-python-pandas-index-1/)
```
; объединение df1 и указанных столбцов df2 по стобцу id
result = pd.merge(df1, df2[['id', 'platform', 'device']], on='id', how='left')
```

## Индексация
```python
df.set_index("Col4", inplace=True)             ; установить указанный столбец в качестве индекса
df.reset_index()                               ; сбросить индекс в значения, начинающиеся с 0
df.index = pd.date_range('1900/1/30',          ; создание date-индекса
                         periods=df.shape[0])
df.rename(index=lambda x: x + 1)               ; mass renaming of index
```
