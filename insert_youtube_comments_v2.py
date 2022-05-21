import numpy as np
import pandas as pd
import os, re
import sys
import pymysql
from config import config
files = os.listdir('./data')
files = [file for file in files if re.search('comments.*\.csv', file)]

data_list = []
for file in files:
    data = pd.read_csv('./data/{}'.format(file))
    data_list.append(data)
data = pd.concat(data_list)
#clean data convert np.nan to None
print('columns: {}'.format(data.columns))
columns = ['user_id', 'user_name']
data = data[columns]
data = data.replace({np.nan: None}) #replace np.nan to None
# data['title'] = data['title'].str.replace('|', '')
# data['title'] = data['title'].str.replace('&', '')
# data['title'] = data['title'].apply(lambda x: str(x))
# data['title'] = 'test string'


mysql_config = config.get('MYSQL_DB')
con= pymysql.connect(**mysql_config) #return Connection object
# con.set_character_set('utf8')
data.to_sql(name='youtube_comment', con=con)
