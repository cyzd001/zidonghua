import flask
import json


server = flask.Flask(__name__)

@server.route('/zhifubao', methods=['get', 'post'])
def zhifubao():
    message = {'msg': '支付宝支付成功', 'msg_code': "1000"}
    return json.dumps(message, sort_keys=True, indent=2, ensure_ascii=False)

# server.run(port=8079,host="0.0.0.0")
server.run(port=8079, host="192.168.18.38")





