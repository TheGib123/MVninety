import MVninty
import os
import pandas as pd
import numpy as np

### All meter data
# file = r'meter_data'
### 2023 meter data
file = r'meter_data\2023'
### Single file of meter data
#file = r'meter_data\2023\SUBS 12-23\SUB_1223.PRN'

mv_data = MVninty.Read_PRN(file_or_files=file)

# create_files
os.mkdir('output')
os.chdir('output')

MVninty.raw_data_output(mv_data, 'raw_data.txt')
MVninty.combined_formatted_data_output(mv_data, 'combined_formatted_data.txt')
MVninty.records_count_by_header(mv_data, 'record_counts_by_meter.txt')

os.mkdir('seperated_data')
os.chdir('seperated_data')
MVninty.seperated_data_output(mv_data, 'seperated_data.txt')

os.chdir('..')
os.mkdir('formatted_data')
os.chdir('formatted_data')
MVninty.formatted_data_output(mv_data, 'formatted_data.txt')

os.chdir('..')
os.mkdir('recorderIDs_data')
os.chdir('recorderIDs_data')
MVninty.recorderIDs_by_header(mv_data, 'recorder_IDs_by_meter.txt')