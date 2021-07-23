### Substring in Dataframe Column
``` python
df['Col3'] = df.Col2.str[0:9]
df['Col3'] = df['col'].str.slice(0, 9)
```

### Text Replacements in Dataframe Column
``` python
df['Vo4'] = df.Col2.str.replace('men', 'women', case=False)
df['Vo4'] = df.Col2.str.replace('f.', 'ba', regex=True)
df['Col4'] = df.Col2.str.slice_replace(start=1, stop=3, repl='X')  # change fix part of text
df['Col4'] = df.Col2.str.strip()                                   # remove leading & ending speces (has argument to_strip for change spece to another symbol)
```
### Filter Dataframe
``` python
df[df.Col2.str.startswith('/', na=False)]                          # argument na use for non-string samples
```

### One Hot Encoding of String Categorial Data
``` python
df_1h = pd.get_dummies(df.Col2, drop_first=True                     # return one-hot dataframe
df2 = df['Extras'].str.get_dummies(",")                             # split column using <,> as separator & use the values pointed out for one-hot encoding
```
