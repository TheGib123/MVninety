import MVninety
import os
import pandas as pd
import numpy as np

### All meter data
# file = r'meter_data'
### 2023 meter data
file = r'meter_data\2023'
### Single file of meter data
#file = r'meter_data\2023\SUBS 12-23\SUB_1223.PRN'

mv_data = MVninety.Read_PRN(file_or_files=file)

# create_files
os.mkdir('output')
os.chdir('output')

MVninety.raw_data_output(mv_data, 'raw_data.txt')
MVninety.combined_formatted_data_output(mv_data, 'combined_formatted_data.txt')
MVninety.records_count_by_header(mv_data, 'record_counts_by_meter.txt')

os.mkdir('seperated_data')
os.chdir('seperated_data')
MVninety.seperated_data_output(mv_data, 'seperated_data.txt')

os.chdir('..')
os.mkdir('formatted_data')
os.chdir('formatted_data')
MVninety.formatted_data_output(mv_data, 'formatted_data.txt')

os.chdir('..')
os.mkdir('recorderIDs_data')
os.chdir('recorderIDs_data')
MVninety.recorderIDs_by_header(mv_data, 'recorder_IDs_by_meter.txt')