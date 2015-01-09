# encoding: utf-8
# liuqiwen@rong360.com


import smtplib
from email.mime.text import MIMEText


# send a mail with title and content to a list of email
def send_mail(to_mail, title, content):
    mail_host="mail.rong360.com"
    mail_user="user"
    mail_pass="password"
    mail_postfix="rong360.com"

    from_mail = mail_user + "<" + mail_user + "@" + mail_postfix + ">"
    message = MIMEText(content, _charset="utf-8")
    message['Subject'] = title
    message['From'] = from_mail
    message['To'] = to_mail
    try:
        smtp = smtplib.SMTP()
        smtp.connect(mail_host)
        smtp.login(mail_user,mail_pass)
        smtp.sendmail(from_mail, to_mail, message.as_string())
        smtp.close()
        return True
    except Exception, e:
        print str(e)
        return False

if __name__ == '__main__':
    content = "This is a test warning mail for that something is wrong of uid-mapping, you should check it"
    mailto_list = ['liuqiwen@rong360.com', 'guoliang@rong360.com', 'zhangyunsong@rong360.com']
    for mailto in mailto_list:
        send_mail(mailto, "This is a test", content)

