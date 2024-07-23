import smtplib
import functools

def SendInfoeEmail(user, password, mailFrom, mailTo, mailSubject, mailBody):
    message = '''From: {}
    Subject: {}
    
    {}
    '''.format(mailFrom,mailSubject,mailBody)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com',465)
        server.ehlo() #przedstawienie się serwerowi
        server.login(user,password)
        server.sendmail(user, mailTo, message)
        server.close()
        print('mail sent')
        return True
    except:
        print('Blad wysylki e-mail')
        return False

mailFrom = 'Your automation system'
mailTo = ['krisdk@poczta.onet.pl', 'krzysztof.domanski@onet.pl']
mailSubject = 'Tytul wiadomosci'
mailBody='''
Hello partial
Test1
Test2
Test3
'''
user = 'pl.lowca@gmail.com'
password = 'jikh qfdw qfpn hsiu'
#SendInfoeEmail(user,password,mailFrom,mailTo,mailSubject,mailBody)

SendInfoEmailFromGmail = functools.partial(SendInfoeEmail, user,password, mailSubject='Execution alert')

SendInfoEmailFromGmail(mailFrom=mailFrom,mailTo=mailTo,mailBody=mailBody)