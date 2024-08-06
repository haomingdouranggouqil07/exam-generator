import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from convert import generate_exam


def send_email():
    filename = generate_exam()
    #创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = Header("qiang__liu@163.com")
    message['To'] =  Header("475397804@qq.com")
    subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')

    sender = 'qiang__liu@163.com'
    sender_pass = 'GSCGRFKRLRGXWLYK'
    receivers = ['475397804@qq.com']
    #邮件正文内容
    message.attach(MIMEText('这是 试卷邮件发送测试……', 'plain', 'utf-8'))
    # 构造附件1，传送当前目录下的 test.txt 文件
    att_doc = MIMEText(open(filename, 'rb').read(), 'base64', 'utf-8')
    att_doc["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att_doc["Content-Disposition"] = 'attachment; filename="output.docx"'
    message.attach(att_doc)
    # 
    try:
        server=smtplib.SMTP_SSL("smtp.163.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(sender, sender_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(sender, receivers, message.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")