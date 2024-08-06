import json
from flask import Flask, request, jsonify
import logging  
from logging.handlers import RotatingFileHandler
from sendEmail import send_email
from utils import getDatePath

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

if __name__ == '__main__':  
    # 启动Flask服务器，监听5000端口  
    app.run(debug=False, port=9527)