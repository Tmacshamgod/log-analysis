import CONF
import smtplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart

def sendmail():
    COMMASPACE = ','
    TO_MAIL = ["jeffzhang@sample.com", "allie@sample.com"]
    
    msg = MIMEMultipart()
    msg['Subject'] = CONF.MSG_SUBJECT
    msg['From'] = CONF.FROM_MAIL
    msg['To'] = COMMASPACE.join(TO_MAIL)
    msg_content = """\
            <html>
                <body>
                    <p>
                        Here is the download link<br>
                        <a href="http://10.103.0.5:8888/download">link</a><br>
                        Please do not reply, thanks!
                    </p>
                </body>
            </html>
            """
    msg.attach(MIMEText(msg_content, 'html', _charset='utf8'))

    try:
        MAIL = smtplib.SMTP()
        MAIL.connect(CONF.MAIL_HOST)
        MAIL.login(CONF.MAIL_USER, CONF.MAIL_PWD)
        MAIL.sendmail(CONF.FROM_MAIL, TO_MAIL, msg.as_string())
        MAIL.close()
        print "send Email successfully!"
        return True
    except Exception, e:
        print "error, %s" % (e)
        return False
if __name__ == '__main__':
    sendmail()
