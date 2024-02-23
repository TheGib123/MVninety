# MVninety Overview
MVninety is used to read PRN files. It tries to structure the data into a single data structure. It also allows you to view the different types of meters for further analysis.  

## MVninety Install
Navigate to directory with setup.py and run the below command
```
pip install .
```

## Initialize MVninety
```
import MVninety
file = r'path/to/folder/with/PRN/files'
file = r'file.PRN'

mv_data = MVninety.Read_PRN(file_or_files=file)
```
#### Or specify date time format 
```
mv_data = MVninety.Read_PRN(file_or_files=file, date_time_format='%m-%d-%Y %H:%M:%S')
```

## Accessing MVninety Attributes
There are four attributes you can access. Types will vary between dictionary and list.
```
x = mv_data.raw_data                      # combines all files into one with no formatting
x = mv_data.seperated_data                # combines all files and seperates the meter type with its data
x = mv_data.formatted_data                # combines all files and seperates the meter type with its formatted data
x = mv_data.combined_formatted_data       # combines all files and formats the data
```

## Outputting MVninety Attributes to Console
```
MVninety.raw_data_output(mv_data)
MVninety.seperated_data_output(mv_data)
MVninety.formatted_data_output(mv_data)
MVninety.combined_formatted_data_output(mv_data)
```

## Outputting MVninety Attributes to Files
```
MVninety.raw_data_output(mv_data, 'raw_data.txt')
MVninety.seperated_data_output(mv_data, 'seperated_data.txt')
MVninety.formatted_data_output(mv_data, 'formatted_data.txt')
MVninety.combined_formatted_data_output(mv_data, 'combined_formatted_data.txt')
```

## Outputting Helpful Data Analysis to Files
```
MVninety.recorderIDs_by_header(mv_data, 'recorder_IDs_by_meter.txt')
MVninety.records_count_by_header(mv_data, 'record_counts_by_meter.txt')
```

## Creating Pandas DataFrame
```
import pandas as pd
import numpy as np
df = pd.DataFrame(mv_data.combined_formatted_data, columns=mv_data.formatted_cols)
df['KVA'] = np.sqrt((df['KW'] * df['KW']) + (df['KVAR'] * df['KVAR']))    # creates and calculates column KVA
print(df.head())
```

## Package Improvement
In read_prn.py towards the bottom of the file after the comment break. You will see the functions that parse each meter type. This is a tedious task and requires understanding of what is being recorded. You can make changes here. 