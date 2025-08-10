import json
import pyodbc

def read_data(json_file):
    with open(json_file, "r", encoding="utf-8") as f:
        return json.load(f)

def SQL_connect(config_file):
    config = read_data(config_file)
    #should be Config\QuanLyXeDB.json
    conn = pyodbc.connect(
        f"DRIVER={config['DRIVER']};"
        f"SERVER={config['SERVER']};"
        f"DATABASE={config['DATABASE']};"
        f"UID={config['USERNAME']};"
        f"PWD={config['PASSWORD']}"
    )
    return conn
