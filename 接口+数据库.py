import json,flask
from flask import request,jsonify
import cx_Oracle as oracle



def jiaoyan(id):
    db = oracle.connect('pj_core', 'pj_core', '192.168.55.5:1521/ljcprd')
    cur = db.cursor()
    cur.execute('select a.SQDLZH,b.SYR_SJRWJBXX_ID,b.SYR_SYZTJC_ID from SYR_SQGX a,SYR_SJYGJBXX b where b.SYR_SQGX_ID=a.ID and a.SQDLZH=%r'%id)
    row = cur.fetchone()
    db.close()
    return row
server = flask.Flask(__name__)
@server.route('/chaxun', methods=['get', 'post'])
# def chaxun():
#     SJH = request.json.get('SJH')
#     print(SJH)
#     if SJH == jiaoyan(SJH)[0]:
#         message = {'id': jiaoyan(SJH)[1], 'msg_code': "200"}
#         return json.dumps(message, sort_keys=True, indent=2, ensure_ascii=False)
#     else:
#         message = {'miaoshu': "系统不存在输入的手机号", 'msg_code': "300"}
#         return json.dumps(message, sort_keys=True, indent=2, ensure_ascii=False)
def chaxun():
    number = request.values.get('SJH')
    result = jiaoyan(number)
    print(result)
    if result == None:
        message = {'id': "账号不存在", 'msg_code': "201"}
        return json.dumps(message, sort_keys=True, indent=2, ensure_ascii=False)
        # return jsonify(result[1])
    elif result[0] == number :
        message={'miaoshu': result[1], 'msg_code': "200"}
        return json.dumps(message, sort_keys=True, indent=2, ensure_ascii=False)
    else:
        message={'miaoshu': "系统错误", 'msg_code': "300"}
        return json.dumps(message, sort_keys=True, indent=2, ensure_ascii=False)
server.run(port=8074, host="192.168.18.38")
17772507772

