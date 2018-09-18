# coding=utf8
from pymysql import connect, cursors
from pymysql.err import OperationalError
import os
import configparser as cparser

# =============读取db_config.ini文件设置===============
base_dir = str(os.path.dirname(os.path.dirname(__file__)))
base_dir = base_dir.replace('\\', '/')
file_path = base_dir + "/db_config.ini"

cf = cparser.ConfigParser()
cf.read(file_path)

host = cf.get("mysqlconf", "host")
port = cf.get("mysqlconf", "port")
db_name = cf.get("mysqlconf", "db_name")
user = cf.get("mysqlconf", "user")
password = cf.get("mysqlconf", "password")


# =============封装MYSQL基本操作===============
# 创建DB类
class DB:
    # __init__方法初始化数据库连接，通过connect()方法连接数据库
    def __init__(self):
        try:
            # 连接数据库
            self.conn = connect(host=host,
                                port=int(port),
                                db=db_name,
                                user=user,
                                password=password,
                                charset='utf8mb4',
                                cursorclass=cursors.DictCursor)
        except OperationalError as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    # 清除表数据
    def clear(self, table_name):
        real_sql = " delete from " + table_name + ";"
        with self.conn.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(real_sql)
        self.conn.commit()

    # 插入表数据
    def insert(self, table_name, table_data):
        # 对插入的数据做格式转化，将字典转化为插入SQL语句，方便测试数据的创建
        for key in table_data:
            table_data[key] = "'" + str(table_data[key])+"'"
        key = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        real_sql = " insert into " + table_name + "(" + key + ") values (" + value + ")"

        print(real_sql)

        with self.conn.cursor() as cursor:
            cursor.execute(real_sql)

        self.conn.commit()

    # 关闭数据库连接
    def close(self):
        self.conn.close()


if __name__ == '__main__':
    db = DB()
    table_name = "sign_event"
    data = {'id': 33, 'name': "oppo event", 'status': 1, 'limit': 2000, 'address': "nanjing",
            'start_time': '2018-09-14 09:18:22'}
    db.clear(table_name)
    db.insert(table_name, data)
    db.close()
