import numpy as np
import pandas as pd
import os, re
import sys


files = os.listdir('./data')
files = [file for file in files if re.search('comments.*\.csv', file)]

data_list = []
for file in files:
    data = pd.read_csv('./data/{}'.format(file))
    data_list.append(data)
data = pd.concat(data_list)
print('columns: {}'.format(data.columns))
columns = ['target_link', 'title', 'user_id', 'user_name', 'comment']
data = data[columns]

import MySQLdb
import sshtunnel
from config import config

sshtunnel.SSH_TIMEOUT = 5.0
sshtunnel.TUNNEL_TIMEOUT = 5.0

with sshtunnel.SSHTunnelForwarder(
    config['remote_machine']['hostname'],
    ssh_username=config['remote_machine']['ssh_username'], 
    ssh_password=config['remote_machine']['ssh_password'],
    remote_bind_address=(config['remote_machine']['msql_hostname'], 3306)
) as tunnel:
    con = MySQLdb.connect(
        user=config['mysql_dev']['user'],
        passwd=config['mysql_dev']['passwd'],
        host='127.0.0.1', #have to set this exact value
        port=tunnel.local_bind_port,
        db=config['mysql_dev']['db'],
    )
    # Do stuff
    query = """INSERT INTO youtube_comment (target_link, title, user_id, user_name, comment)
    VALUES (%s, %s, %s, %s, %s);
    """
    cursor = con.cursor() #Connection.cursor() return Cursor object
    params = list(data.values)
    print(params)
    try: 
        cursor.executemany(query, params)
        con.commit()
    except Exception as e:
        print('Error: ', e)
        con.rollback()
        raise Exception(e)
    data = pd.DataFrame(data)
    con.close()