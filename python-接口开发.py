import flask
from flask import request
from flask import jsonify


"""
接口协议：http、webservice、rpc等。
请求方式：get、post方式
请求参数格式：
a. get请求都是通过url?param=xxx&param1=xxx
b. post请求的请求参数常用类型有：application/json、application/x-www-form-urlencoded、multipart/form-data、text/html等。
"""


'''
flask： web框架，可以通过flask提供的装饰器@server.route()将普通函数转换为服务
登录接口，需要传url、username、passwd
'''

#创建一个服务，把当前这个python文件当做一个服务
server = flask.Flask(__name__)
#server.config['JSON_AS_ASCII'] = False
# @server.route()可以将普通函数转变为服务  登录接口的路径、请求方式
@server.route('/login', methods=['get'])
def login():
    # 获取通过url请求传参的数据19     username = request.values.get('name')
    # 获取url请求传的密码，明文
    pwd = request.values.get('pwd')
    # 判断用户名、密码都不为空，如果不传用户名、密码则username和pwd为None
    if username and pwd:
        # 获取加密后的密码
        password = tools.md5_pwd(pwd)
        # 执行sql，如果查询的username和password不为空，说明数据库存在admin的账号
        sql = 'select name,password from test where name= "%s" and password= "%s";' % (username, password)
        # 从数据查询结果后，res返回是元组
        res = OP_db.getconn(
            host=settings.mysql_info['host'],
            user=settings.mysql_info['user'],
            passwd=settings.mysql_info['pwd'],
            db=settings.mysql_info['db'],
            port=settings.mysql_info['port'],
            sql=sql)

        if res:  # res的结果不为空，说明找到了username=admin的用户，且password为加密前的123456
             resu = {'code': 200, 'message': '登录成功'}
             return jsonify(resu)
        else:
             resu = {'code': -1, 'message': '账号/密码错误'}
             return jsonify(resu)
    else:
         res = {'code': 999, 'message': '必填参数未填写'}
         return jsonify(res)
if __name__ == '__main__':
    server.run(debug=True, port=8888, host=0.0.0.0)  # 指定端口、host,0.0.0.0代表不管几个网卡，任何ip都可以访问


''' 
注册接口： 
post请求，请求参数入参类型json 
{
"username":"aaa",
"pwd":"123456",
"c_pwd":"123456"
}
'''
server = flask.Flask(__name__)
@ server.route('/register', methods=['GET', 'POST'])
def registerPost():
     # 判断接口的请求方式是GET还是POST
    if request.method == 'POST':
     # 获取请求参数是json格式，返回结果是字典
         params = request.json
         username = params.get('username')
         pwd = params.get('pwd')
         confirmpwd = params.get('confirmpwd')
         if username and pwd and confirmpwd:  # 判断输入的用户名、密码、确认密码都不为空
              select_sql = 'select username from lhldemo  where username = "%s" ;' % username
              # 查询注册的用户是否存在数据库，如果存在，则username不为空，否则username为空
              res_mysql = opMysql.op_select(select_sql)
              if res_mysql:
                    return jsonify({"code": 999, "mesg": "用户已注册"})
              else:
                   if pwd == confirmpwd:  # 判断pwd和confirmpwd一致
                        new_pwd = md5_create.md5_test(pwd)  # 加密后的密码
                        insert_sql = 'insert into lhldemo(username,password) values("%s", "%s") ;' % (username, new_pwd)
                        opMysql.op_insert(insert_sql)
                        return jsonify({"code": 200, "msg": "注册成功"})
                   else:
                        return jsonify({"code": 998, "msg": "密码不一样"})

        else:
            return jsonify({"code": 504, "msg": "必填项不能为空"})
    else:
         return jsonify({"code": 201, "msg": "请求方式不正确"})
if __name__ == '__main__':
# port可以指定端口，默认端口是5000
# host写成0.0.0.0的话，其他人可以访问，代表监听多块网卡上面，默认是127.0.0.1
    server.run(debug=True, port=8899, host='0.0.0.0')




''' 
注册接口： 
post请求，请求参数入参类型json 
{
"username":"aaa",
"pwd":"123456",
"c_pwd":"123456"
}
'''
server = flask.Flask(__name__)
@ server.route('/register', methods=['GET', 'POST'])
def registerPost():
     # 判断接口的请求方式是GET还是POST
    if request.method == 'POST':
     # 获取请求参数是json格式，返回结果是字典
         username = request.values.get('username')
         pwd = request.values.get('pwd')
         confirmpwd = request.values.get('confirmpwd')
         if username and pwd and confirmpwd:  # 判断输入的用户名、密码、确认密码都不为空
              select_sql = 'select username from lhldemo  where username = "%s" ;' % username
              # 查询注册的用户是否存在数据库，如果存在，则username不为空，否则username为空
              res_mysql = opMysql.op_select(select_sql)
              if res_mysql:
                    return jsonify({"code": 999, "mesg": "用户已注册"})
              else:
                   if pwd == confirmpwd:  # 判断pwd和confirmpwd一致
                        new_pwd = md5_create.md5_test(pwd)  # 加密后的密码
                        insert_sql = 'insert into lhldemo(username,password) values("%s", "%s") ;' % (username, new_pwd)
                        opMysql.op_insert(insert_sql)
                        return jsonify({"code": 200, "msg": "注册成功"})
                   else:
                        return jsonify({"code": 998, "msg": "密码不一样"})
        else:
            return jsonify({"code": 504, "msg": "必填项不能为空"})
    else:
         return jsonify({"code": 201, "msg": "请求方式不正确"})
if __name__ == '__main__':
# port可以指定端口，默认端口是5000
# host写成0.0.0.0的话，其他人可以访问，代表监听多块网卡上面，默认是127.0.0.1
    server.run(debug=True, port=8899, host='0.0.0.0')

http://www.php.cn/python-tutorials-373157.html


