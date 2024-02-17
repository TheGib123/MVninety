from datetime import datetime
from datetime import timedelta
import os

class Read_PRN():

    def __init__(self, file_or_files, date_time_format='%m-%d-%Y %H:%M:%S'):
        '''
        raw_data - list that combines all file or files data with modification
        seperated_data - dictionay that groups each meter header with its hourly data from all file or files
        formatted_data - dictionary that groups each meter header with its hourly data in a standard fromat from all file or files
        combined_formatted_data - list of all hourly data in a standard format from all file or files
        '''
        self.raw_data = None
        self.seperated_data = None
        self.formatted_data = None
        self.combined_formatted_data = None
        self.date_time_format = date_time_format
        self.file_or_files = file_or_files

        if ('.PRN' in file_or_files.upper()):     # if .PRN is in varaible - then we assume it is a file
            self.raw_data = self.__read_file(self.file_or_files)
        else:                                  # else we assume the variable is a file path
            self.file_or_files = self.__list_files_recursive(self.file_or_files)    # returns a list of all .PRN files in the directory
            if (len(self.file_or_files) == 0):
                raise Exception('Directory could not be found or has no .PRN files')
            self.raw_data = self.__read_all_files(self.file_or_files)   

        self.seperated_data = self.__seperate_meter_types()
        self.formatted_data = self.__format_data()
        self.combined_formatted_data = self.__combine_formatted_data()

    def __list_files_recursive(self, path):
        files = []
        # r = root, d = directories, f = files
        for r, d, f in os.walk(path):
            for file in f:
                if ('.PRN' in file[len(file)-4:len(file)].upper()):
                    files.append(os.path.join(r, file))
        lst = [file for file in files]
        return lst

    def __combine_formatted_data(self):
        data = []
        for header, rows in self.formatted_data.items():
            for row in rows:
                data.append(row)
        return data

    def __format_data(self):
        formatted_data = {}
        for header, rows in self.seperated_data.items():
            formatted_rows = []
            if (header == '"RECORDER ID" " DATE" " HOUR" " IN" " UN" " KW    " " KVAR  " " KVAR  " "       "'): 
                formatted_rows = self.__headers_1(rows)
            elif (header == '"RECORDER ID" " DATE" " HOUR" " IN" " UN" " KW    " " KVAR  " " KVAR  " " KW    " " KVAR  " " KVAR  " "       " "       "'):
                formatted_rows = self.__headers_2(rows)
            elif (header == '"RECORDER ID" " DATE" " HOUR" " IN" " UN" " KW    " " KW    " " KW    " "       "'):
                formatted_rows = self.__headers_3(rows)
            elif (header == '"RECORDER ID" " DATE" " HOUR" " IN" " UN" " KW    " " KW    " " KVAR  " " KVAR  "'):
                formatted_rows = self.__headers_4(rows)
            elif (header == '"RECORDER ID" " DATE" " HOUR" " IN" " UN" " KW    " " KW    " " MVAR  " " MVAR  "'):
                formatted_rows = self.__headers_5(rows)
            elif (header == '"RECORDER ID" " DATE" " HOUR" " IN" " UN" " KW    " " KVAR  " "       " "       "'):
                formatted_rows = self.__headers_6(rows)

            if (len(formatted_rows) > 0):
                formatted_data[header] = formatted_rows
        return formatted_data

    def __seperate_meter_types(self):
        data = {}
        temp_data = []
        header = ''
        for row in self.raw_data:
            #print(row)
            #row = row[0]
            row = row.strip()
            if ('RECORDER ID' in row and temp_data == []):
                header = row
            elif ('RECORDER ID' in row):
                if (header in data):
                    data[header] = data[header] + temp_data
                else:
                    data[header] = temp_data
                temp_data = []
                header = row
            else:
                temp_data.append(row)
        if (header in data):
            data[header] = data[header] + temp_data
        else:
            data[header] = temp_data
        return data
    
    def __read_file(self, file_name):
        raw_data = []
        with open(file_name, 'r') as file:
            for line in file:
                line = line.replace(',', ' ')
                raw_data.append(line.rstrip())
        return raw_data

    def __read_all_files(self, file_names):
        lines = []
        for file in file_names:
            print(file)
            lines = lines + self.__read_file(file)
        return lines

    ####################
    def __format_datetime(self, row):
        d = row[1]
        t = row[2]
        del row[1]
        del row[1]
        year = '20' + d[4:6]
        month = d[0:2]
        day = d[2:4]
        hour = t[0:2]
        dt = None
        if (hour == '24'):
            dt = datetime(int(year),int(month),int(day))
            dt = dt + timedelta(days=1)
        else:
            dt = datetime(int(year),int(month),int(day), int(hour))
        dt = dt.strftime(self.date_time_format)
        row.append(dt)
        return row

    def __headers_1(self, rows):
        new_rows = []
        for row in rows:
            row = row.replace('"','')
            row = row.split()
            del row[3]
            del row[3]
            del row[5]
            del row[5]
            row[3] = int(row[3])
            row[4] = int(row[4])
            row = self.__format_datetime(row)
            new_rows.append(row)
        return new_rows

    def __headers_2(self, rows):
        new_rows = []
        for row in rows:
            row = row.replace('"','')
            row = row.split()
            del row[3]
            del row[3]
            del row[3]
            del row[3]
            del row[3]
            del row[5]
            del row[5]
            del row[5]
            row[3] = int(row[3])
            row[4] = int(row[4])
            row = self.__format_datetime(row)
            new_rows.append(row)
        return new_rows

    def __headers_3(self, rows):
        new_rows = []
        for row in rows:
            row = row.replace('"','')
            row = row.split()
            del row[3]
            del row[3]
            del row[5]
            del row[5]
            row[3] = int(row[3])
            row[4] = int(row[4])
            row = self.__format_datetime(row)
            new_rows.append(row)
        return new_rows

    def __headers_4(self, rows):
        new_rows = []
        for row in rows:
            row = row.replace('"','')
            row = row.split()
            del row[3]
            del row[3]
            del row[4]
            del row[4]
            row[3] = int(row[3])
            row[4] = int(row[4]) * -1
            row = self.__format_datetime(row)
            new_rows.append(row)
        return new_rows

    def __headers_5(self, rows):
        new_rows = []
        for row in rows:
            row = row.replace('"','')
            row = row.split()
            del row[3]
            del row[3]
            del row[4]
            del row[4]
            row[3] = int(row[3])
            row[4] = int(row[4]) * -1
            row = self.__format_datetime(row)
            new_rows.append(row)
        return new_rows

    def __headers_6(self, rows):
        new_rows = []
        for row in rows:
            row = row.replace('"','')
            row = row.split()
            del row[3]
            del row[3]
            del row[5]
            del row[5]
            row[3] = int(row[3])
            row[4] = int(row[4])
            row = self.__format_datetime(row)
            new_rows.append(row)
        return new_rows