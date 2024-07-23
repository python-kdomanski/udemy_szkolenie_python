import smtplib

mailFrom = 'Your automation system'
mailTo = ['krisdk@poczta.onet.pl', 'krzysztof.domanski@onet.pl']
mailSubject = 'Tytul wiadomosci'
mailBody='''Hello

Test2
Test3
'''

message = '''From: {}
Subject: {}

{}
'''.format(mailFrom,mailSubject,mailBody)

user = 'pl.lowca@gmail.com'
password = 'jikh qfdw qfpn hsiu'

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo() #przedstawienie się serwerowi
    server.login(user,password)
    server.sendmail(user, mailTo, message)
    server.close()
    print('mail sent')
except:
    print('Blad wysylki e-mail')
