import smtplib

to = 'ychen@thorlabs.com'
gmail_user = '18621300389@163.com'
gmail_pwd = 'win11pes'
smtpserver = smtplib.SMTP("mail.163.com")
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(gmail_user, gmail_pwd)
header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:testing \n'
print (header)
msg = header + '\n this is test msg from mkyong.com \n\n'
smtpserver.sendmail(gmail_user, to, msg)
print ('done!')
smtpserver.close()