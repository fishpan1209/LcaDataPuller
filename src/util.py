import pandas as pd
import numpy as np
import os

# need 11 and 09 data as well

def sample_data(dir):
    file_list = get_data_file_list(dir)
    for file in file_list:
        df = read_data(file)
        df_test = df.sample(frac=0.05, replace=True)
        out_file = "{}.sample.csv".format(file)
        print(out_file)
        df_test.to_csv(out_file, sep=',', encoding = 'utf-8')

def get_data_file_list(dir):
    file_list = []
    for file in os.listdir(dir):
        if file.endswith(".xlsx"):
            file_list.append(os.path.join(dir, file))
    print(file_list)
    return file_list

def read_data(file_path):
    df = pd.read_excel(file_path)
    return df

sample_data("data/left")