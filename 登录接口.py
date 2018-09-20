import json,flask
from flask import request,jsonify
import cx_Oracle as oracle
import hashlib


def jiaoyan(user):
    db = oracle.connect('pj_core', 'pj_core', '192.168.55.5:1521/ljcprd')
    cur = db.cursor()
    cur.execute('select SQDLZH,DLMM from SYR_SQGX where SQDLZH=%r' % user)
    row = cur.fetchone()
    db.close()
    return row
def jiami(pwd):
    hl = hashlib.md5(pwd.encode(encoding='UTF-8')).hexdigest().upper()
    return hl
server = flask.Flask(__name__)
@server.route('/login', methods=['get', 'post'])
def denglu():
    number = request.values.get('SJH')
    password = request.values.get('PWD')
    if number== '':
        message = {'msg': "账号为空", 'msg_code': "202"}
        return json.dumps(message, sort_keys=True, indent=2, ensure_ascii=False)
    elif number.isdigit() == False:
        message = {'msg': "账号格式有误，为纯数字", 'msg_code': "201"}
        return json.dumps(message, sort_keys=True, indent=2, ensure_ascii=False)
    else:
        result = jiaoyan(number)
        mima = jiami(password)
        print(password,mima,result[1])
        if result == None:
            message = {'id': "账号不存在", 'msg_code': "203"}
            return json.dumps(message, sort_keys=True, indent=2, ensure_ascii=False)
        elif result[0]==number:
            if mima == result[1]:
                message = {'id': "成功登录", 'msg_code': "200"}
                return json.dumps(message, sort_keys=True, indent=2, ensure_ascii=False)
            elif mima != result[1]:
                message = {'id': "密码有误", 'msg_code': "204"}
                return json.dumps(message, sort_keys=True, indent=2, ensure_ascii=False)
            else:
                message = {'id': "请再次输入", 'msg_code': "205"}
                return json.dumps(message, sort_keys=True, indent=2, ensure_ascii=False)


    # elif number.isdigit() == True:
    #     result = jiaoyan(number)
    #     if result == None:
    #     message = {'id': "输入为空", 'msg_code': "201"}
    #     return json.dumps(message, sort_keys=True, indent=2, ensure_ascii=False)
    #     # return jsonify(result[1])
    #     elif result[0] == number:
    #     message = {'miaoshu': result[1], 'msg_code': "200"}
    #     return json.dumps(message, sort_keys=True, indent=2, ensure_ascii=False)



server.run(port=8073, host="192.168.18.38")




