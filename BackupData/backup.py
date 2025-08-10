import json
import pyodbc
from datetime import datetime

def read_data(json_file):
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

def SQL_connect(config):
    config_SQL = read_data(config)
    conn = pyodbc.connect(
        f"DRIVER={config_SQL['DRIVER']};"
        f"SERVER={config_SQL['SERVER']};"
        f"DATABASE={config_SQL['DATABASE']};"
        f"UID={config_SQL['USERNAME']};"
        f"PWD={config_SQL['PASSWORD']}"
    )
    return conn  
def json_type(json_file):
    data = read_data(json_file)
    if isinstance(data, list):
        return "list"
    elif isinstance(data, dict):
        return "dict"
    else:
        return "unknown"
    
def is_datetime_str(s):
    if not isinstance(s, str):
        return False
    for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d"):
        try:
            datetime.datetime.strptime(s, fmt)
            return True
        except:
            continue
    return False

def element_type(json_file):
    data = read_data(json_file)
    columns = {}
    if json_type(json_file) == "list":
        # Lấy phần tử đầu tiên làm mẫu để đoán kiểu
        sample = data[0] if data else {}
        for key, value in sample.items():
            if isinstance(value, int):
                columns[key] = f"[{key}] INT"
            elif isinstance(value, float):
                columns[key] = f"[{key}] FLOAT"
            elif isinstance(value, bool):
                columns[key] = f"[{key}] BIT"
            elif is_datetime_str(value):
                columns[key] = f"[{key}] DATETIME"
            elif isinstance(value, str):
                columns[key] = f"[{key}] NVARCHAR(MAX)"
            else:
                columns[key] = f"[{key}] NVARCHAR(MAX)"
    elif json_type(json_file) == "dict":
        for key, value in data.items():
            if isinstance(value, int):
                columns[key] = f"[{key}] INT"
            elif isinstance(value, float):
                columns[key] = f"[{key}] FLOAT"
            elif isinstance(value, bool):
                columns[key] = f"[{key}] BIT"
            elif is_datetime_str(value):
                columns[key] = f"[{key}] DATETIME"
            elif isinstance(value, str):
                columns[key] = f"[{key}] NVARCHAR(MAX)"
            else:
                columns[key] = f"[{key}] NVARCHAR(MAX)"
    else:
        return []

    return list(columns.values())
def Gen_table(json_file):
    columns = element_type(json_file)
    if not columns:
        return ""
    table_name = json_file.split("/")[-1].split(".")[0]
    create_table_sql = f"CREATE TABLE [{table_name}] (\nSTT INT IDENTITY(1,1) PRIMARY KEY,\n"
    create_table_sql += ",\n".join(columns)
    create_table_sql += "\n);"
    return create_table_sql

def gen_insert_statements(json_file):
    data = read_data(json_file)  # hàm đọc json trả về list dict
    table_name = json_file.split("/")[-1].split(".")[0]
    insert_statements = []
    for item in data:
        columns = ", ".join(f"[{k}]" for k in item.keys())
        # xử lý giá trị phù hợp với kiểu SQL: strings có ' thì escape
        values = []
        for v in item.values():
            if isinstance(v, str):
                escaped = v.replace("'", "''")  # escape dấu nháy đơn
                values.append(f"N'{escaped}'")
            elif v is None:
                values.append("NULL")
            elif isinstance(v, bool):
                values.append('1' if v else '0')
            else:
                values.append(str(v))
        values_str = ", ".join(values)
        insert_statements.append(f"INSERT INTO [{table_name}] ({columns}) VALUES ({values_str});")

    return "\n".join(insert_statements)

def cursor(text):
    conn =  SQL_connect("Config/QuanLyXeDB.json")
    try:
        cursor = conn.cursor()
        cursor.execute(text)
        conn.commit()
    except Exception as dogshit:
        print(f"DUMP: {dogshit}")
    finally:
        cursor.close()
        conn.close()

output_folder = 'BackupData/Data'
def fetch_data_as_json(query, config):
    conn = SQL_connect(config)
    cursor = conn.cursor()
    cursor.execute(query)
    
    columns = [column[0] for column in cursor.description]
    rows = cursor.fetchall()

    result_list = []
    for row in rows:
        # Bỏ cột STT
        row_dict = {col: val for col, val in zip(columns, row) if col != 'STT'}
        result_list.append(row_dict)
    
    cursor.close()
    conn.close()
    
    return json.dumps(result_list, ensure_ascii=False, indent=2)

def backup_table_to_json(table_name, config):
    query = f"SELECT * FROM {table_name}"
    json_data = fetch_data_as_json(query, config)
    with open(f"{output_folder}/{table_name}.json", "w", encoding="utf-8") as f:
        f.write(json_data)






# for table in ['users', 'data', 'dashboard_data', 'slot']:
#     backup_table_to_json(table, "Config/QuanLyXeDB.json")
# cursor(Gen_table("static/data.json"))
# cursor(gen_insert_statements("static/data.json"))
# cursor(Gen_table("static/dashboard_data.json"))
# cursor(gen_insert_statements("static/dashboard_data.json"))
# cursor(Gen_table("static/slot.json"))
# cursor(gen_insert_statements("static/slot.json"))
# cursor(Gen_table("static/users.json"))
# cursor(gen_insert_statements("static/users.json"))
# cursor(Gen_table("static/xe_logger.json"))
# cursor(gen_insert_statements("static/xe_logger.json"))