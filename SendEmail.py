import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(to_email, subject, body):
    # 发件人信息
    from_email = input("请替换为你的QQ邮箱: ")  # 请替换为你的QQ邮箱
    password = input("请替换为你的邮箱密码的STMP的密码: ") #  这是我自己的STMp密码

    # 创建邮件对象
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # 添加邮件正文
    msg.attach(MIMEText(body, 'plain'))

    try:
        # 连接到QQ邮箱的SMTP服务器
        server = smtplib.SMTP('smtp.qq.com', 587)
        server.starttls()  # 启用TLS加密
        server.login(from_email, password)  # 登录邮箱

        # 发送邮件
        server.sendmail(from_email, to_email, msg.as_string())
        print(f'邮件成功发送到 {to_email}')
    except Exception as e:
        print(f'发送邮件失败: {e}')
    finally:
        server.quit()  # 关闭连接


def main():
    # 示例：发送邮件
    recipients = ['template@email.com']  # 收件人列表
    subject = input("请输入您的邮件主题: ")  # 邮件主题
    body = '你的邮件正文'  # 邮件正文

#这里批量发送给里面的接收者。
    for recipient in recipients:
        send_email(recipient, subject, body)


if __name__ == '__main__':
    main()