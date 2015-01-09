# encoding: utf-8
# author: fanko24@gmail.com


import smtplib
from email.mime.text import MIMEText


# send a mail with title and content to a list of email
def send_mail(to_mail, title, content):
    # the parameter of sending mail
    mail_host="mail.rong360.com"
    mail_user="cro_automail@rong360.com"
    mail_pass="izrgblhg84"
    mail_postfix="rong360.com"

    # from mail
    from_mail = mail_user + "<" + mail_user + "@" + mail_postfix + ">"

    # the message
    message = MIMEText(content, _charset="utf-8")
    message['Subject'] = title
    message['From'] = from_mail
    message['To'] = to_mail

    # send the mail
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

