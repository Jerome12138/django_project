__author__ = "Jerome Chang"
import sqlite3


# 定义查询结果返回方式
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


# 获取数据，返回值为字典形式
def get_data():
    # 连接数据库
    conn = sqlite3.connect(r'E:\Downloads\学习视频\Python\Code\django_project\app1\mysql.db')
    conn.row_factory = dict_factory
    cursor = conn.cursor()
    # cursor.execute('select * from work_record where ROWID=?', (row_id,))
    cursor.execute('select * from work_record')
    # col_name_list = [tuple[0] for tuple in cursor.description]
    # print(col_name_list)
    res = cursor.fetchall()
    # res.insert(0,col_name_list)
    cursor.close()
    conn.close()
    return res


# 查询记录总数
def get_rows():
    # 连接数据库
    conn = sqlite3.connect(r'E:\Downloads\学习视频\Python\Code\django_project\app1\mysql.db')
    cursor = conn.cursor()
    cursor.execute('select count(*) from work_record')
    total = cursor.fetchone()
    cursor.close()
    conn.close()
    return total[0]


#
def add_data():
    pass


#
# print(get_data()[0])
# print(get_rows())


def transfer_data():
    from app1 import models
    data = get_data()
    # models.WorkData.objects.all().delete()
    for row in data:
        row['company_name'] = row.pop('公司名称')
        row['products'] = row.pop('主要产品')
        row['work_place'] = row.pop('工作地点')
        row['salary'] = row.pop('薪资')
        row['preaching_time'] = row.pop('宣讲时间')
        row['preaching_place'] = row.pop('宣讲地点')
        row['preaching'] = row.pop('宣讲')
        row['delivery'] = row.pop('投递')
        row['delivery_time'] = row.pop('投递时间')
        row['position_1'] = row.pop('职位1')
        row['position_2'] = row.pop('职位2')
        row['assessment'] = row.pop('测评')
        row['examination'] = row.pop('笔试')
        row['interview'] = row.pop('面试')
        row['status'] = row.pop('状态')
        row['notes'] = row.pop('备注')
        row['preaching_information_link'] = row.pop('宣讲信息')
        row['delivery_link'] = row.pop('网申链接')
        # print(row)
        models.WorkData.objects.create(**row)

def status_create():
    from app1 import models
    models.Status.objects.create(status='待宣讲')
    models.Status.objects.create(status='待测评')
    models.Status.objects.create(status='待面试')
    models.Status.objects.create(status='待通知')
    models.Status.objects.create(status='签约')
    models.Status.objects.create(status='未签')
    models.Status.objects.create(status='放弃')
    models.Status.objects.create(status='凉凉')

# transfer_data()
# status_create()