import sys
import os
import psycopg2

db=psycopg2.connect(host="192.168.0.21",dbname="lb-sites",port="5504",user="lb-site-1",password="lb-site-1")
# db=psycopg2.connect("192.168.0.21","5504","lb-site-1","lb-sites","lb-site-1")
cur=db.cursor()
# cur.execute("select * from bill_salary_ratio where agenter_name = 'sb001'; ")
cur.execute("SELECT lb_salary('2018-07-03')")
# cur.execute("select * from bill_salary_ratio where agenter_name = 'sb001';")

# cur.execute("select * from bill_salary where expect = '2018-06-26' and agenter_name in('sb001','sb002');")

# cur.execute("select * from bill_salary where expect = '2018-06-26' and agenter_name = 'sb001';")
# cur.execute("select * from bill_salary where expect = '2018-06-26' and agenter_name = 'sb002';")
'''单条数据'''
# rows = cur.fetchone()  #获取第一条数据
# for i in range(0,9):
#     if rows[i] == "sb001" :
#         print(rows[i], end="")
#         print("sb001工资方案梯度二设置成功")
#     else:
#         print("sb001工资方案未设置成功")
#
# print(rows)
# print(rows[0])
'''多条数据'''
# rows = cur.fetchall()
# for i in rows:
#     id = i[0]
#     agenter_id = i[1]
#     agenter_name = i[2]
#     agenter_level = i[3]
#     grade_id = i[4]
#     ratio = i[5]
#     ratio_limit = i[6]
#     project_id = i[7]
#     project_name = i[8]
#     print("id=%s,agenter_id=%s,agenter_name=%s,agenter_level=%s,grade_id=%s,ratio=%s,ratio_limit=%s,progect_id=%s,progect_name=%s"% \
#               (id,agenter_id,agenter_name,agenter_level,grade_id,ratio,ratio_limit,project_id,project_name))
#     if agenter_name == 'sb001'and ratio == 0.00:
#         print("sb001工资方案梯度一设置成功")
#     elif agenter_name == "sb001" and ratio == 15.00:
#         print("sb001工资方案梯度二设置成功")
#     else:
#         print("未找到设置的工资方案")
cur.execute("select * from bill_salary where expect = '2018-07-03'order by id desc")
rows = cur.fetchall()
for i in rows:
    print(i)
# cur.execute("select * from bill_salary where expect = '2018-07-03'")
cur.scroll(4,'absolute')
rown = cur.fetchone()
print(rown)
# cur.execute("delete from bill_salary where expect = '2018-07-03';")
# print(cur.fetchone())
# db.commit()

db.close()