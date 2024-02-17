#### MVninty Tutorial ####
import MVninty

########### MVninty can read a single PRN and multiple PRN's from a folder structure #########
### All meter data
# file = r'meter_data'
### 2023 meter data
# file = r'meter_data\2023'
### Single file of meter data
file = r'meter_data\2023\SUBS 12-23\SUB_1223.PRN'


########### Retriving the MVninty data in several formats ########
### Read in meter data
mv_data = MVninty.Read_PRN(file_or_files=file)

### 4 formats
# mv_data.raw_data                      # combines all files into one with no formatting
# mv_data.seperated_data                # combines all files and seperates the meter type with its data
# mv_data.formatted_data                # combines all files and seperates the meter type with its formatted data
# mv_data.combined_formatted_data       # combines all files and formats the data

########### outputting data to console #########
# MVninty.raw_data_output(mv_data)
# MVninty.seperated_data_output(mv_data)
# MVninty.formatted_data_output(mv_data)
# MVninty.combined_formatted_data_output(mv_data)

########### outputting data to files #########
MVninty.raw_data_output(mv_data, 'raw_data.txt')
MVninty.seperated_data_output(mv_data, 'seperated_data.txt')
MVninty.formatted_data_output(mv_data, 'formatted_data.txt')
MVninty.combined_formatted_data_output(mv_data, 'combined_formatted_data.txt')

########### outputting helpful analysis data to files #########
MVninty.recorderIDs_by_header(mv_data, 'recorder_IDs_by_meter.txt')
MVninty.records_count_by_header(mv_data, 'record_counts_by_meter.txt')


########### createing dataframe with data ###########
import pandas as pd
import numpy as np

df = pd.DataFrame(mv_data.combined_formatted_data, columns=['RECORDER_ID', 'KW', 'KVAR', 'DATE_TIME'])
df = df.drop_duplicates()
df['KVA'] = np.sqrt((df['KW'] * df['KW']) + (df['KVAR'] * df['KVAR']))
print(df.head(15))


