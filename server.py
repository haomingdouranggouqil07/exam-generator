import json
from flask import Flask, request, jsonify
import logging  
from logging.handlers import RotatingFileHandler
from sendEmail import send_email
from utils import getDatePath
import hashlib

# 配置日志记录器  
logger = logging.getLogger(__name__)  
logger.setLevel(logging.INFO)  
  
# 创建一个文件处理器，用于写入日志文件  
# maxBytes和backupCount参数是RotatingFileHandler特有的，用于日志轮转  
handler = RotatingFileHandler("{}/{}{}".format("./logs", getDatePath(), '.log'), maxBytes=10240, backupCount=5)  
handler.setLevel(logging.INFO)  
  
# 创建一个日志格式器，并将其添加到处理器中  
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  
handler.setFormatter(formatter) 
# 将处理器添加到日志记录器中  
logger.addHandler(handler)  
  
app = Flask(__name__) 
@app.route('/math', methods=['POST'])  
def post_data():  
    # 从请求体中获取JSON数据  
    data = request.get_json()  
    logger.info('Received POST request to /math, {}'.format(json.dumps(data, indent=4)))
    try:
        send_email()
        return jsonify({'message': 'success'}), 200  
    except:
        logger.error('Received POST request to /math, {}'.format(json.dumps(data, indent=4)))
        return jsonify({'message': 'error.'}), 400  
    # 向客户端发送响应  

@app.route('/wx', methods=['GET'])  
def get_handle():  
    try:
        data = request.get_json()  
        if len(data) == 0:
            return "hello, this is handle view"
        signature = data.signature
        timestamp = data.timestamp
        nonce = data.nonce
        echostr = data.echostr
        token = "lq0508" #请按照公众平台官网\基本配置中信息填写

        list = [token, timestamp, nonce]
        list.sort()
        sha1 = hashlib.sha1()
        map(sha1.update, list)
        hashcode = sha1.hexdigest()
        print("handle/GET func: hashcode, signature: ", hashcode, signature)
        if hashcode == signature:
            return echostr
        else:
            return ""
    except Exception as Argument:
        return Argument 

if __name__ == '__main__':  
    # 启动Flask服务器，监听5000端口  
    app.run(debug=False, port=80)