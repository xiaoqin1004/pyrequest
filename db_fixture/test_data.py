import sys
sys.path.append('../db_fixture')
from mysql_db import DB


# 创建测试数据
datas = {
    # 发布会表数据
    'sign_event': [
        {'id': 101, 'name': 'event 01', 'status': 0, 'limit': 2000, 'address': 'nanjing',
            'start_time': '2018-09-20 09:00:00'},
        {'id': 102, 'name': 'event 02', 'status': 1, 'limit': 2000, 'address': 'nanjing',
            'start_time': '2018-09-20 09:00:00'},
        {'id': 103, 'name': 'event 03', 'status': 1, 'limit': 2000, 'address': 'nanjing',
            'start_time': '2018-09-20 09:00:00'},
        {'id': 104, 'name': 'event 04', 'status': 1, 'limit': 2000, 'address': 'nanjing',
            'start_time': '2018-09-20 09:00:00'},
        {'id': 105, 'name': 'event 05', 'status': 1, 'limit': 2000, 'address': 'nanjing',
         'start_time': '2018-09-20 09:00:00'},
    ],
    # 嘉宾表数据
    'sign_guest': [
        {'id': 91, 'realname': 'helen', 'phone': 131333333333, 'email': 'helen@mail.com', 'sign': 0,
            'event_id': 101},
        {'id': 92, 'realname': 'jack', 'phone': 122333333333, 'email': 'jack@mail.com', 'sign': 1,
            'event_id': 101},
        {'id': 93, 'realname': 'lucy', 'phone': 133333333333, 'email': 'lucy@mail.com', 'sign': 0,
            'event_id': 102},
    ]
}


# 将测试数据插入表
def init_data():
    # 用于读取datas字典中的数据。先调用DB类中的clear方法清除表数据，然后循环调用insert方法插入数据
    db = DB()
    for table, data in datas.items():
        db.clear(table)
        for d in data:
            db.insert(table, d)
    db.close()


if __name__ == '__main__':
    init_data()
