import csv
import ast
import os
import shutil

def get_data_set(file_name):
    '''We have to convert it into a "understandable format. So we have to clean it up, beucase alot of the tiles is not unicode based right.'''
    with open(file_name, encoding="utf8", errors='ignore') as f:
        reader = csv.reader(f)
        next(reader) # skip header
        data_set = []
        for row in reader:
                try:
                    # We create a single object for each row, that takes the important informations and put them into an array.
                    row_object = {}
                    # Had to decode some characters into a suitable format the computer understands, so we chose to use latin. We also put the information into suitable formats, for better performance and correct indication
                    row_object['adult'], row_object['budget'], row_object['genres'], row_object['original_language'], row_object['original_title'],row_object['overview'], row_object['popularity'], row_object['production_countries'], row_object['release_date'], row_object['revenue'], row_object['runtime'] = row[0:1][0], int(row[2:3][0]), ast.literal_eval(row[3:4][0]), row[7:8][0], str(row[8:9][0]).encode('utf-8').decode('latin-1'),row[9:10][0], float(row[10:11][0]), ast.literal_eval(row[13:14][0]), row[14:15][0], int(row[15:16][0]), float(row[16:17][0])
                    
                    data_set.append(row_object)
                except:
                    pass
    shutil.rmtree(os.getcwd() + '\\__pycache__')
    return data_set