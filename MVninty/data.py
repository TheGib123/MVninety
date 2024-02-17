
################# OUTPUTING DATA #########################

def __output_console(data):
    if (type(data) is list):
        for row in data:
            print(row)
    elif (type(data) is dict):
        for header, rows in data.items():
            print(header)
            for row in rows:
                print(row)
            print()

def __output_file(data, file_name):
    if (type(data) is list):
        with open(file_name, 'w') as f:
            for row in data:
                if (type(row) is list):
                    for i in row:
                        f.write(str(i) + ', ')
                    f.write('\n')
                else:
                    f.write(row)
                    f.write('\n')
            f.close()
    elif (type(data) is dict):
        file_count = 1
        for header, rows in data.items():
            with open(str(file_count) + file_name, 'w') as f:
                f.write(header)
                f.write('\n')
                for row in rows:
                    if (type(row) is list):
                        for i in row:
                            f.write(str(i) + ', ')
                    else:
                        f.write(row)
                    f.write('\n')
                f.close()
            file_count = file_count + 1



################# Different Data Outputs #########################

def raw_data_output(mv_data, file_name=None):
    output = mv_data.raw_data
    if (file_name == None):
        __output_console(output)
    else:
        __output_file(output, file_name)

def seperated_data_output(mv_data, file_name=None):
    output = mv_data.seperated_data
    if (file_name == None):
        __output_console(output)
    else:
        __output_file(output, file_name)

def formatted_data_output(mv_data, file_name=None):
    output = mv_data.formatted_data
    if (file_name == None):
        __output_console(output)
    else:
        __output_file(output, file_name)

def combined_formatted_data_output(mv_data, file_name=None):
    output = mv_data.combined_formatted_data
    if (file_name == None):
        __output_console(output)
    else:
        __output_file(output, file_name)

def records_count_by_header(mv_data, file_name=None):
    total_rows = 0
    output = []
    for header, rows in mv_data.seperated_data.items():
        rows_length = len(rows)
        output.append(header)
        output.append('count of hourly reads ' + str(rows_length))
        output.append('\n')
        total_rows = total_rows + rows_length
    output.append('total rows ' + str(total_rows))
    if (file_name == None):
        __output_console(output)
    else:
        __output_file(output, file_name)

def recorderIDs_by_header(mv_data, file_name=None):
    output = {}
    for header, rows in mv_data.formatted_data.items():
        recorderIDs = []
        for row in rows:
            recorderID = row[0]
            if (recorderID not in recorderIDs):
                recorderIDs.append(recorderID)
        output[header] = recorderIDs
    if (file_name == None):
        __output_console(output)
    else:
        __output_file(output, file_name)

def meter_sample_output(mv_data, file_name=None, num_records=2):
    output = {}
    for header, rows in mv_data.seperated_data.items():
        tmp_list = []
        for row_index in range(num_records):
            tmp_list.append(rows[row_index])
        output[header] = tmp_list
    if (file_name == None):
        __output_console(output)
    else:
        __output_file(output, file_name)
        